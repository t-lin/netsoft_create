import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser


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
