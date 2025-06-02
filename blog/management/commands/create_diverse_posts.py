from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import BlogPost, Category
from django.utils import timezone
from django.utils.text import slugify
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Create diverse blog posts with different authors'

    def handle(self, *args, **options):
        # Get all users
        users = list(User.objects.all())
        if len(users) < 2:
            self.stdout.write(
                self.style.ERROR('Please create sample users first using: python manage.py create_sample_users')
            )
            return
        
        diverse_posts = [
            # Technology posts
            {
                'title': 'Python vs JavaScript: Which Language to Learn First?',
                'content': '''Choosing your first programming language is a crucial decision that can shape your development journey. Two of the most popular options for beginners are Python and JavaScript, each with distinct advantages and use cases.

**Python: The Beginner-Friendly Giant**
Python's philosophy of "readability counts" makes it an excellent choice for newcomers to programming. Its clean, English-like syntax allows beginners to focus on learning programming concepts rather than wrestling with complex syntax.

Key advantages of Python:
- Simple, readable syntax
- Extensive standard library
- Strong community support
- Versatile applications (web development, data science, AI, automation)
- Excellent learning resources

Popular Python frameworks and libraries:
- Django and Flask for web development
- NumPy and Pandas for data analysis
- TensorFlow and PyTorch for machine learning
- Selenium for automation

**JavaScript: The Language of the Web**
JavaScript is the only programming language that runs natively in web browsers, making it essential for front-end web development. With Node.js, it's also become a powerful backend language.

Key advantages of JavaScript:
- Immediate visual feedback in browsers
- No setup required - runs in any browser
- Huge job market demand
- Full-stack development capability
- Rich ecosystem of frameworks and libraries

Popular JavaScript frameworks and libraries:
- React, Vue, and Angular for frontend
- Node.js and Express for backend
- React Native for mobile development
- Electron for desktop applications

**Making the Right Choice**
Consider your goals:
- Choose Python if you're interested in data science, AI, or want an easier learning curve
- Choose JavaScript if you want to build websites, web applications, or see immediate visual results

Both languages offer excellent career opportunities and have strong communities. The most important thing is to start coding and build projects, regardless of which language you choose.''',
                'excerpt': 'Compare Python and JavaScript to decide which programming language is best for beginners to learn first.',
                'tags': ['programming', 'python', 'javascript', 'beginners', 'web-development'],
                'category': 'Technology',
                'author_username': 'sarah_tech'
            },
            {
                'title': 'Cybersecurity Essentials: Protecting Your Digital Life',
                'content': '''In our increasingly connected world, cybersecurity has become as important as locking your front door. Understanding basic security principles can protect you from the majority of cyber threats.

**Common Cyber Threats**
Understanding what you're protecting against is the first step in cybersecurity:

1. **Phishing Attacks**: Fraudulent emails or websites designed to steal credentials
2. **Malware**: Malicious software including viruses, ransomware, and spyware
3. **Social Engineering**: Psychological manipulation to gain unauthorized access
4. **Data Breaches**: Unauthorized access to personal or corporate data
5. **Identity Theft**: Using stolen personal information for fraudulent purposes

**Essential Security Practices**

**Strong Password Management**
- Use unique passwords for each account
- Enable two-factor authentication (2FA) wherever possible
- Consider using a password manager like Bitwarden or 1Password
- Create passwords with at least 12 characters including mixed case, numbers, and symbols

**Safe Browsing Habits**
- Verify website URLs before entering sensitive information
- Look for HTTPS (the lock icon) on websites handling personal data
- Be cautious with public Wi-Fi networks
- Keep browsers and plugins updated

**Email Security**
- Be skeptical of unexpected emails, even from known contacts
- Don't click suspicious links or download unexpected attachments
- Verify requests for sensitive information through alternative channels
- Use email filtering and anti-spam tools

**Device Security**
- Keep operating systems and software updated
- Use reputable antivirus software
- Enable automatic screen locks on mobile devices
- Regularly backup important data

**Social Media Privacy**
- Review and adjust privacy settings regularly
- Be cautious about sharing personal information
- Think before posting location data or travel plans
- Be selective about friend/connection requests

**Financial Protection**
- Monitor bank and credit card statements regularly
- Set up account alerts for transactions
- Use secure payment methods for online purchases
- Freeze credit reports if not actively applying for credit

**For Businesses**
- Implement employee cybersecurity training
- Use enterprise-grade security solutions
- Develop incident response plans
- Regular security audits and penetration testing

**Staying Informed**
Cybersecurity is an evolving field. Stay updated through:
- Security blogs and news sources
- Official security advisories from software vendors
- Cybersecurity awareness training
- Professional security communities

Remember, cybersecurity is not about achieving perfect security—it's about making yourself a harder target than the next person. Most cybercriminals look for easy targets, so implementing basic security measures significantly reduces your risk.''',
                'excerpt': 'Learn essential cybersecurity practices to protect your personal and professional digital life from common threats.',
                'tags': ['cybersecurity', 'privacy', 'digital-safety', 'technology', 'security'],
                'category': 'Technology',
                'author_username': 'sarah_tech'
            },
            
            # Travel posts
            {
                'title': 'Solo Travel Safety: A Complete Guide for First-Time Solo Travelers',
                'content': '''Solo travel can be one of the most rewarding experiences of your life, offering freedom, self-discovery, and incredible adventures. However, traveling alone requires extra preparation and awareness to ensure your safety and enjoyment.

**Pre-Trip Planning**

**Research Your Destination**
- Study local customs, laws, and cultural norms
- Research common scams targeting tourists
- Identify safe neighborhoods and areas to avoid
- Learn basic phrases in the local language
- Understand local transportation options

**Share Your Itinerary**
- Provide detailed travel plans to trusted friends or family
- Use apps like TripIt to share real-time location updates
- Check in regularly with your emergency contacts
- Register with your embassy if traveling internationally

**Documentation and Backup**
- Make copies of important documents (passport, ID, insurance)
- Store digital copies in cloud storage
- Carry emergency cash in multiple currencies
- Have backup payment methods (multiple cards)

**Safety During Travel**

**Accommodation Safety**
- Choose reputable accommodations with good reviews
- Request rooms on higher floors (2nd-7th) for security
- Always lock doors and use additional security devices
- Trust your instincts about places and people

**Transportation Safety**
- Use official transportation services
- Avoid traveling alone at night when possible
- Keep valuables secure and out of sight
- Have backup transportation plans

**Daily Safety Practices**
- Dress appropriately for local customs
- Avoid displaying expensive items or large amounts of cash
- Stay aware of your surroundings
- Trust your instincts—if something feels wrong, leave

**Communication and Technology**
- Keep your phone charged with portable batteries
- Download offline maps and translation apps
- Use VPN for secure internet connections
- Have emergency numbers saved in your phone

**Meeting People Safely**
- Use common sense when meeting new people
- Meet in public places initially
- Don't share detailed personal information immediately
- Trust your gut feelings about people

**Health and Wellness**
- Research health risks and required vaccinations
- Pack a comprehensive first aid kit
- Have travel insurance with medical coverage
- Know how to access medical care in your destination

**Emergency Preparedness**
- Know local emergency numbers
- Have embassy contact information
- Keep emergency cash hidden separately
- Have a plan for various emergency scenarios

**Solo Travel Tips for Different Destinations**

**Urban Destinations**
- Use ride-sharing apps for safe transportation
- Stay in well-lit, busy areas at night
- Be extra cautious with street food and water
- Use hotel concierge services for recommendations

**Rural/Remote Areas**
- Inform locals of your travel plans
- Carry extra supplies and emergency equipment
- Have satellite communication devices if needed
- Travel during daylight hours when possible

**International Travel**
- Understand visa requirements and restrictions
- Know your embassy's location and services
- Understand local laws and penalties
- Have international phone/data plans

**Building Confidence**
Solo travel confidence comes with experience:
- Start with shorter trips to build skills
- Choose destinations known for solo traveler safety
- Join solo travel communities for advice and support
- Take a self-defense class before traveling

**Red Flags to Watch For**
- People who seem overly interested in your travel plans
- Offers that seem too good to be true
- Pressure to make quick decisions
- Requests for personal information or documents

**Solo Travel Benefits**
Despite safety considerations, solo travel offers unique advantages:
- Complete freedom to choose your itinerary
- Opportunities for personal growth and self-discovery
- Easier connections with locals and other travelers
- Development of problem-solving and independence skills

Remember, millions of people travel solo safely every year. With proper preparation, awareness, and common sense, you can have amazing solo adventures while staying safe and secure.''',
                'excerpt': 'Essential safety tips and strategies for first-time solo travelers to explore the world confidently and securely.',
                'tags': ['solo-travel', 'travel-safety', 'travel-tips', 'adventure', 'independence'],
                'category': 'Travel',
                'author_username': 'mike_traveler'
            },
            
            # Food posts
            {
                'title': 'Fermentation at Home: Ancient Techniques for Modern Kitchens',
                'content': '''Fermentation is one of humanity's oldest food preservation techniques, and it's experiencing a renaissance in modern kitchens. From kombucha to kimchi, fermented foods offer incredible flavors, health benefits, and a connection to culinary traditions.

**Understanding Fermentation**
Fermentation is a metabolic process where microorganisms (bacteria, yeasts, or molds) convert organic compounds into acids, gases, or alcohol. This process not only preserves food but also creates unique flavors and increases nutritional value.

**Types of Fermentation**

**Lactic Acid Fermentation**
- Creates tangy, sour flavors
- Examples: sauerkraut, kimchi, yogurt, sourdough
- Beneficial bacteria: Lactobacillus species
- Produces probiotics that support gut health

**Alcoholic Fermentation**
- Converts sugars to alcohol and CO2
- Examples: wine, beer, kombucha, kefir
- Primary microorganisms: yeasts
- Can be further processed to create vinegars

**Acetic Acid Fermentation**
- Produces vinegars from alcoholic beverages
- Examples: apple cider vinegar, wine vinegar
- Beneficial bacteria: Acetobacter
- Creates acidic preservation environment

**Getting Started: Essential Equipment**
- Glass jars (Mason jars work perfectly)
- Non-metal lids or cheesecloth
- Kitchen scale for precise measurements
- pH strips (optional but helpful)
- Clean kitchen towels
- Fermentation weights (glass or ceramic)

**Beginner-Friendly Fermentation Projects**

**Sauerkraut (Easiest Start)**
Ingredients:
- 1 medium cabbage (about 2 lbs)
- 1 tablespoon sea salt (non-iodized)

Instructions:
1. Shred cabbage finely
2. Massage with salt until liquid appears (10-15 minutes)
3. Pack tightly into jar, ensuring liquid covers cabbage
4. Weigh down with fermentation weight
5. Cover with cloth and secure with rubber band
6. Ferment at room temperature for 3-4 weeks
7. Taste weekly and refrigerate when desired sourness is reached

**Water Kefir (Probiotic Drink)**
Ingredients:
- 1/4 cup water kefir grains
- 1/4 cup sugar
- 4 cups filtered water
- Optional: dried fruit, lemon slice

Instructions:
1. Dissolve sugar in water
2. Add kefir grains and optional flavorings
3. Cover with cloth and ferment 24-48 hours
4. Strain grains and bottle liquid
5. Second fermentation: 12-24 hours for carbonation
6. Refrigerate and enjoy

**Fermented Salsa**
Ingredients:
- 6 large tomatoes, diced
- 1 onion, diced
- 2-3 jalapeños, minced
- 3 cloves garlic, minced
- 1 tablespoon sea salt
- Juice of 1 lime

Instructions:
1. Mix all ingredients in bowl
2. Let sit 30 minutes for juices to develop
3. Pack into jar, ensuring liquid covers vegetables
4. Ferment 2-5 days at room temperature
5. Refrigerate when desired flavor is achieved

**Health Benefits of Fermented Foods**
- **Probiotics**: Support digestive and immune health
- **Enhanced Nutrition**: Fermentation increases bioavailability of nutrients
- **Digestive Enzymes**: Aid in food digestion
- **Reduced Antinutrients**: Fermentation breaks down compounds that inhibit nutrient absorption
- **Unique Compounds**: Creates beneficial metabolites not found in fresh foods

**Safety Considerations**
- Use clean equipment and hands
- Maintain proper salt ratios (2-3% by weight)
- Keep vegetables submerged under liquid
- Trust your senses—bad ferments smell truly awful
- Start with small batches to learn the process
- When in doubt, throw it out

**Troubleshooting Common Issues**
- **White film on surface**: Usually kahm yeast, harmless but scrape off
- **Too salty**: Rinse before eating or dilute with fresh vegetables
- **Not sour enough**: Ferment longer or increase temperature slightly
- **Mushy texture**: Too much salt, too warm, or over-fermented

**Advanced Fermentation Projects**
Once comfortable with basics, try:
- Sourdough starter and bread
- Fermented hot sauces
- Miso and other fermented bean pastes
- Fermented dairy (if you consume dairy)
- Wine and mead making

**Seasonal Fermentation**
- **Spring**: Ferment early greens and herbs
- **Summer**: Peak season for vegetable ferments
- **Fall**: Preserve harvest abundance
- **Winter**: Focus on longer ferments and maintenance

Fermentation connects us to our ancestors while providing modern health benefits. Start simple, be patient, and enjoy the journey of creating living foods in your own kitchen.''',
                'excerpt': 'Discover the art of home fermentation with beginner-friendly recipes and techniques for creating healthy, flavorful foods.',
                'tags': ['fermentation', 'probiotics', 'food-preservation', 'healthy-eating', 'traditional-cooking'],
                'category': 'Food',
                'author_username': 'emma_chef'
            },
            
            # Lifestyle posts
            {
                'title': 'Building Sustainable Habits: The Science of Lasting Change',
                'content': '''Creating lasting change in our lives isn't about willpower or motivation—it's about understanding the science of habit formation and designing systems that support our goals. Research shows that small, consistent actions compound into remarkable transformations over time.

**The Science of Habit Formation**

**The Habit Loop**
Every habit follows a three-part neurological loop:
1. **Cue**: The trigger that initiates the behavior
2. **Routine**: The behavior itself
3. **Reward**: The benefit you gain from the behavior

Understanding this loop allows you to design new habits and modify existing ones effectively.

**The Role of the Brain**
Habits are stored in the basal ganglia, a part of the brain that operates automatically. This is why established habits require little conscious thought—your brain has automated the process to conserve mental energy.

**Principles of Sustainable Habit Formation**

**Start Ridiculously Small**
The biggest mistake people make is starting too big. Instead:
- Want to exercise? Start with 5 push-ups daily
- Want to read more? Read one page per day
- Want to meditate? Start with 2 minutes
- Want to eat healthier? Add one vegetable to each meal

Small habits are easier to maintain and build momentum for larger changes.

**Focus on Consistency Over Intensity**
It's better to do something small every day than something big occasionally:
- 10 minutes of daily exercise beats 2-hour weekend workouts
- Writing 100 words daily beats waiting for inspiration
- 5 minutes of daily cleaning beats weekend cleaning marathons

**Stack New Habits on Existing Ones**
Use habit stacking to link new behaviors to established routines:
- "After I pour my morning coffee, I will write in my gratitude journal"
- "After I brush my teeth, I will do 10 squats"
- "After I sit down at my desk, I will review my daily priorities"

**Design Your Environment**
Make good habits easier and bad habits harder:
- Place books where you'll see them
- Put your workout clothes next to your bed
- Remove junk food from easily accessible places
- Use apps to block distracting websites during work hours

**The Two-Minute Rule**
Any new habit should take less than two minutes to complete:
- "Read before bed" becomes "Read one page before bed"
- "Do yoga" becomes "Put on yoga clothes"
- "Study French" becomes "Open my French textbook"

Once the habit is established, you can gradually increase the duration.

**Common Habit-Building Mistakes**

**Trying to Change Everything at Once**
Focus on one habit at a time. Research shows that people who try to change multiple habits simultaneously have a much lower success rate.

**Relying on Motivation**
Motivation is unreliable. Instead, create systems and environments that make the right choice automatic.

**All-or-Nothing Thinking**
Missing one day doesn't ruin your progress. The key is getting back on track quickly rather than abandoning the habit entirely.

**Not Tracking Progress**
What gets measured gets managed. Use simple tracking methods:
- Habit tracking apps
- Calendar marking
- Simple checklists
- Photo documentation

**Strategies for Different Types of Habits**

**Health and Fitness Habits**
- Start with movement, not exercise
- Focus on showing up, not performance
- Prepare the night before
- Find activities you genuinely enjoy

**Productivity Habits**
- Use time-blocking for important tasks
- Implement the "two-minute rule" for small tasks
- Create morning and evening routines
- Batch similar activities together

**Learning Habits**
- Set specific learning goals
- Use spaced repetition for retention
- Teach others what you learn
- Connect new information to existing knowledge

**Relationship Habits**
- Schedule regular check-ins with loved ones
- Practice active listening
- Express gratitude daily
- Create shared rituals and traditions

**Breaking Bad Habits**

**Identify Triggers**
Understanding what triggers unwanted behaviors is crucial:
- Environmental cues (seeing junk food)
- Emotional states (stress, boredom)
- Social situations (peer pressure)
- Time-based patterns (afternoon energy crash)

**Replace, Don't Eliminate**
Instead of trying to eliminate a bad habit, replace it with a positive one:
- Replace scrolling social media with reading
- Replace stress eating with a short walk
- Replace negative self-talk with affirmations

**The 21-Day Myth**
Contrary to popular belief, habits don't form in 21 days. Research shows it takes an average of 66 days for a behavior to become automatic, with a range of 18-254 days depending on the complexity of the habit.

**Building Habit Systems**

**Morning Routines**
Create a consistent morning routine that sets a positive tone:
- Wake up at the same time
- Include physical movement
- Practice mindfulness or gratitude
- Review daily priorities

**Evening Routines**
End your day with habits that promote rest and preparation:
- Reflect on the day's accomplishments
- Prepare for tomorrow
- Limit screen time before bed
- Practice relaxation techniques

**Weekly Reviews**
Regularly assess your progress:
- What habits are working well?
- What obstacles are you encountering?
- How can you adjust your approach?
- What support do you need?

**The Compound Effect**
Small habits may seem insignificant in the moment, but they compound over time:
- Reading 10 pages daily = 3,650 pages per year (about 12 books)
- Saving $5 daily = $1,825 per year
- Walking 2,000 extra steps daily = 730,000 steps per year

Remember, sustainable change happens gradually. Focus on progress, not perfection, and trust the process of small, consistent improvements.''',
                'excerpt': 'Learn the science-backed strategies for building lasting habits and creating sustainable positive changes in your life.',
                'tags': ['habits', 'personal-development', 'behavior-change', 'productivity', 'self-improvement'],
                'category': 'Lifestyle',
                'author_username': 'alex_lifestyle'
            },
            
            # Business posts
            {
                'title': 'The Future of Work: Adapting to the Post-Pandemic Economy',
                'content': '''The COVID-19 pandemic fundamentally altered the global workplace, accelerating trends that were already emerging and creating new paradigms for how, where, and when we work. As we move forward, understanding these changes is crucial for both employers and employees.

**The Great Workplace Transformation**

**Remote Work Revolution**
What started as an emergency response has become a permanent fixture:
- 42% of the U.S. workforce now works remotely full-time
- 82% of workers want to continue working remotely at least part-time
- Companies are redesigning office spaces for collaboration rather than individual work
- Geographic barriers to talent acquisition have largely disappeared

**Hybrid Work Models**
Most organizations are adopting flexible hybrid approaches:
- 2-3 days in office, 2-3 days remote
- Core collaboration days when teams gather
- Flexible scheduling based on project needs
- Results-oriented work environments (ROWE)

**Key Trends Shaping the Future of Work**

**Digital-First Operations**
- Cloud-based tools and platforms as standard infrastructure
- AI and automation handling routine tasks
- Digital collaboration tools replacing in-person meetings
- Cybersecurity as a critical business function

**Employee Well-being Focus**
- Mental health support and resources
- Flexible scheduling for work-life balance
- Emphasis on preventing burnout
- Comprehensive benefits packages including wellness programs

**Skills-Based Hiring**
- Focus on capabilities rather than credentials
- Continuous learning and reskilling programs
- Project-based and gig work integration
- Cross-functional team collaboration

**Diversity, Equity, and Inclusion (DEI)**
- Intentional efforts to build diverse teams
- Inclusive leadership training
- Equitable compensation practices
- Accessible workplace design and policies

**Challenges in the New Work Environment**

**For Employers**
- Maintaining company culture in distributed teams
- Ensuring equitable treatment of remote and in-office workers
- Managing productivity and performance remotely
- Providing adequate technology and support
- Adapting legal and compliance frameworks

**For Employees**
- Establishing work-life boundaries at home
- Combating isolation and maintaining connections
- Managing distractions and staying productive
- Developing new digital communication skills
- Navigating career advancement in remote environments

**Strategies for Success in the Future of Work**

**For Organizations**

**Invest in Technology Infrastructure**
- Reliable, secure remote access systems
- Collaboration platforms (Slack, Microsoft Teams, Zoom)
- Project management tools (Asana, Monday.com, Jira)
- Cloud-based file storage and sharing
- Cybersecurity measures and training

**Redefine Performance Management**
- Focus on outcomes rather than hours worked
- Set clear, measurable goals and expectations
- Regular check-ins and feedback sessions
- Flexible performance review cycles
- Recognition and reward systems for remote workers

**Foster Virtual Culture**
- Virtual team-building activities
- Online coffee chats and social hours
- Digital recognition programs
- Shared virtual workspaces
- Company-wide online events and celebrations

**Support Employee Development**
- Online learning and development platforms
- Virtual mentorship programs
- Cross-functional project opportunities
- Leadership development for remote management
- Career pathing in distributed organizations

**For Individual Workers**

**Develop Digital Fluency**
- Master video conferencing etiquette
- Learn collaborative software tools
- Understand digital project management
- Develop online presentation skills
- Stay current with industry-specific technology

**Build Remote Work Skills**
- Time management and self-discipline
- Effective written communication
- Virtual relationship building
- Independent problem-solving
- Adaptability and resilience

**Create Effective Home Workspaces**
- Dedicated work area with proper ergonomics
- Reliable internet and technology setup
- Good lighting and minimal distractions
- Professional background for video calls
- Separation between work and personal spaces

**Maintain Professional Networks**
- Participate in virtual industry events
- Join online professional communities
- Schedule regular check-ins with colleagues
- Engage in social media professional networking
- Seek out virtual mentorship opportunities

**Industry-Specific Adaptations**

**Technology Sector**
- Fully distributed teams becoming the norm
- Emphasis on asynchronous communication
- Global talent acquisition strategies
- Continuous learning and upskilling programs

**Healthcare**
- Telemedicine and remote patient monitoring
- Hybrid administrative and clinical roles
- Enhanced infection control protocols
- Technology integration in patient care

**Education**
- Blended learning models
- Digital curriculum development
- Online student engagement strategies
- Teacher training for virtual instruction

**Financial Services**
- Digital-first customer service
- Remote financial advisory services
- Enhanced cybersecurity measures
- Automated processes and AI integration

**Preparing for Continued Change**

**Stay Adaptable**
The future of work will continue evolving. Key principles for adaptation:
- Embrace lifelong learning
- Develop transferable skills
- Build diverse professional networks
- Stay informed about industry trends
- Maintain flexibility in career planning

**Focus on Human Skills**
As automation handles routine tasks, uniquely human skills become more valuable:
- Emotional intelligence
- Creative problem-solving
- Critical thinking
- Leadership and influence
- Empathy and communication

**The Long-Term Outlook**
The future of work will likely feature:
- Increased automation and AI integration
- More flexible, project-based employment
- Greater emphasis on work-life integration
- Continued globalization of talent markets
- Sustainability and social responsibility focus

Organizations and individuals who proactively adapt to these changes will thrive in the post-pandemic economy. The key is to remain flexible, invest in continuous learning, and focus on creating value in new and innovative ways.''',
                'excerpt': 'Explore how the pandemic has permanently changed the workplace and strategies for thriving in the new economy.',
                'tags': ['future-of-work', 'remote-work', 'business-strategy', 'workplace-culture', 'digital-transformation'],
                'category': 'Business',
                'author_username': 'david_business'
            }
        ]
        
        created_count = 0
        
        for post_data in diverse_posts:
            # Check if post already exists
            if BlogPost.objects.filter(title=post_data['title']).exists():
                self.stdout.write(f'Post "{post_data["title"]}" already exists, skipping...')
                continue
            
            # Get the specified author
            try:
                author = User.objects.get(username=post_data['author_username'])
            except User.DoesNotExist:
                self.stdout.write(f'Author {post_data["author_username"]} not found, using admin...')
                author = User.objects.get(username='admin')
            
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
                published_at=timezone.now() - timedelta(days=random.randint(1, 15))
            )
            
            # Add tags using django-taggit
            post.tags.add(*post_data['tags'])
            
            created_count += 1
            self.stdout.write(f'Created post: {post.title} by {author.username}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} diverse blog posts!')
        )
