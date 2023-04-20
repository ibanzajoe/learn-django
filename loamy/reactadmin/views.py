from django.shortcuts import render

# Create your views here.
def dashboard(request, *args, **kwargs):
    return render(request, "reactadmin/index.html")