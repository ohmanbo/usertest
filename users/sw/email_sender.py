from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags


def send_test_email(subject, display_name, recipient_list):
    
    message = display_name + ', please confirm your email address thanks.'
    
    send_mail(
        subject,  # 이메일 제목
        message,  # 이메일 본문 메시지
        'ohmanbo@gmail.com',  # 보내는 이메일 (settings.py에 설정된 EMAIL_HOST_USER와 동일)
        recipient_list,  # 받는 사람의 이메일 주소 리스트
        fail_silently=False,
    )
    
def send_verification_email(user_email, user_name, verification_token):
    subject = "이메일 인증 요청"
    verification_url = 'http://127.0.0.1:8000/auth/verifyemail=email_token?' + verification_token
    html_message = render_to_string('emails/email_verification.html', {
        'user_name': user_name,
        'verification_url': verification_url,
    })
    plain_message = strip_tags(html_message)
    from_email = 'ohmanbo@gmail.com'
    
    send_mail(subject, plain_message, from_email, [user_email], html_message=html_message)