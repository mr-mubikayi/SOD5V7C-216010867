from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'title': 'Welcome to Our Website',
        'message': 'This is the home page of our Django application.',
        'current_time': '2025-06-17'
    }
    return render(request, 'main/home.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'company_name': 'Django Demo Company',
        'description': 'We are a demonstration company showcasing Django web development capabilities.',
        'features': ['Modern Web Design', 'Responsive Layout', 'Template Inheritance', 'URL Routing']
    }
    return render(request, 'main/about.html', context)

def posts(request):
    all_posts = Post.objects.all().order_by('-publication_date')
    popular_posts = Post.objects.filter(views__gt=100).order_by('-views')
    total_posts = all_posts.count()
    popular_count = popular_posts.count()
    
    context = {
        'posts': all_posts,
        'popular_posts': popular_posts,
        'total_posts': total_posts,
        'popular_count': popular_count,
        'title': 'Blog Posts'
    }
    return render(request, 'main/posts.html', context)
