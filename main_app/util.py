import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

import json
import string
from random import *
import requests

#from django.conf import settings
from netsoft_create import settings
#settings.configure(default_settings=main_app_defaults, DEBUG=True)


def get_account_info():
    ret_dict = {}
    config = configparser.ConfigParser()
    config.read("/etc/apache2/email_account_config.py")
    ret_dict["from_addr"] = config.get("email", "from_addr")
    ret_dict["password"] = config.get("email", "password")
    return ret_dict

def send_email(to_addr, subject, body):
    # sender information
    info = get_account_info()
    from_addr = info["from_addr"]
    passwd = info["password"]

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, passwd)

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def send_user_account_email(email, first_name, username, password):

    subject = "Netsoft CREATE Account"

    body = "Dear "+first_name+",\n\n"
    body += "A new account has been created to access the Netsoft CREATE Portal.\n\n"
    body += "Username: %s" % username+"\n"
    body += "Password: %s" % password+"\n\n"
    body += "If you have any questions, please contact: v.cirillo@utoronto.ca"+"\n"

    send_email(email, subject, body)

def verify_recaptcha(recaptcha_response, remote_ip):

    url = settings.GOOGLE_RECAPTCHA_VERIFY_URL

    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response,
        'remoteip': remote_ip
    }
    data = requests.post(url, data=values)
    result = json.loads(data.text)
    return result


def create_user(form):

    first_name = form.cleaned_data.get('first_name')
    last_name = form.cleaned_data.get('last_name')
    email = form.cleaned_data.get('email')

    username = first_name+"."+last_name

    # generate password
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(8, 16)))

    # create user
    try:
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name

        print("first_name: %s, last_name: %s, email: %s, username: %s, password: %s" %(first_name, last_name, email, username,password))

        user.save()
    except Exception as e:
        result = "Invalid input. Try again!"

    else:
        # Not really error, work on aesthetics (like diff. msgs with diff. dialogs later)
        result = "Successfully created user! Please check your e-mail for the login information."
        send_user_account_email(email, first_name, username, password)

    return result
