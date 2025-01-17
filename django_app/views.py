from django.views.generic import TemplateView
from django.shortcuts import render
from django_app.models import Author

# FUNCTION BASED VIEWS
def my_view(request):
    car_list = [
        {'title': 'Ford'},
        {'title': 'BMW'},
        {'title': 'Toyota'},
        {'title': 'Honda'},
    ]

    context = {
        'car_list': car_list
    }
    return render(request, 'django_app/car_list.html', context)

# CLASS BASED VIEWS
class AuthorProfileView(TemplateView):
    template_name = 'django_app/author_profile.html'

    def get_context_data(self, **kwargs):
        author = Author.objects.get(id=kwargs['id'])
        return {
            'author_profile': author,
        }

# FUNCTION BASED VIEWS
def author_profile_view(request, **kwargs):
    author = Author.objects.get(id=kwargs['id'])
    context = {
        'author_profile': author
    }
    return render(request, 'django_app/author_profile.html', context)