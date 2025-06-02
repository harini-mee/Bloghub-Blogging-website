#!/usr/bin/env python3
"""
BlogHub Development Server Runner
Quick script to start the Django development server
"""

import os
import sys
import subprocess

def check_setup():
    """Check if the project is properly set up."""
    required_files = [
        'manage.py',
        'requirements.txt',
        'bloghub/settings.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nPlease run setup.py first!")
        return False
    
    return True

def check_dependencies():
    """Check if dependencies are installed."""
    try:
        import django
        import djongo
        import pymongo
        print("✅ Dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def start_server():
    """Start the Django development server."""
    print("\n🚀 Starting BlogHub development server...")
    print("📍 Server will be available at: http://127.0.0.1:8000")
    print("🛑 Press Ctrl+C to stop the server\n")
    
    try:
        subprocess.run([sys.executable, 'manage.py', 'runserver'], check=True)
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Thanks for using BlogHub!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error starting server: {e}")
        print("Please check your configuration and try again.")

def main():
    """Main function."""
    print("="*50)
    print("🌟 BLOGHUB DEVELOPMENT SERVER")
    print("="*50)
    
    if not check_setup():
        sys.exit(1)
    
    if not check_dependencies():
        sys.exit(1)
    
    start_server()

if __name__ == "__main__":
    main()
