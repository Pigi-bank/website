from django.http import JsonResponse
from django.shortcuts import render

from website.forms import SubscribeForm
from .models import Subscribers
from .email import send_welcome_email
# Create your views here.
def index(request):
  form = SubscribeForm()
  return render(request, 'index.html', {"subscribeForm":form})

def subscriber(request):
  name = request.POST.get('name')
  phone_number = request.POST.get('phone_number')
  email = request.POST.get('email')

  recipient = Subscribers(name = name, phone_number = phone_number, email = email)
  
  recipient.save()
  send_welcome_email(name,email)
  data = {'Success': 'You have been added to the mailing list'}
  return JsonResponse(data)