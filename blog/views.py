from django.shortcuts import render

def home(request):
    return render(request, 'home.html')



template_name = "blog/index.html"
paginate_by = 6

