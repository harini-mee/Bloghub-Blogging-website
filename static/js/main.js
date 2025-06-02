// Main JavaScript for BlogHub

$(document).ready(function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Professional interactions
    initProfessionalNavbar();
    initProfessionalCards();
    initProfessionalForms();
    initScrollAnimations();
    initInteractiveElements();

    // Smooth scrolling for anchor links
    $('a[href*="#"]').not('[href="#"]').not('[href="#0"]').click(function(event) {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && 
            location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                event.preventDefault();
                $('html, body').animate({
                    scrollTop: target.offset().top - 100
                }, 1000);
            }
        }
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000);

    // Like button functionality
    $('.like-btn').click(function(e) {
        e.preventDefault();
        var btn = $(this);
        var postSlug = btn.data('post-slug');
        var liked = btn.data('liked') === 'true';
        
        // Show loading state
        btn.prop('disabled', true);
        var originalHtml = btn.html();
        btn.html('<i class="fas fa-spinner fa-spin"></i>');
        
        $.ajax({
            url: '/post/' + postSlug + '/like/',
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val()
            },
            success: function(data) {
                btn.data('liked', data.liked);
                btn.find('.like-count').text(data.like_count);
                
                if (data.liked) {
                    btn.find('i').first().addClass('text-danger');
                    btn.removeClass('btn-outline-danger').addClass('btn-danger');
                } else {
                    btn.find('i').first().removeClass('text-danger');
                    btn.removeClass('btn-danger').addClass('btn-outline-danger');
                }
                
                // Animation
                btn.addClass('animate__animated animate__pulse');
                setTimeout(function() {
                    btn.removeClass('animate__animated animate__pulse');
                }, 1000);
            },
            error: function() {
                alert('Error occurred while processing your request.');
            },
            complete: function() {
                btn.prop('disabled', false);
                btn.html(originalHtml);
            }
        });
    });

    // Comment reply functionality
    $('.reply-btn').click(function(e) {
        e.preventDefault();
        var commentId = $(this).data('comment-id');
        var replyForm = $('#reply-form-' + commentId);
        
        // Hide other reply forms
        $('.reply-form').not(replyForm).slideUp();
        
        // Toggle current reply form
        replyForm.slideToggle();
        
        // Focus on textarea if showing
        if (replyForm.is(':visible')) {
            replyForm.find('textarea').focus();
        }
    });

    // Cancel reply
    $('.cancel-reply').click(function() {
        $(this).closest('.reply-form').slideUp();
    });

    // Search functionality
    $('#search-form').submit(function(e) {
        var query = $('#search-input').val().trim();
        if (query === '') {
            e.preventDefault();
            alert('Please enter a search term.');
            $('#search-input').focus();
        }
    });

    // Auto-save for forms (localStorage)
    function autoSave() {
        var formData = {};
        $('#post-form input, #post-form textarea').each(function() {
            var field = $(this);
            if (field.attr('name') && field.val()) {
                formData[field.attr('name')] = field.val();
            }
        });
        
        if (Object.keys(formData).length > 0) {
            localStorage.setItem('blog_post_draft', JSON.stringify(formData));
            showNotification('Draft saved automatically', 'success');
        }
    }

    // Restore auto-saved data
    function restoreAutoSave() {
        var savedData = localStorage.getItem('blog_post_draft');
        if (savedData) {
            try {
                var formData = JSON.parse(savedData);
                var hasData = false;
                
                for (var field in formData) {
                    var input = $('[name="' + field + '"]');
                    if (input.length && !input.val()) {
                        input.val(formData[field]);
                        hasData = true;
                    }
                }
                
                if (hasData) {
                    showNotification('Auto-saved draft restored', 'info');
                }
            } catch (e) {
                console.log('Error restoring auto-save data:', e);
            }
        }
    }

    // Auto-save timer for post forms
    if ($('#post-form').length) {
        restoreAutoSave();
        
        var autoSaveTimer;
        $('#post-form input, #post-form textarea').on('input', function() {
            clearTimeout(autoSaveTimer);
            autoSaveTimer = setTimeout(autoSave, 10000); // Save every 10 seconds
        });
        
        // Clear auto-save on successful submission
        $('#post-form').submit(function() {
            localStorage.removeItem('blog_post_draft');
        });
    }

    // Image preview functionality
    function previewImage(input, previewContainer) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                $(previewContainer).html(
                    '<img src="' + e.target.result + '" class="img-fluid rounded shadow" style="max-height: 300px;">'
                );
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    // File input change handlers
    $('input[type="file"]').change(function() {
        var previewId = $(this).attr('id') + '-preview';
        var previewContainer = $('#' + previewId);
        if (previewContainer.length === 0) {
            previewContainer = $(this).siblings('.image-preview');
        }
        if (previewContainer.length) {
            previewImage(this, previewContainer);
        }
    });

    // Notification system
    function showNotification(message, type = 'info') {
        var alertClass = 'alert-' + type;
        var notification = $('<div class="alert ' + alertClass + ' alert-dismissible fade show position-fixed" style="top: 20px; right: 20px; z-index: 9999;">' +
            message +
            '<button type="button" class="btn-close" data-bs-dismiss="alert"></button>' +
            '</div>');
        
        $('body').append(notification);
        
        setTimeout(function() {
            notification.fadeOut(function() {
                $(this).remove();
            });
        }, 5000);
    }

    // Infinite scroll for blog posts (optional)
    var loading = false;
    var page = 2;
    
    function loadMorePosts() {
        if (loading) return;
        loading = true;
        
        $.get('?page=' + page, function(data) {
            var newPosts = $(data).find('.blog-post');
            if (newPosts.length) {
                $('.blog-posts-container').append(newPosts);
                page++;
                loading = false;
            } else {
                $(window).off('scroll', handleScroll);
            }
        }).fail(function() {
            loading = false;
        });
    }
    
    function handleScroll() {
        if ($(window).scrollTop() + $(window).height() >= $(document).height() - 1000) {
            loadMorePosts();
        }
    }
    
    // Enable infinite scroll if on home page
    if ($('.blog-posts-container').length && $('.pagination').length === 0) {
        $(window).scroll(handleScroll);
    }

    // Character counter for textareas
    $('textarea[maxlength]').each(function() {
        var textarea = $(this);
        var maxLength = textarea.attr('maxlength');
        var counter = $('<div class="text-muted small text-end mt-1"><span class="current">0</span>/' + maxLength + ' characters</div>');
        textarea.after(counter);
        
        textarea.on('input', function() {
            var currentLength = $(this).val().length;
            counter.find('.current').text(currentLength);
            
            if (currentLength > maxLength * 0.9) {
                counter.addClass('text-warning');
            } else {
                counter.removeClass('text-warning');
            }
            
            if (currentLength >= maxLength) {
                counter.addClass('text-danger').removeClass('text-warning');
            } else {
                counter.removeClass('text-danger');
            }
        });
        
        // Trigger initial count
        textarea.trigger('input');
    });

    // Copy to clipboard functionality
    $('.copy-btn').click(function() {
        var text = $(this).data('copy-text') || $(this).prev().text();
        navigator.clipboard.writeText(text).then(function() {
            showNotification('Copied to clipboard!', 'success');
        });
    });

    // Reading time calculator
    function calculateReadingTime(text) {
        var wordsPerMinute = 200;
        var words = text.trim().split(/\s+/).length;
        var minutes = Math.ceil(words / wordsPerMinute);
        return minutes;
    }

    // Add reading time to posts
    $('.post-content').each(function() {
        var content = $(this).text();
        var readingTime = calculateReadingTime(content);
        var readingTimeHtml = '<small class="text-muted"><i class="fas fa-clock me-1"></i>' + readingTime + ' min read</small>';
        $(this).closest('article').find('.post-meta').append(' • ' + readingTimeHtml);
    });

    // Lazy loading for images
    if ('IntersectionObserver' in window) {
        var imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    var img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(function(img) {
            imageObserver.observe(img);
        });
    }

    // Theme toggle (if implemented)
    $('.theme-toggle').click(function() {
        $('body').toggleClass('dark-theme');
        var isDark = $('body').hasClass('dark-theme');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });

    // Restore theme preference
    var savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        $('body').addClass('dark-theme');
    }
});

