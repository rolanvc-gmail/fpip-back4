from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def unlock_user_notify(email_add, user, locator, newpasswd):
    """
    Sends an email to a locked user
    :param email_add:
    :param user:
    :param locator:
    :param newpasswd:
    :return:
    """
    from_email = "parkadmin@fpip.com"
    to_email = [email_add]
    template_html = 'unlocked_user_notify.html'
    template_text = 'unlocked_user_notify.txt'
    subject = "FPIP PARK ACCESS PORTAL NOTIFICATION"

    data = {
        "user_email": email_add,
        "passwd": newpasswd
    }
    try:
        text_content = render_to_string(template_text, data)
        html_content = render_to_string(template_html, data)
    except Exception as e:
        print (e.message)

    send_mail(subject, text_content, settings.EMAIL_HOST_USER,
              to_email, fail_silently=False, html_message=html_content)


def newuser_notify(email_add, name, newuser, locator):
    '''
    Sends an email to user re new user he enrolled
    :param email_add: addresseee
    :param name: name of addressee
    :param newuser: the new user
    :param locator: locator
    :return:
    '''
    # me == my email address
    # you == recipient's email address
    from_email = "parkadmin@fpip.com"
    to_email = [email_add]
    template_html = 'new_user_notify.html'
    template_text = 'new_user_notify.txt'
    subject = "FPIP PARK ACCESS PORTAL NOTIFICATION"

    data = {
        "authorizer": name,
        "new_user": newuser,
        "locator": locator,
        "email": email_add
    }

    text_content = render_to_string(template_text, data)
    html_content = render_to_string(template_html, data)

    send_mail(subject, text_content, settings.EMAIL_HOST_USER,
              to_email, fail_silently=False, html_message=html_content)


def gv_notify(email_add, name, trans_no):
    '''
    :param email_add: end an email to a user who requested guest visitor access that his request had been received and processed.
    :param name:
    :param trans_no:
    :return:
    '''
    to_email = [email_add]
    template_html = 'gv_app.html'
    template_text = 'gv_app.txt'
    subject = "FPIP PARK ACCESS PORTAL NOTIFICATION"

    data = {
        "name": name,
        "trans_no":trans_no}
    text_content = render_to_string(template_text, data)
    html_content = render_to_string(template_html, data)

    send_mail(subject, text_content, settings.EMAIL_HOST_USER,
              to_email, fail_silently=False, html_message=html_content)


def empblacklist_notify(email_add, user, emp_lastname, emp_firstname, app_type):
    '''
        send an email to emaail_add that user applied emp who is blacklisted to an app_type application.
        :param email_add: email of addressee
        :param user: user
        :param emp_lastname: employee lastname
        :param emp_firstname: employee firstname
        :param app_type: application type
        :return: None
    '''

    from_email = "parkadmin@fpip.com"
    to_email = [email_add]
    template_html = 'empblacklist_notify.html'
    template_text = 'empblacklist_notify.txt'
    subject = "FPIP PARK ACCESS PORTAL NOTIFICATION:BLACKLIST"
    data = {
        "email_add": email_add,
        "user":user,
        "emp_lastname":emp_lastname,
        "emp_firstname":emp_firstname,
        "app_type": app_type
    }
    text_content = render_to_string(template_text, data)
    html_content = render_to_string(template_html, data)

    send_mail(subject, text_content, settings.EMAIL_HOST_USER,
              to_email, fail_silently=False, html_message=html_content)

def user_locked_email(username, user_email):
    '''
      email user thaat his account has been locked.
    :param username: the name of the user for Dear username
    :param user_email: his email address account
    :return:
    '''
    to_email = [user_email]
    template_html = 'user_locked_email.html'
    template_text = 'user_locked_email.txt'
    subject = "FPIP PARK ACCESS PORTAL: THIS ACCOUNT HAS BEEN LOCKED"
    data = {
        "useremail": user_email,
        "username":username,
    }
    text_content = render_to_string(template_text, data)
    html_content = render_to_string(template_html, data)

    send_mail(subject, text_content, settings.EMAIL_HOST_USER,
              to_email, fail_silently=False, html_message=html_content)

def user_locked_notify(creator_name, creator_email, username, useremail):
    '''
    send notification to creator ( of account) that account useremail has been locked
    :param creator_name:
    :param creator_email:
    :param username:
    :param useremail:
    :return:
    '''
    to_email = [creator_email]
    template_html = 'user_locked_notify.html'
    template_text = 'user_locked_notify.txt'
    subject = "FPIP PARK ACCESS PORTAL: ACCOUNT HAS BEEN LOCKED"
    data = {
        "creator_name": creator_name,
        "creator_email": creator_email,
        "username":username,
        "useremail":useremail,
    }
    text_content = render_to_string(template_text, data)
    html_content = render_to_string(template_html, data)

    send_mail(subject, text_content, settings.EMAIL_HOST_USER,
              to_email, fail_silently=False, html_message=html_content)

def flagged_purpose_notify(email_add, user, locator, purpose, app_type):
    '''
        send an email to emaail_add that user applied emp who is blacklisted to an app_type application.
        :param email_add: email of addressee
        :param user: user
        :param emp_lastname: employee lastname
        :param emp_firstname: employee firstname
        :param app_type: application type
        :return: None
    '''

    from_email = "parkadmin@fpip.com"
    to_email = [email_add]
    template_html = 'flagged_purpose_notify.html'
    template_text = 'flagged_purpose_notify.txt'
    subject = "FPIP PARK ACCESS PORTAL NOTIFICATION:FLAGGED PURPOSE"
    data = {
        "email_add": email_add,
        "user":user,
        "locator":locator,
        "purpose":purpose,
        "app_type": app_type
    }
    text_content = render_to_string(template_text, data)
    html_content = render_to_string(template_html, data)

    send_mail(subject, text_content, settings.EMAIL_HOST_USER,
              to_email, fail_silently=False, html_message=html_content)


def gv_notify_batch(email_add, fullname, trn_list):
    '''
    :param email_add: end an email to a user who requested guest visitor access that his request had been received and processed.
    :param name:
    :param trans_no:
    :return:
    '''
    to_email = [email_add]
    template_html = 'gv_app_batch.html'
    template_text = 'gv_app_batch.txt'
    subject = "FPIP PARK ACCESS PORTAL NOTIFICATION"

    data = {
        "fullname": fullname,
        "trn_list":trn_list}
    text_content = render_to_string(template_text, data)
    html_content = render_to_string(template_html, data)

    send_mail(subject, text_content, settings.EMAIL_HOST_USER,
              to_email, fail_silently=False, html_message=html_content)
