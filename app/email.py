from flask_mail import Message
from flask import render_template
from .import mail

def welcome_message(subject, template, to, **kwargs):
    sender_email = 'mutuma.brian@yahoo.com'
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + '.txt', **kwargs)
    email.html = render_template(template + '.html', **kwargs)
    mmail.send(email)

def notification_message(subject, template, to, **kwargs):
    sender_email = 'mutuma.brian@yahoo.com'
    email = Message(subject, template, to, **kwargs)
    email.body = render_template(template + '.txt', **kwargs)
    email.html = render_template(template + '.html', **kwargs)
    mail.send(email)
