from django.shortcuts import render

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