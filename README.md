# 🌟 BlogHub - Interactive Blog Platform

A modern, feature-rich blogging platform built with Django, featuring an interactive landing page, user authentication, and comprehensive blog management capabilities with a beautiful pink, teal, and cream color scheme.

## Features

### 🚀 Core Features
- **User Management**: Registration, authentication, and user profiles
- **Blog System**: Create, edit, delete posts with rich text content
- **Media Support**: Upload and manage images for blog posts
- **Tagging System**: Organize posts with tags for easy categorization
- **Draft/Publish System**: Save posts as drafts or publish immediately
- **Comments & Interactions**: Comment on posts, like posts, and reply to comments
- **Social Sharing**: Share posts on Twitter, Facebook, and LinkedIn

### 👨‍💼 Admin Features
- **Content Moderation**: Admin panel for managing posts and comments
- **User Management**: Manage user accounts and profiles
- **Analytics**: View post statistics and engagement metrics

### 🎨 Frontend Features
- **Responsive Design**: Mobile-friendly Bootstrap 5 interface
- **Interactive UI**: Dynamic JavaScript interactions
- **Search Functionality**: Search posts by title, content, and tags
- **Pagination**: Efficient content browsing
- **Real-time Features**: Like buttons, comment replies

## Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Font Awesome, Custom CSS
- **Image Processing**: Pillow
- **Tags**: django-taggit

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd bloghub
   ```

2. **Run the setup script**
   ```bash
   python setup.py
   ```
   
   This script will:
   - Check Python and MongoDB compatibility
   - Install dependencies
   - Create environment configuration
   - Set up the database
   - Create necessary directories
   - Guide you through creating an admin user

3. **Start the development server**
   ```bash
   python manage.py runserver
   ```

4. **Access the application**
   - Main site: http://127.0.0.1:8000
   - Admin panel: http://127.0.0.1:8000/admin

### Manual Setup

If you prefer manual setup:

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. **Set up database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=bloghub
DB_HOST=mongodb://localhost:27017
```

### MongoDB Setup

1. **Install MongoDB**
   - Windows: Download from [MongoDB website](https://www.mongodb.com/try/download/community)
   - macOS: `brew install mongodb-community`
   - Ubuntu: `sudo apt install mongodb`

2. **Start MongoDB service**
   ```bash
   # Windows
   net start MongoDB
   
   # macOS/Linux
   sudo systemctl start mongod
   ```

## Usage

### For Users

1. **Register an account** at `/accounts/register/`
2. **Complete your profile** with bio, avatar, and social links
3. **Create your first post** using the "Write" button
4. **Engage with content** by liking and commenting on posts
5. **Discover content** using search and tags

### For Administrators

1. **Access admin panel** at `/admin/`
2. **Manage users** and their profiles
3. **Moderate content** by reviewing posts and comments
4. **Monitor activity** through the dashboard
5. **Configure site settings** as needed

## Project Structure

```
bloghub/
├── bloghub/                 # Main project settings
├── accounts/                # User management app
├── blog/                    # Blog functionality app
├── templates/               # HTML templates
├── static/                  # CSS, JavaScript, images
├── media/                   # User uploaded files
├── requirements.txt         # Python dependencies
├── manage.py               # Django management script
└── setup.py                # Automated setup script
```

## Key Features Explained

### User Profiles
- Customizable avatars and bio
- Social media links integration
- Activity timeline
- Post statistics

### Blog Posts
- Rich text content with image support
- Tag-based categorization
- Draft/publish workflow
- View tracking and analytics
- Social sharing integration

### Interaction System
- Like/unlike posts
- Threaded comments with replies
- Real-time updates via AJAX
- User engagement metrics

### Search & Discovery
- Full-text search across posts
- Tag-based filtering
- Author-based browsing
- Related posts suggestions

## Development

### Adding New Features

1. **Create new Django apps** for major features
2. **Follow the existing patterns** for models, views, and templates
3. **Use Bootstrap classes** for consistent styling
4. **Add JavaScript interactions** in `static/js/main.js`
5. **Update admin interface** for new models

### Customization

- **Styling**: Modify `static/css/style.css`
- **Templates**: Update HTML templates in `templates/`
- **Functionality**: Extend views and models in respective apps
- **Configuration**: Adjust settings in `bloghub/settings.py`

## Deployment

### Production Considerations

1. **Security Settings**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com']
   SECURE_SSL_REDIRECT = True
   ```

2. **Database Configuration**
   - Use MongoDB Atlas for cloud hosting
   - Configure connection strings properly

3. **Static Files**
   ```bash
   python manage.py collectstatic
   ```

4. **Web Server**
   - Use Gunicorn + Nginx for production
   - Configure proper media file serving

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review existing issues for solutions

## Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive CSS framework
- MongoDB for the flexible database solution
- Font Awesome for the beautiful icons

---

**Happy Blogging! 🎉**
