from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .models import BlogPost, Comment, Like, Category
from .forms import BlogPostForm, CommentForm, SearchForm
from taggit.models import Tag


def home(request):
    posts = BlogPost.objects.filter(status='published').order_by('-published_at')
    featured_posts = posts[:3]  # Top 3 recent posts
    
    # Popular tags
    popular_tags = Tag.objects.annotate(
        post_count=Count('taggit_taggeditem_items')
    ).order_by('-post_count')[:10]
    
    # Pagination
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'featured_posts': featured_posts,
        'popular_tags': popular_tags,
    }
    return render(request, 'blog/home.html', context)


def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    
    # Increment views
    post.views += 1
    post.save(update_fields=['views'])
    
    # Comments
    comments = post.comments.filter(parent=None).order_by('-created_at')
    
    # Check if user liked the post
    user_liked = False
    if request.user.is_authenticated:
        user_liked = Like.objects.filter(post=post, user=request.user).exists()
    
    # Comment form
    comment_form = CommentForm()
    
    # Related posts
    related_posts = BlogPost.objects.filter(
        tags__in=post.tags.all(),
        status='published'
    ).exclude(id=post.id).distinct()[:3]
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'user_liked': user_liked,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def edit_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, author=request.user)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = BlogPostForm(instance=post)
    
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, author=request.user)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blog:home')
    
    return render(request, 'blog/delete_post.html', {'post': post})


@login_required
def my_posts(request):
    posts = BlogPost.objects.filter(author=request.user).order_by('-created_at')

    # Calculate statistics
    total_posts = posts.count()
    published_posts = posts.filter(status='published').count()
    draft_posts = posts.filter(status='draft').count()
    total_views = sum(post.views for post in posts)

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'total_posts': total_posts,
        'published_posts': published_posts,
        'draft_posts': draft_posts,
        'total_views': total_views,
    }

    return render(request, 'blog/my_posts.html', context)


@login_required
@require_POST
def add_comment(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    form = CommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        
        # Handle reply to comment
        parent_id = request.POST.get('parent_id')
        if parent_id:
            comment.parent = get_object_or_404(Comment, id=parent_id)
        
        comment.save()
        messages.success(request, 'Comment added successfully!')
    
    return redirect('blog:post_detail', slug=slug)


@login_required
@require_POST
def toggle_like(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    like, created = Like.objects.get_or_create(post=post, user=request.user)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': post.get_like_count()
    })


def search_posts(request):
    form = SearchForm()
    posts = BlogPost.objects.none()
    query = None

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = BlogPost.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query),
                status='published'
            ).distinct().order_by('-published_at')

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'posts': page_obj,
        'query': query,
    }
    return render(request, 'blog/search.html', context)


def tag_posts(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = BlogPost.objects.filter(tags=tag, status='published').order_by('-published_at')

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tag': tag,
        'posts': page_obj,
    }
    return render(request, 'blog/tag_posts.html', context)


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.filter(category=category, status='published').order_by('-published_at')

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'posts': page_obj,
    }
    return render(request, 'blog/category_posts.html', context)
