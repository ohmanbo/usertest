from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def view_login(request):
    
    if request.method == 'POST':
        acc = request.POST['account']
        pwd = request.POST['password']
        
        user = authenticate(username=acc, password=pwd )
        
        if user is not None:
            login(request, user)
        else:
            print("인증실패")
        
        print(request.POST)
    
    return render(request, 'users/login.html')

def view_logout(request):
    logout(request)
    return redirect("users:login")