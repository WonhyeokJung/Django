from django.shortcuts import render

# Create your views here.
def dinner(request, dinner_menu, people):
    context = {
        'dinner_menu': dinner_menu,
        'people': people,
    }
    return render(request, 'workshop0309/dinner.html', context)