from lib2to3.pgen2 import token
from flask_mail import Message
from flask import url_for
from api import app, mail


def send_email(to, subject, token):
    msg = Message(
        subject,
        recipients=[to],
        sender=app.config['MAIL_USERNAME'])
    msg.body=f'''
            To activate your account visit the following link: {url_for('confirm', token=token, _external=True)}
            If you did not make this account, please ignore this email.
        '''
    mail.send(msg)

def send_reset_email(to, subject, token):
    msg = Message(
        subject,
        recipients=[to],
        sender=app.config['MAIL_USERNAME'])
    msg.body=f'''
            To reset your password click the following link: http://localhost:3000/forgot-password/{token}
            If you did not request to change your password, please ignore this email.
        '''
    mail.send(msg)