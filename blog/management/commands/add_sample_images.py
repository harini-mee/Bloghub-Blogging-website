from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from blog.models import BlogPost
import requests
from io import BytesIO
from PIL import Image
import os

class Command(BaseCommand):
    help = 'Add sample images to blog posts'

    def handle(self, *args, **options):
        # Sample images from Unsplash (free to use)
        image_mappings = {
            # Technology posts
            'artificial-intelligence': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=400&fit=crop',
            'web-development': 'https://images.unsplash.com/photo-1627398242454-45a1465c2479?w=800&h=400&fit=crop',
            'programming': 'https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=800&h=400&fit=crop',
            'cybersecurity': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800&h=400&fit=crop',
            'machine-learning': 'https://images.unsplash.com/photo-1555255707-c07966088b7b?w=800&h=400&fit=crop',
            'react': 'https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=800&h=400&fit=crop',
            'docker': 'https://images.unsplash.com/photo-1605745341112-85968b19335b?w=800&h=400&fit=crop',
            
            # Travel posts
            'travel': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=800&h=400&fit=crop',
            'solo-travel': 'https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800&h=400&fit=crop',
            'southeast-asia': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=400&fit=crop',
            'adventure': 'https://images.unsplash.com/photo-1551632811-561732d1e306?w=800&h=400&fit=crop',
            'budget-travel': 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=800&h=400&fit=crop',
            'photography': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=800&h=400&fit=crop',
            'digital-nomad': 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&h=400&fit=crop',
            
            # Food posts
            'food': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800&h=400&fit=crop',
            'pasta': 'https://images.unsplash.com/photo-1621996346565-e3dbc353d2e5?w=800&h=400&fit=crop',
            'fermentation': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&h=400&fit=crop',
            'vegan': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800&h=400&fit=crop',
            'mediterranean': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=800&h=400&fit=crop',
            'sourdough': 'https://images.unsplash.com/photo-1509440159596-0249088772ff?w=800&h=400&fit=crop',
            'cooking': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=800&h=400&fit=crop',
            
            # Lifestyle posts
            'minimalism': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=800&h=400&fit=crop',
            'habits': 'https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=800&h=400&fit=crop',
            'meditation': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=400&fit=crop',
            'wellness': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&h=400&fit=crop',
            'productivity': 'https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=800&h=400&fit=crop',
            'organization': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&h=400&fit=crop',
            'sustainability': 'https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=800&h=400&fit=crop',
            
            # Business posts
            'remote-work': 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&h=400&fit=crop',
            'startup': 'https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=800&h=400&fit=crop',
            'business': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=400&fit=crop',
            'marketing': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=400&fit=crop',
            'cryptocurrency': 'https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=800&h=400&fit=crop',
            'project-management': 'https://images.unsplash.com/photo-1611224923853-80b023f02d71?w=800&h=400&fit=crop',
            'ecommerce': 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&h=400&fit=crop',
        }
        
        # Default fallback images by category
        category_defaults = {
            'Technology': 'https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=800&h=400&fit=crop',
            'Travel': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=800&h=400&fit=crop',
            'Food': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800&h=400&fit=crop',
            'Lifestyle': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=400&fit=crop',
            'Business': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=400&fit=crop',
        }
        
        posts = BlogPost.objects.filter(featured_image="")
        self.stdout.write(f'Found {posts.count()} posts without images')
        updated_count = 0
        
        for post in posts:
            try:
                # Find appropriate image URL
                image_url = None
                
                # First, try to match by tags
                for tag in post.tags.all():
                    if tag.name in image_mappings:
                        image_url = image_mappings[tag.name]
                        break
                
                # If no tag match, use category default
                if not image_url and post.category:
                    image_url = category_defaults.get(post.category.name)
                
                # Final fallback
                if not image_url:
                    image_url = 'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=800&h=400&fit=crop'
                
                # Download and save image
                response = requests.get(image_url, timeout=10)
                if response.status_code == 200:
                    # Create image from response
                    img = Image.open(BytesIO(response.content))
                    
                    # Convert to RGB if necessary
                    if img.mode in ('RGBA', 'P'):
                        img = img.convert('RGB')
                    
                    # Resize to consistent dimensions
                    img = img.resize((800, 400), Image.Resampling.LANCZOS)
                    
                    # Save to BytesIO
                    img_io = BytesIO()
                    img.save(img_io, format='JPEG', quality=85)
                    img_io.seek(0)
                    
                    # Create filename
                    filename = f"{post.slug[:50]}.jpg"
                    
                    # Save to model
                    post.featured_image.save(
                        filename,
                        ContentFile(img_io.getvalue()),
                        save=True
                    )
                    
                    updated_count += 1
                    self.stdout.write(f'Added image to: {post.title}')
                
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'Failed to add image to "{post.title}": {str(e)}')
                )
                continue
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully added images to {updated_count} blog posts!')
        )
