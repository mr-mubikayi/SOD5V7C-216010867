from django.shortcuts import render

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
