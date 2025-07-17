from django.shortcuts import render

<<<<<<< HEAD
def index_view(request):
    return render(request, 'index.html')

def role_choice_view(request):
    return render(request, 'rolechoice.html')

def login_page(request):
    return render(request, 'loginpage.html')
=======
def profile_view(request):
    return render(request, 'profile.html')

def dept_view(request):
    return render(request, 'dept.html')

def update_view(request):
    return render(request, 'update.html')
>>>>>>> cece332 (changes)
