from django.urls import path
from django.http import HttpResponse
from django_app.views import my_view, AuthorProfileView

def my_view2(request, *args, **kwargs):
    print(request)
    print(args)
    print(kwargs)
    return HttpResponse("Hello World")

urlpatterns = [
    path('cars/car_list/', my_view),
    path('cars/details/<int:id>/', my_view2),
    path('cars/brands/<str:brand>', my_view2),
    #path('author/<int:id>/profile', author_profile_view),
    path('author/<int:id>/profile', AuthorProfileView.as_view()),
]