from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import BlogPost, Comment, Like
from django.utils import timezone
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Add sample comments and likes to blog posts'

    def handle(self, *args, **options):
        # Get all users and posts
        users = list(User.objects.all())
        posts = list(BlogPost.objects.filter(status='published'))
        
        if len(users) < 2:
            self.stdout.write(
                self.style.ERROR('Please create sample users first using: python manage.py create_sample_users')
            )
            return
        
        if len(posts) < 1:
            self.stdout.write(
                self.style.ERROR('No published posts found. Please create sample posts first.')
            )
            return
        
        # Sample comments by category
        comment_templates = {
            'Technology': [
                "Great explanation! This really helped me understand the concept better.",
                "Thanks for sharing this. I've been looking for a tutorial like this.",
                "Excellent post! Do you have any recommendations for further reading?",
                "This is exactly what I needed for my current project. Much appreciated!",
                "Very well written and easy to follow. Looking forward to more content like this.",
                "I tried this approach and it worked perfectly. Thanks for the detailed guide!",
                "Interesting perspective. I hadn't considered this approach before.",
                "Could you elaborate more on the security implications?",
                "This saved me hours of debugging. Thank you so much!",
                "Great tutorial! I'll definitely be bookmarking this for future reference."
            ],
            'Travel': [
                "Amazing photos! This place is definitely going on my bucket list.",
                "Thanks for the detailed travel tips. Very helpful for planning my trip.",
                "I've been to this place and can confirm it's as beautiful as described!",
                "Great recommendations! How long did you spend there?",
                "This looks incredible. What was your favorite part of the trip?",
                "Thanks for sharing your experience. This is very inspiring!",
                "I'm planning a similar trip. Any additional tips you'd recommend?",
                "Beautiful writing! You really captured the essence of the place.",
                "This makes me want to pack my bags right now!",
                "Excellent guide! I'll definitely use these tips for my next adventure."
            ],
            'Food': [
                "This recipe looks delicious! Can't wait to try it.",
                "I made this last night and it was amazing. Thank you for sharing!",
                "Great technique! I never thought to prepare it this way.",
                "This brings back memories of my grandmother's cooking.",
                "Perfect timing! I was just looking for a recipe like this.",
                "The photos are making me hungry! Definitely trying this weekend.",
                "Thanks for the detailed instructions. Very easy to follow.",
                "I love how you explained the cultural background of this dish.",
                "This is now my go-to recipe. So flavorful and authentic!",
                "Excellent post! Do you have any vegetarian variations?"
            ],
            'Lifestyle': [
                "This is so inspiring! I'm definitely going to try implementing these changes.",
                "Thank you for sharing your journey. It's very motivating.",
                "I needed to read this today. Perfect timing!",
                "Great advice! I've been struggling with this exact issue.",
                "This really resonates with me. Thanks for the honest perspective.",
                "I've been following similar practices and can confirm they work!",
                "Very thoughtful post. I appreciate the practical tips.",
                "This is exactly the mindset shift I needed. Thank you!",
                "I love how you broke this down into actionable steps.",
                "Inspiring content! Looking forward to your next post."
            ],
            'Business': [
                "Excellent insights! This aligns with what we're seeing in our industry.",
                "Very timely post. These trends are definitely worth watching.",
                "Great analysis! Do you think this will impact small businesses too?",
                "This is exactly what our team needed to hear. Thank you!",
                "Insightful post! I'll be sharing this with my colleagues.",
                "Thanks for the practical advice. Very applicable to our situation.",
                "This confirms what we've been experiencing. Great to see the data.",
                "Excellent breakdown of complex topics. Very well explained.",
                "This gives me a lot to think about for our strategy.",
                "Great post! Looking forward to seeing how this evolves."
            ]
        }
        
        # Generic positive comments
        generic_comments = [
            "Fantastic post! Really enjoyed reading this.",
            "Thank you for sharing your knowledge and experience.",
            "This is incredibly helpful. Much appreciated!",
            "Great content as always. Keep up the excellent work!",
            "I learned something new today. Thanks for this!",
            "Very well researched and presented. Excellent work!",
            "This is going to be very useful. Thank you!",
            "Brilliant insights! Thanks for sharing.",
            "I really appreciate the time you put into this post.",
            "This is exactly what I was looking for. Perfect!"
        ]
        
        comments_created = 0
        likes_created = 0
        
        # Add comments to posts
        for post in posts:
            # Determine number of comments (1-8 per post)
            num_comments = random.randint(1, 8)
            
            # Get appropriate comment templates
            category_name = post.category.name if post.category else 'Generic'
            available_comments = comment_templates.get(category_name, generic_comments)
            
            for _ in range(num_comments):
                # Select random user (not the post author)
                available_users = [u for u in users if u != post.author]
                if not available_users:
                    continue
                    
                commenter = random.choice(available_users)
                
                # Select random comment
                comment_text = random.choice(available_comments)
                
                # Create comment with random timestamp
                days_ago = random.randint(0, 30)
                comment_time = timezone.now() - timedelta(days=days_ago, hours=random.randint(0, 23))
                
                comment = Comment.objects.create(
                    post=post,
                    author=commenter,
                    content=comment_text,
                    created_at=comment_time
                )
                
                comments_created += 1
                
                # 30% chance of a reply to this comment
                if random.random() < 0.3 and len(available_users) > 1:
                    # Get different user for reply
                    reply_users = [u for u in available_users if u != commenter]
                    if reply_users:
                        replier = random.choice(reply_users)
                        
                        reply_texts = [
                            "Thanks for the feedback!",
                            "I'm glad you found it helpful!",
                            "Great point! I hadn't considered that.",
                            "Thank you for sharing your experience!",
                            "I appreciate your kind words!",
                            "That's a really good question. Let me think about that.",
                            "Thanks for reading and commenting!",
                            "I'm so happy this was useful to you!",
                            "Your feedback means a lot to me!",
                            "Thanks for the encouragement!"
                        ]
                        
                        reply_time = comment_time + timedelta(hours=random.randint(1, 48))
                        
                        Comment.objects.create(
                            post=post,
                            author=replier,
                            content=random.choice(reply_texts),
                            parent=comment,
                            created_at=reply_time
                        )
                        
                        comments_created += 1
        
        # Add likes to posts
        for post in posts:
            # Each user has a 40% chance of liking each post
            for user in users:
                if user != post.author and random.random() < 0.4:
                    # Check if like already exists
                    if not Like.objects.filter(post=post, user=user).exists():
                        days_ago = random.randint(0, 30)
                        like_time = timezone.now() - timedelta(days=days_ago, hours=random.randint(0, 23))
                        
                        like = Like.objects.create(
                            post=post,
                            user=user,
                            created_at=like_time
                        )
                        
                        likes_created += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {comments_created} comments and {likes_created} likes!')
        )
        
        # Show statistics
        total_posts = BlogPost.objects.filter(status='published').count()
        total_comments = Comment.objects.count()
        total_likes = Like.objects.count()
        
        self.stdout.write(f'\nStatistics:')
        self.stdout.write(f'Total posts: {total_posts}')
        self.stdout.write(f'Total comments: {total_comments}')
        self.stdout.write(f'Total likes: {total_likes}')
        self.stdout.write(f'Average comments per post: {total_comments/total_posts:.1f}')
        self.stdout.write(f'Average likes per post: {total_likes/total_posts:.1f}')
