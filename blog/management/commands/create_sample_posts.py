from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import BlogPost, Category
from django.utils import timezone
from django.utils.text import slugify
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Create sample blog posts across various categories'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=50,
            help='Number of sample posts to create (default: 50)'
        )

    def handle(self, *args, **options):
        count = options['count']
        
        # Sample blog data organized by categories
        sample_posts = [
            # Technology Category
            {
                'title': 'The Future of Artificial Intelligence in 2024',
                'content': '''Artificial Intelligence continues to revolutionize industries across the globe. From machine learning algorithms that can predict market trends to natural language processing systems that understand human emotions, AI is becoming increasingly sophisticated.

In this comprehensive guide, we'll explore the latest developments in AI technology, including:

**Machine Learning Advances**
- Deep learning neural networks
- Reinforcement learning applications
- Computer vision breakthroughs

**Natural Language Processing**
- Large language models like GPT and BERT
- Real-time translation systems
- Conversational AI assistants

**AI in Business**
- Automated customer service
- Predictive analytics
- Process optimization

The implications of these technologies are far-reaching, affecting everything from healthcare diagnostics to autonomous vehicles. As we move forward, it's crucial to consider both the opportunities and challenges that AI presents.

**Ethical Considerations**
As AI becomes more powerful, we must address important ethical questions about privacy, bias, and the future of work. Companies and governments worldwide are developing frameworks to ensure AI is used responsibly.

The next decade will be pivotal in determining how AI shapes our society. By staying informed and engaged with these developments, we can help ensure that AI benefits everyone.''',
                'excerpt': 'Explore the latest developments in AI technology and their impact on business, society, and the future of work.',
                'tags': ['technology', 'artificial-intelligence', 'machine-learning', 'future'],
                'category': 'Technology'
            },
            {
                'title': 'Web Development Trends: React vs Vue vs Angular',
                'content': '''The JavaScript framework landscape continues to evolve rapidly. In 2024, three frameworks dominate the frontend development space: React, Vue, and Angular. Each has its strengths and ideal use cases.

**React: The Industry Standard**
React remains the most popular choice for many developers and companies. Its component-based architecture and vast ecosystem make it versatile for projects of all sizes.

Key advantages:
- Large community and job market
- Extensive third-party libraries
- Flexible and unopinionated
- Strong corporate backing from Meta

**Vue: The Progressive Framework**
Vue.js offers an excellent balance between simplicity and power. It's particularly popular among developers who want a gentle learning curve without sacrificing functionality.

Key advantages:
- Easy to learn and integrate
- Excellent documentation
- Great performance out of the box
- Growing ecosystem

**Angular: The Enterprise Solution**
Angular provides a complete framework solution with built-in tools for routing, forms, HTTP client, and more. It's particularly well-suited for large-scale enterprise applications.

Key advantages:
- Full-featured framework
- TypeScript by default
- Strong opinions and structure
- Excellent tooling

**Making the Right Choice**
The best framework depends on your specific needs:
- Choose React for maximum flexibility and job opportunities
- Choose Vue for rapid development and ease of use
- Choose Angular for large, complex enterprise applications

Regardless of your choice, focus on understanding JavaScript fundamentals, as they remain constant across all frameworks.''',
                'excerpt': 'A comprehensive comparison of the top JavaScript frameworks in 2024: React, Vue, and Angular.',
                'tags': ['web-development', 'javascript', 'react', 'vue', 'angular'],
                'category': 'Technology'
            },
            
            # Travel Category
            {
                'title': 'Hidden Gems of Southeast Asia: Off the Beaten Path',
                'content': '''Southeast Asia offers incredible diversity beyond the popular tourist destinations. While places like Bangkok, Bali, and Singapore are amazing, there are countless hidden gems waiting to be discovered.

**Philippines: Siquijor Island**
Known as the "Island of Fire," Siquijor offers pristine beaches, mystical folklore, and incredible diving spots. The island maintains its authentic charm with traditional healing practices and unspoiled natural beauty.

Must-visit spots:
- Cambugahay Falls - Multi-tiered waterfalls perfect for swimming
- Salagdoong Beach - Crystal clear waters and cliff jumping
- Lazi Church - Historic Spanish colonial architecture

**Vietnam: Ha Giang Province**
Located in northern Vietnam near the Chinese border, Ha Giang offers some of the most spectacular mountain scenery in Southeast Asia. The famous Ha Giang Loop is a motorcycle journey through ethnic minority villages and terraced rice fields.

Highlights:
- Dong Van Karst Plateau - UNESCO Global Geopark
- Ma Pi Leng Pass - Breathtaking mountain views
- Lung Cu Flag Tower - Northernmost point of Vietnam

**Indonesia: Flores Island**
Beyond Bali lies Flores, an island of volcanic landscapes, traditional villages, and the famous Komodo dragons. The island offers authentic Indonesian culture and stunning natural beauty.

Key attractions:
- Kelimutu National Park - Three colored crater lakes
- Traditional villages of Wae Rebo and Bena
- Pink Beach - One of only seven pink sand beaches in the world

**Laos: Nong Khiaw**
This small town along the Nam Ou River offers incredible limestone karst scenery and peaceful riverside living. It's perfect for travelers seeking tranquility and natural beauty.

Activities:
- Hiking to Pha Tok Cave viewpoint
- Kayaking on the Nam Ou River
- Visiting traditional Lao villages

**Travel Tips for Hidden Gems:**
- Learn basic local phrases
- Respect local customs and traditions
- Travel slowly to truly appreciate each destination
- Support local businesses and communities
- Be prepared for basic accommodations

These destinations offer authentic experiences away from crowds, allowing you to connect with local cultures and pristine natural environments.''',
                'excerpt': 'Discover the most beautiful hidden destinations in Southeast Asia, from mystical islands to mountain villages.',
                'tags': ['travel', 'southeast-asia', 'hidden-gems', 'adventure', 'culture'],
                'category': 'Travel'
            },
            
            # Food Category
            {
                'title': 'The Art of Italian Pasta: From Dough to Perfection',
                'content': '''Italian pasta is more than just food—it's a cultural heritage that has been perfected over centuries. Understanding the fundamentals of pasta making can transform your cooking and deepen your appreciation for Italian cuisine.

**The Foundation: Pasta Dough**
Traditional Italian pasta uses just two ingredients: semolina flour and eggs (for egg pasta) or water (for dried pasta). The quality of these simple ingredients makes all the difference.

Types of flour:
- Semolina (semola di grano duro) - The gold standard for pasta
- 00 flour - Finely milled, perfect for delicate pasta
- All-purpose flour - Acceptable substitute for home cooking

**Regional Pasta Varieties**
Italy's 20 regions each have their signature pasta shapes and preparations:

**Northern Italy:**
- Tagliatelle from Emilia-Romagna - Perfect with rich ragù
- Pici from Tuscany - Hand-rolled thick spaghetti
- Pizzoccheri from Lombardy - Buckwheat pasta with cabbage and cheese

**Central Italy:**
- Cacio e Pepe from Lazio - Simple perfection with cheese and pepper
- Pappardelle from Tuscany - Wide ribbons ideal for game sauces
- Spaghetti all'Amatriciana - Classic Roman dish with guanciale and tomatoes

**Southern Italy:**
- Orecchiette from Puglia - "Little ears" perfect for vegetables
- Pasta alla Norma from Sicily - Eggplant, tomatoes, and ricotta salata
- Spaghetti alle Vongole from Campania - Clams, garlic, and white wine

**The Perfect Cooking Technique**
Achieving al dente pasta requires attention to detail:

1. Use plenty of salted water (1 liter per 100g pasta)
2. Add pasta when water reaches a rolling boil
3. Stir immediately and occasionally
4. Taste test 1-2 minutes before package time
5. Reserve pasta water before draining
6. Finish cooking in the sauce

**Sauce Pairing Principles**
- Thin sauces pair with long, thin pasta (spaghetti, linguine)
- Chunky sauces work best with short, textured pasta (rigatoni, penne)
- Delicate sauces complement fresh, thin pasta (angel hair, fresh tagliatelle)
- Rich, heavy sauces need sturdy pasta (pappardelle, rigatoni)

**Essential Italian Pasta Recipes to Master:**
1. Aglio e Olio - Garlic, olive oil, and chili
2. Carbonara - Eggs, cheese, guanciale, and black pepper
3. Pomodoro - Simple tomato sauce with basil
4. Pesto Genovese - Basil, pine nuts, garlic, and Parmigiano

Remember, great pasta is about respecting tradition while using the best ingredients you can find. Start with these fundamentals, and you'll be creating authentic Italian pasta dishes that would make nonna proud.''',
                'excerpt': 'Master the art of Italian pasta making with traditional techniques, regional varieties, and perfect sauce pairings.',
                'tags': ['food', 'italian-cuisine', 'pasta', 'cooking', 'recipes'],
                'category': 'Food'
            },
            
            # Lifestyle Category
            {
                'title': 'Minimalism in 2024: Living More with Less',
                'content': '''Minimalism has evolved from a design trend to a lifestyle philosophy that helps people focus on what truly matters. In our increasingly complex world, the principles of minimalism offer a path to greater clarity, purpose, and satisfaction.

**What Minimalism Really Means**
Minimalism isn't about living with as few possessions as possible—it's about being intentional with what you choose to keep in your life. It's about removing the excess to make room for what adds value and joy.

Core principles:
- Intentionality in all decisions
- Quality over quantity
- Experiences over possessions
- Mindful consumption
- Focus on relationships and personal growth

**The Benefits of Minimalist Living**

**Mental Clarity**
Reducing physical clutter often leads to mental clarity. When your environment is simplified, your mind can focus on more important matters rather than being overwhelmed by visual noise.

**Financial Freedom**
Minimalism naturally leads to more mindful spending. By questioning each purchase and focusing on needs rather than wants, many people find they save significant money.

**Environmental Impact**
Consuming less means producing less waste and having a smaller environmental footprint. Minimalists often choose quality items that last longer, reducing the cycle of constant replacement.

**Time Savings**
Fewer possessions mean less time spent cleaning, organizing, and maintaining. This freed-up time can be invested in relationships, hobbies, and personal development.

**Practical Steps to Embrace Minimalism**

**Start Small**
Begin with one area of your life:
- Declutter your wardrobe using the "one year rule"
- Simplify your digital life by unsubscribing from unnecessary emails
- Reduce your commitments to focus on what matters most

**The 30-Day Minimalism Game**
On day 1, remove 1 item. On day 2, remove 2 items. Continue until day 30. By the end, you'll have removed 465 items from your life.

**Digital Minimalism**
- Uninstall apps you don't use regularly
- Unsubscribe from email lists that don't add value
- Limit social media consumption
- Create phone-free zones in your home

**Mindful Consumption**
Before making any purchase, ask:
- Do I really need this?
- Will this add value to my life?
- Do I have something that serves the same purpose?
- Am I buying this for the right reasons?

**Common Minimalism Myths Debunked**

**Myth 1: Minimalists live in empty, sterile spaces**
Reality: Minimalist spaces are thoughtfully curated, not empty. They contain items that serve a purpose or bring joy.

**Myth 2: You have to get rid of everything**
Reality: Minimalism is personal. Keep what adds value to your life, regardless of quantity.

**Myth 3: Minimalism is only for wealthy people**
Reality: Minimalism can actually save money and is accessible to people of all income levels.

**Minimalism and Relationships**
Minimalism extends beyond possessions to relationships and commitments. Focus on:
- Deep, meaningful relationships over numerous acquaintances
- Quality time over busy schedules
- Authentic connections over social media followers

**Creating Your Minimalist Journey**
Remember that minimalism is a journey, not a destination. Start where you are, use what you have, and do what you can. The goal isn't perfection—it's progress toward a more intentional life.

Your version of minimalism might look different from others, and that's perfectly fine. The key is finding what works for your life, values, and circumstances.''',
                'excerpt': 'Discover how minimalism can bring clarity, freedom, and purpose to your life in 2024 with practical tips and strategies.',
                'tags': ['lifestyle', 'minimalism', 'mindfulness', 'personal-development', 'wellness'],
                'category': 'Lifestyle'
            },
            
            # Business Category
            {
                'title': 'Remote Work Revolution: Building High-Performance Distributed Teams',
                'content': '''The remote work revolution has fundamentally changed how we think about productivity, collaboration, and work-life balance. As organizations worldwide embrace distributed teams, new strategies and tools are emerging to maximize the potential of remote work.

**The New Remote Work Landscape**
Remote work is no longer a temporary pandemic response—it's become a permanent fixture in the modern workplace. Companies that master remote work practices gain access to global talent, reduced overhead costs, and often see increased employee satisfaction and productivity.

**Key Statistics:**
- 42% of the U.S. workforce now works remotely full-time
- Remote workers report 22% higher happiness levels
- Companies save an average of $11,000 per remote employee annually
- 74% of workers say remote work opportunities would make them less likely to leave

**Building High-Performance Remote Teams**

**1. Establish Clear Communication Protocols**
Effective communication is the backbone of successful remote teams. Establish clear guidelines for:

- **Synchronous vs. Asynchronous Communication**
  - Use real-time communication for urgent matters and brainstorming
  - Leverage asynchronous tools for updates, documentation, and non-urgent discussions

- **Communication Channels**
  - Slack/Teams for quick questions and team chat
  - Email for formal communications and external contacts
  - Video calls for meetings and face-to-face discussions
  - Project management tools for task-related communication

**2. Implement Robust Project Management Systems**
Remote teams need clear visibility into project progress and individual responsibilities.

Essential tools and practices:
- **Project Management Platforms**: Asana, Trello, Monday.com, or Jira
- **Documentation**: Confluence, Notion, or Google Workspace
- **Time Tracking**: Toggl, RescueTime, or Clockify
- **File Sharing**: Google Drive, Dropbox, or SharePoint

**3. Foster Team Culture and Connection**
Building relationships remotely requires intentional effort:

- **Virtual Coffee Chats**: Schedule informal 15-minute video calls
- **Online Team Building**: Virtual escape rooms, online games, or cooking classes
- **Regular Check-ins**: Weekly one-on-ones and team retrospectives
- **Celebration Rituals**: Acknowledge achievements and milestones

**4. Optimize for Different Time Zones**
Global teams require thoughtful scheduling and communication strategies:

- **Core Overlap Hours**: Identify 2-4 hours when most team members are available
- **Rotating Meeting Times**: Share the burden of inconvenient meeting times
- **Asynchronous Updates**: Use recorded videos or written summaries for important information
- **Documentation First**: Ensure all decisions and discussions are documented

**Remote Work Best Practices for Individuals**

**Creating an Effective Home Office**
- **Dedicated Workspace**: Separate work area from living space
- **Ergonomic Setup**: Proper chair, desk height, and monitor positioning
- **Good Lighting**: Natural light when possible, supplemented with task lighting
- **Minimal Distractions**: Quiet environment with necessary tools within reach

**Maintaining Work-Life Balance**
- **Set Clear Boundaries**: Define start and end times for work
- **Take Regular Breaks**: Use the Pomodoro Technique or similar methods
- **Physical Activity**: Incorporate movement throughout the day
- **Social Connection**: Maintain relationships outside of work

**Productivity Strategies**
- **Time Blocking**: Schedule specific times for different types of work
- **Batch Similar Tasks**: Group similar activities together
- **Eliminate Distractions**: Use website blockers and phone settings
- **Regular Reviews**: Weekly planning and daily prioritization

**Technology Stack for Remote Teams**

**Communication Tools:**
- Slack or Microsoft Teams for instant messaging
- Zoom or Google Meet for video conferencing
- Loom for asynchronous video messages

**Collaboration Tools:**
- Figma for design collaboration
- GitHub for code collaboration
- Google Workspace or Microsoft 365 for document collaboration

**Productivity Tools:**
- Notion or Obsidian for knowledge management
- Calendly for scheduling
- LastPass or 1Password for security

**Measuring Remote Team Success**
Track both quantitative and qualitative metrics:

**Quantitative Metrics:**
- Project completion rates
- Response times to communications
- Meeting attendance and participation
- Goal achievement rates

**Qualitative Metrics:**
- Employee satisfaction surveys
- Team cohesion assessments
- Communication effectiveness
- Innovation and creativity levels

**The Future of Remote Work**
As remote work continues to evolve, we're seeing trends toward:
- Hybrid work models combining remote and in-office time
- Virtual reality meetings and collaboration spaces
- AI-powered productivity and wellness tools
- Increased focus on mental health and well-being

Organizations that invest in remote work capabilities now will have a significant competitive advantage in attracting and retaining top talent while building resilient, adaptable teams for the future.''',
                'excerpt': 'Learn how to build and manage high-performance remote teams with proven strategies, tools, and best practices.',
                'tags': ['business', 'remote-work', 'team-management', 'productivity', 'leadership'],
                'category': 'Business'
            }
        ]
        
        # Get or create a default user for the posts
        try:
            author = User.objects.get(username='admin')
        except User.DoesNotExist:
            author = User.objects.create_user(
                username='admin',
                email='admin@bloghub.com',
                password='admin123',
                first_name='Blog',
                last_name='Admin'
            )
            self.stdout.write(
                self.style.SUCCESS(f'Created admin user: {author.username}')
            )

        created_count = 0
        
        # Create sample posts
        for i in range(min(count, len(sample_posts))):
            post_data = sample_posts[i % len(sample_posts)]

            # Check if post already exists
            if BlogPost.objects.filter(title=post_data['title']).exists():
                continue

            # Create or get category
            category, _ = Category.objects.get_or_create(
                name=post_data['category'],
                defaults={'slug': slugify(post_data['category'])}
            )

            # Create the post
            post = BlogPost.objects.create(
                title=post_data['title'],
                slug=slugify(post_data['title']),
                content=post_data['content'],
                excerpt=post_data['excerpt'],
                author=author,
                category=category,
                status='published',
                published_at=timezone.now() - timedelta(days=random.randint(1, 30))
            )

            # Add tags using django-taggit
            post.tags.add(*post_data['tags'])

            created_count += 1
            self.stdout.write(f'Created post: {post.title}')
        
        # If we need more posts, create variations
        if count > len(sample_posts):
            additional_posts = [
                {
                    'title': 'Machine Learning for Beginners: A Complete Guide',
                    'content': 'Machine learning is transforming industries...',
                    'excerpt': 'Start your machine learning journey with this comprehensive beginner guide.',
                    'tags': ['technology', 'machine-learning', 'programming', 'data-science'],
                    'category': 'Technology'
                },
                {
                    'title': 'Sustainable Travel: How to Explore Responsibly',
                    'content': 'Sustainable travel practices are becoming increasingly important...',
                    'excerpt': 'Learn how to travel responsibly while minimizing your environmental impact.',
                    'tags': ['travel', 'sustainability', 'environment', 'responsible-tourism'],
                    'category': 'Travel'
                },
                {
                    'title': 'Plant-Based Nutrition: Complete Protein Sources',
                    'content': 'Plant-based diets can provide all essential nutrients...',
                    'excerpt': 'Discover complete protein sources for a healthy plant-based diet.',
                    'tags': ['food', 'nutrition', 'plant-based', 'health', 'vegan'],
                    'category': 'Food'
                },
                {
                    'title': 'Digital Detox: Reclaiming Your Time and Attention',
                    'content': 'In our hyperconnected world, taking breaks from technology...',
                    'excerpt': 'Learn how to implement a digital detox for better mental health and productivity.',
                    'tags': ['lifestyle', 'digital-detox', 'wellness', 'mindfulness', 'productivity'],
                    'category': 'Lifestyle'
                },
                {
                    'title': 'Startup Funding: From Idea to Investment',
                    'content': 'Securing funding for your startup requires preparation...',
                    'excerpt': 'Navigate the startup funding landscape with this comprehensive guide.',
                    'tags': ['business', 'startup', 'funding', 'entrepreneurship', 'investment'],
                    'category': 'Business'
                }
            ]
            
            remaining = count - len(sample_posts)
            for i in range(remaining):
                post_data = additional_posts[i % len(additional_posts)]

                # Create variations by adding numbers to titles
                variation_title = f"{post_data['title']} - Part {(i // len(additional_posts)) + 1}"

                if BlogPost.objects.filter(title=variation_title).exists():
                    continue

                # Create or get category
                category, _ = Category.objects.get_or_create(
                    name=post_data['category'],
                    defaults={'slug': slugify(post_data['category'])}
                )

                post = BlogPost.objects.create(
                    title=variation_title,
                    slug=slugify(variation_title),
                    content=post_data['content'],
                    excerpt=post_data['excerpt'],
                    author=author,
                    category=category,
                    status='published',
                    published_at=timezone.now() - timedelta(days=random.randint(1, 60))
                )

                # Add tags using django-taggit
                post.tags.add(*post_data['tags'])

                created_count += 1
                self.stdout.write(f'Created post: {post.title}')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} sample blog posts!')
        )

        # Display available categories and tags
        categories = Category.objects.all()
        self.stdout.write(f'\nAvailable categories: {", ".join([cat.name for cat in categories])}')

        # Get all tags from taggit
        from taggit.models import Tag
        tags = Tag.objects.all()
        self.stdout.write(f'Available tags: {", ".join([tag.name for tag in tags])}')
