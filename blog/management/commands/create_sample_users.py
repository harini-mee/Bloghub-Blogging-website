from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile

class Command(BaseCommand):
    help = 'Create sample users for the blog'

    def handle(self, *args, **options):
        sample_users = [
            {
                'username': 'sarah_tech',
                'email': 'sarah@example.com',
                'first_name': 'Sarah',
                'last_name': 'Johnson',
                'bio': 'Tech enthusiast and AI researcher. Passionate about machine learning and web development.'
            },
            {
                'username': 'mike_traveler',
                'email': 'mike@example.com',
                'first_name': 'Mike',
                'last_name': 'Chen',
                'bio': 'Digital nomad and travel blogger. Exploring hidden gems around the world.'
            },
            {
                'username': 'emma_chef',
                'email': 'emma@example.com',
                'first_name': 'Emma',
                'last_name': 'Rodriguez',
                'bio': 'Professional chef and food writer. Sharing authentic recipes and culinary traditions.'
            },
            {
                'username': 'alex_lifestyle',
                'email': 'alex@example.com',
                'first_name': 'Alex',
                'last_name': 'Thompson',
                'bio': 'Minimalist lifestyle coach and wellness advocate. Helping people live intentionally.'
            },
            {
                'username': 'david_business',
                'email': 'david@example.com',
                'first_name': 'David',
                'last_name': 'Kim',
                'bio': 'Startup founder and business strategist. Expert in remote work and team management.'
            }
        ]
        
        created_count = 0
        
        for user_data in sample_users:
            # Check if user already exists
            if User.objects.filter(username=user_data['username']).exists():
                self.stdout.write(f'User {user_data["username"]} already exists, skipping...')
                continue
            
            # Create user
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password='samplepass123',
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            
            # Update or create profile
            profile, created = Profile.objects.get_or_create(user=user)
            profile.bio = user_data['bio']
            profile.save()
            
            created_count += 1
            self.stdout.write(f'Created user: {user.username}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} sample users!')
        )
        
        if created_count > 0:
            self.stdout.write(
                self.style.WARNING('Default password for all sample users: samplepass123')
            )
