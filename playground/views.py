import logging

import requests
from django.core.cache import cache
from django.core.mail import (BadHeaderError, EmailMessage, mail_admins,
                              send_mail)
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from templated_mail.mail import BaseEmailMessage

from playground.tasks import notify_customers

# Create your views here.

logger = logging.getLogger(__name__)

class HelloView(APIView):
    # @method_decorator(cache_page(5 * 50))
    def get(self, request):
        try:
            
            logger.info('Calling httpbin')
            response = requests.get("https://httpbin.org/delay/2")
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, "hello.html", {"name": data})


# @cache_page(5 * 50)
# def say_hello(request):
#     # notify_customers.delay("Hello")
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, "hello.html", {"name": data})


# message = BaseEmailMessage(
#     template_name='emails/hello.html',
#     context ={'name':'Daniel' }
# )
# message.send(['namebethat@dan.com'])


# send_mail('subject', 'message', 'info@dan.com', ['mbazudaniel97@gmail.com'])
# mail_admins('subject', 'message', html_message='message')
# message =   EmailMessage('subject', 'message', 'info@dan.com', ['mbazudaniel97@gmail.com'])
# message.attach_file('playground/static/images/1.png')
# message.send()
