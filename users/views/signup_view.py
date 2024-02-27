from django.shortcuts import render, redirect
from ..models import User
from ..sw.email_sender import send_verification_email
import secrets
from django.http import HttpResponse

def view_signup(request):
    if request.method == 'POST':
        print(request.POST)
        account = request.POST['account']
        password = request.POST['password']
        display_name = request.POST['display_name']
        email = request.POST['email']
        
        user = User.objects.create_user(account, email, password)
        email_token = secrets.token_urlsafe(16)
        user.email_verification_token = email_token
        user.save()
        
        
        print(email_token + "send_verification_mail 호출")
        try:
            send_verification_email(email, display_name, email_token)
            
        except Exception as e:
            print(f"Error: {e}")
        return redirect("users:login")
        
    return render(request, 'users/signup.html')

def view_verifyemail(request):
    
     
        email_token = request.GET.get('email_token', None)
        if email_token:
            try:
                user = User.objects.get(email_verification_token = email_token)
                if( user.is_active is not True ):
                    user.is_active = True
                    user.save()
                    return render(request, 'users/verifyemail_success.html')
                else:
                    return HttpResponse('계정이 이미 활성화되었습니다.')
            except User.DoesNotExist:
                # 토큰이 유효하지 않을 때의 처리
                return HttpResponse('유효하지 않은 인증 요청입니다.')
        else:
            # 토큰이 URL에 없을 때의 처리
            return HttpResponse('유효하지 않은 접근입니다.')
