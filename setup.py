#!/usr/bin/env python3
"""
BlogHub Setup Script
This script helps set up the BlogHub Django project with MongoDB.
"""

import os
import sys
import subprocess
import secrets
import shutil

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"✗ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return None

def create_env_file():
    """Create .env file from .env.example."""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            shutil.copy('.env.example', '.env')
            
            # Generate a random secret key
            secret_key = secrets.token_urlsafe(50)
            
            # Read and update .env file
            with open('.env', 'r') as file:
                content = file.read()
            
            content = content.replace('your-secret-key-here', secret_key)
            
            with open('.env', 'w') as file:
                file.write(content)
            
            print("✓ Created .env file with generated secret key")
        else:
            print("✗ .env.example file not found")
    else:
        print("✓ .env file already exists")

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("✗ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def check_mongodb():
    """Check if MongoDB is running."""
    try:
        import pymongo
        client = pymongo.MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=2000)
        client.server_info()
        print("✓ MongoDB is running and accessible")
        return True
    except Exception as e:
        print(f"✗ MongoDB connection failed: {e}")
        print("Please make sure MongoDB is installed and running on localhost:27017")
        return False

def install_dependencies():
    """Install Python dependencies."""
    if run_command("pip install -r requirements.txt", "Installing dependencies"):
        return True
    return False

def setup_django():
    """Set up Django project."""
    commands = [
        ("python manage.py makemigrations", "Creating migrations"),
        ("python manage.py migrate", "Running migrations"),
        ("python manage.py collectstatic --noinput", "Collecting static files"),
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    return True

def create_superuser():
    """Create Django superuser."""
    print("\n" + "="*50)
    print("CREATE SUPERUSER")
    print("="*50)
    print("Please create an admin user for your BlogHub installation:")
    
    try:
        subprocess.run(["python", "manage.py", "createsuperuser"], check=True)
        print("✓ Superuser created successfully")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to create superuser")
        return False
    except KeyboardInterrupt:
        print("\n✗ Superuser creation cancelled")
        return False

def create_media_directories():
    """Create necessary media directories."""
    directories = [
        'media',
        'media/profile_pics',
        'media/blog_images',
        'static',
        'staticfiles'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    print("✓ Created media and static directories")

def main():
    """Main setup function."""
    print("="*60)
    print("BLOGHUB SETUP")
    print("="*60)
    print("Setting up your Django blogging platform with MongoDB...")
    
    # Check Python version
    check_python_version()
    
    # Create .env file
    create_env_file()
    
    # Create directories
    create_media_directories()
    
    # Check MongoDB
    if not check_mongodb():
        print("\nPlease install and start MongoDB before continuing.")
        print("Visit: https://docs.mongodb.com/manual/installation/")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("Failed to install dependencies. Please check your internet connection and try again.")
        sys.exit(1)
    
    # Setup Django
    if not setup_django():
        print("Failed to set up Django. Please check the error messages above.")
        sys.exit(1)
    
    # Create superuser
    create_superuser()
    
    print("\n" + "="*60)
    print("SETUP COMPLETE!")
    print("="*60)
    print("Your BlogHub installation is ready!")
    print("\nTo start the development server, run:")
    print("  python manage.py runserver")
    print("\nThen visit: http://127.0.0.1:8000")
    print("\nAdmin panel: http://127.0.0.1:8000/admin")
    print("\nHappy blogging! 🎉")

if __name__ == "__main__":
    main()
