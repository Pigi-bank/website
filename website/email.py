from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
  #Creating message subject and sender
  subject = 'PIGIBANK LAUNCH'
  sender = 'mercy@pigibank.co'

  text_context = render_to_string('email/subscribemail.txt')
  html_content = render_to_string('email/template_email.html')

  msg = EmailMultiAlternatives(subject, text_context, sender, [receiver])
  msg.attach_alternative(html_content, 'text/html')
  msg.send()