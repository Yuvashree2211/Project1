from django.shortcuts import render

def sidebar_view(request):
    return render(request, 'profile.html')  # HTML template inside user/templates/

from django.shortcuts import render

def dept_view(request):
    return render(request, 'dept.html')  # Match this with the file name in templates folder

def update_profile_view(request):
    return render(request, 'update.html')  # Make sure the file is saved as update.html
