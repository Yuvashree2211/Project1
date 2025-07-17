from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def role_choice_view(request):
    return render(request, 'rolechoice.html')

def login_page(request):
    return render(request, 'loginpage.html')
