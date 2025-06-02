from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import BlogPost, Category
from django.utils import timezone
from django.utils.text import slugify
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Create quick sample posts for search variety'

    def handle(self, *args, **options):
        # Get all users
        users = list(User.objects.all())
        
        quick_posts = [
            # Technology
            {'title': 'Getting Started with Docker Containers', 'category': 'Technology', 'tags': ['docker', 'containers', 'devops', 'technology']},
            {'title': 'React Hooks: A Complete Guide', 'category': 'Technology', 'tags': ['react', 'javascript', 'hooks', 'frontend']},
            {'title': 'Introduction to Machine Learning with TensorFlow', 'category': 'Technology', 'tags': ['machine-learning', 'tensorflow', 'ai', 'python']},
            {'title': 'Building REST APIs with Node.js and Express', 'category': 'Technology', 'tags': ['nodejs', 'express', 'api', 'backend']},
            {'title': 'CSS Grid vs Flexbox: When to Use Which', 'category': 'Technology', 'tags': ['css', 'grid', 'flexbox', 'web-design']},
            
            # Travel
            {'title': 'Budget Travel Tips for Europe', 'category': 'Travel', 'tags': ['budget-travel', 'europe', 'backpacking', 'travel-tips']},
            {'title': 'Best Photography Spots in Japan', 'category': 'Travel', 'tags': ['photography', 'japan', 'travel', 'culture']},
            {'title': 'Digital Nomad Guide to Southeast Asia', 'category': 'Travel', 'tags': ['digital-nomad', 'remote-work', 'asia', 'travel']},
            {'title': 'Sustainable Tourism: How to Travel Responsibly', 'category': 'Travel', 'tags': ['sustainable-travel', 'eco-tourism', 'environment', 'responsible-travel']},
            {'title': 'Adventure Sports in New Zealand', 'category': 'Travel', 'tags': ['adventure', 'sports', 'new-zealand', 'outdoor']},
            
            # Food
            {'title': 'Mediterranean Diet: Health Benefits and Recipes', 'category': 'Food', 'tags': ['mediterranean', 'healthy-eating', 'diet', 'nutrition']},
            {'title': 'Vegan Protein Sources: Complete Guide', 'category': 'Food', 'tags': ['vegan', 'protein', 'plant-based', 'nutrition']},
            {'title': 'Sourdough Bread Making for Beginners', 'category': 'Food', 'tags': ['sourdough', 'bread', 'baking', 'fermentation']},
            {'title': 'Spice Guide: Essential Spices for Every Kitchen', 'category': 'Food', 'tags': ['spices', 'cooking', 'flavor', 'kitchen-basics']},
            {'title': 'Farm-to-Table Cooking: Seasonal Recipes', 'category': 'Food', 'tags': ['farm-to-table', 'seasonal', 'local-food', 'cooking']},
            
            # Lifestyle
            {'title': 'Morning Routines of Successful People', 'category': 'Lifestyle', 'tags': ['morning-routine', 'productivity', 'success', 'habits']},
            {'title': 'Mindfulness Meditation for Beginners', 'category': 'Lifestyle', 'tags': ['mindfulness', 'meditation', 'mental-health', 'wellness']},
            {'title': 'Sustainable Living: Reducing Your Carbon Footprint', 'category': 'Lifestyle', 'tags': ['sustainability', 'environment', 'green-living', 'eco-friendly']},
            {'title': 'Home Organization: Decluttering Your Space', 'category': 'Lifestyle', 'tags': ['organization', 'decluttering', 'home', 'minimalism']},
            {'title': 'Work-Life Balance in the Digital Age', 'category': 'Lifestyle', 'tags': ['work-life-balance', 'digital-wellness', 'productivity', 'mental-health']},
            
            # Business
            {'title': 'Social Media Marketing for Small Businesses', 'category': 'Business', 'tags': ['social-media', 'marketing', 'small-business', 'digital-marketing']},
            {'title': 'Cryptocurrency and Blockchain Basics', 'category': 'Business', 'tags': ['cryptocurrency', 'blockchain', 'finance', 'technology']},
            {'title': 'Project Management Best Practices', 'category': 'Business', 'tags': ['project-management', 'productivity', 'leadership', 'business']},
            {'title': 'E-commerce Trends for 2024', 'category': 'Business', 'tags': ['ecommerce', 'trends', 'online-business', 'retail']},
            {'title': 'Building a Personal Brand Online', 'category': 'Business', 'tags': ['personal-brand', 'online-presence', 'networking', 'career']}
        ]
        
        created_count = 0
        
        for post_data in quick_posts:
            # Check if post already exists
            if BlogPost.objects.filter(title=post_data['title']).exists():
                continue
            
            # Get random author
            author = random.choice(users)
            
            # Create or get category
            category, _ = Category.objects.get_or_create(
                name=post_data['category'],
                defaults={'slug': slugify(post_data['category'])}
            )
            
            # Generate simple content
            content = f"""This is a comprehensive guide about {post_data['title'].lower()}. 

In this article, we'll explore the key concepts, best practices, and practical tips that will help you understand and implement these ideas effectively.

## Key Points

- Understanding the fundamentals
- Practical implementation strategies  
- Common challenges and solutions
- Best practices and recommendations
- Future trends and considerations

## Getting Started

Whether you're a beginner or looking to expand your knowledge, this guide provides valuable insights and actionable advice.

## Conclusion

By following these guidelines and staying updated with the latest developments, you'll be well-equipped to succeed in this area.

Stay tuned for more detailed content and updates on this topic!"""
            
            excerpt = f"A comprehensive guide to {post_data['title'].lower()} with practical tips and best practices."
            
            # Create the post
            post = BlogPost.objects.create(
                title=post_data['title'],
                slug=slugify(post_data['title']),
                content=content,
                excerpt=excerpt,
                author=author,
                category=category,
                status='published',
                published_at=timezone.now() - timedelta(days=random.randint(1, 45))
            )
            
            # Add tags
            post.tags.add(*post_data['tags'])
            
            created_count += 1
            self.stdout.write(f'Created post: {post.title}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} quick sample posts!')
        )
        
        # Show total posts
        total_posts = BlogPost.objects.filter(status='published').count()
        self.stdout.write(f'Total published posts: {total_posts}')
        
        # Show categories and tags summary
        categories = Category.objects.all()
        self.stdout.write(f'Categories: {", ".join([cat.name for cat in categories])}')
        
        from taggit.models import Tag
        tags = Tag.objects.all()[:20]  # Show first 20 tags
        self.stdout.write(f'Sample tags: {", ".join([tag.name for tag in tags])}...')