// Professional Interactive Functions

// Professional Navbar
function initProfessionalNavbar() {
    const navbar = document.querySelector('.navbar');

    // Navbar scroll effect
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Active link highlighting
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

// Professional Card Interactions
function initProfessionalCards() {
    const cards = document.querySelectorAll('.card');

    // Intersection Observer for card animations
    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 100);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
        cardObserver.observe(card);
    });
}

// Parallax scrolling effect
function initParallaxEffect() {
    $(window).scroll(function() {
        const scrolled = $(this).scrollTop();
        const parallax = $('.hero-background');
        const speed = 0.5;

        parallax.css('transform', 'translateY(' + (scrolled * speed) + 'px)');

        // Floating elements parallax
        $('.floating-element').each(function(index) {
            const speed = 0.3 + (index * 0.1);
            $(this).css('transform', 'translateY(' + (scrolled * speed) + 'px)');
        });
    });
}

// Card hover animations
function initCardAnimations() {
    $('.card').hover(
        function() {
            $(this).addClass('animate__animated animate__pulse');
        },
        function() {
            $(this).removeClass('animate__animated animate__pulse');
        }
    );

    // Staggered animation for cards on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('animate__animated', 'animate__fadeInUp');
                }, index * 100);
            }
        });
    });

    document.querySelectorAll('.card').forEach(card => {
        observer.observe(card);
    });
}

