from django.core.mail import  send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from post.models import *

def send_subscriber_mail(title,content,link,current_site):

    recievers = ['unurlan05@gmail.com','rehimli195@gmail.com','idris.ceferov244@gmail.com']

    current_site = current_site
    subject=str('Coders Azerbaijandan') + " " +str(title) + " " +str('adlı yeni məqalə')
    message=render_to_string('send_mail.html', {
                'title':title,
                'content':content,
                'domain': current_site.domain,
                'link':link,
                })
    send_mail(subject,message,'verify@buqelemun.com',recievers)
