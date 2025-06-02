from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
import requests
from io import BytesIO
from PIL import Image

class Command(BaseCommand):
    help = 'Add sample avatars to user profiles'

    def handle(self, *args, **options):
        # Sample avatar URLs from UI Avatars (generates avatars based on initials)
        users = User.objects.all()
        updated_count = 0
        
        for user in users:
            try:
                # Skip if user already has an avatar
                if user.profile.avatar:
                    continue
                
                # Generate avatar URL based on user's initials
                initials = f"{user.first_name[:1]}{user.last_name[:1]}" if user.first_name and user.last_name else user.username[:2]
                avatar_url = f"https://ui-avatars.com/api/?name={initials}&size=300&background=e91e63&color=ffffff&bold=true"
                
                # Download avatar
                response = requests.get(avatar_url, timeout=10)
                if response.status_code == 200:
                    # Create image from response
                    img = Image.open(BytesIO(response.content))
                    
                    # Convert to RGB if necessary
                    if img.mode in ('RGBA', 'P'):
                        img = img.convert('RGB')
                    
                    # Resize to 300x300
                    img = img.resize((300, 300), Image.Resampling.LANCZOS)
                    
                    # Save to BytesIO
                    img_io = BytesIO()
                    img.save(img_io, format='JPEG', quality=90)
                    img_io.seek(0)
                    
                    # Create filename
                    filename = f"{user.username}_avatar.jpg"
                    
                    # Save to profile
                    user.profile.avatar.save(
                        filename,
                        ContentFile(img_io.getvalue()),
                        save=True
                    )
                    
                    updated_count += 1
                    self.stdout.write(f'Added avatar to: {user.username}')
                
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'Failed to add avatar to "{user.username}": {str(e)}')
                )
                continue
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully added avatars to {updated_count} users!')
        )