// Floating elements animation
function initFloatingElements() {
    // Create random floating particles
    for (let i = 0; i < 20; i++) {
        createFloatingParticle();
    }
}

function createFloatingParticle() {
    const particle = document.createElement('div');
    particle.className = 'floating-particle';
    particle.innerHTML = ['✨', '💖', '🌟', '💫', '🦋', '🌸'][Math.floor(Math.random() * 6)];

    particle.style.left = Math.random() * 100 + 'vw';
    particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
    particle.style.animationDelay = Math.random() * 5 + 's';

    document.body.appendChild(particle);

    // Remove particle after animation
    setTimeout(() => {
        if (particle.parentNode) {
            particle.parentNode.removeChild(particle);
        }
    }, 15000);
}

// Professional Form Interactions
function initProfessionalForms() {
    // Enhanced form validation
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');

        inputs.forEach(input => {
            // Add floating label effect
            input.addEventListener('focus', () => {
                input.parentElement.classList.add('focused');
            });

            input.addEventListener('blur', () => {
                if (!input.value) {
                    input.parentElement.classList.remove('focused');
                }
            });

            // Real-time validation feedback
            input.addEventListener('input', () => {
                validateField(input);
            });
        });
    });
}

function validateField(field) {
    const value = field.value.trim();
    const fieldContainer = field.parentElement;

    // Remove existing feedback
    const existingFeedback = fieldContainer.querySelector('.field-feedback');
    if (existingFeedback) {
        existingFeedback.remove();
    }

    // Basic validation
    let isValid = true;
    let message = '';

    if (field.required && !value) {
        isValid = false;
        message = 'This field is required';
    } else if (field.type === 'email' && value && !isValidEmail(value)) {
        isValid = false;
        message = 'Please enter a valid email address';
    }

    // Apply validation styling
    if (!isValid) {
        field.classList.add('is-invalid');
        const feedback = document.createElement('div');
        feedback.className = 'field-feedback text-danger small mt-1';
        feedback.textContent = message;
        fieldContainer.appendChild(feedback);
    } else {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
    }
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Scroll Animations
function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('.hero-stats .stat-item, .section-header');

    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.2
    });

    animatedElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
        scrollObserver.observe(element);
    });
}

// Interactive Elements
function initInteractiveElements() {
    // Button ripple effect
    const buttons = document.querySelectorAll('.btn');

    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple-effect');

            this.appendChild(ripple);

            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Enhanced tooltips
    const tooltipElements = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipElements.forEach(element => {
        new bootstrap.Tooltip(element, {
            animation: true,
            delay: { show: 300, hide: 100 }
        });
    });
}

// Global functions
window.BlogHub = {
    showNotification: function(message, type = 'info') {
        const notification = $(`
            <div class="magical-notification ${type} animate__animated animate__fadeInRight">
                <i class="fas fa-sparkles me-2"></i>
                ${message}
                <button class="btn-close" onclick="$(this).parent().remove()"></button>
            </div>
        `);

        $('body').append(notification);

        setTimeout(() => {
            notification.addClass('animate__fadeOutRight');
            setTimeout(() => notification.remove(), 500);
        }, 4000);
    },

    confirmDelete: function(message = 'Are you sure you want to delete this magical creation?') {
        return confirm(message);
    },

    formatDate: function(date) {
        return new Date(date).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    },

    addSparkles: function(element) {
        for (let i = 0; i < 5; i++) {
            const sparkle = document.createElement('div');
            sparkle.className = 'sparkle';
            sparkle.innerHTML = '✨';
            sparkle.style.left = Math.random() * 100 + '%';
            sparkle.style.top = Math.random() * 100 + '%';
            element.appendChild(sparkle);

            setTimeout(() => sparkle.remove(), 1000);
        }
    }
};
