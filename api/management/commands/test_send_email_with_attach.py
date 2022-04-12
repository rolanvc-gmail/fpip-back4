"""
This sends a test email with files as attachemnts.
"""
from django.core.mail import send_mail, EmailMessage
from django.core.management.base import BaseCommand
from smtplib import SMTPException
import os

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        email = EmailMessage( "Test Email", "Using EmailMessage class.", None, ['rolanvc@gmail.com'])

        the_folder = "/home/rolan/data1/Dropbox/Temp/fpip-sheets"
        the_file_2021 = os.path.join(the_folder, "LocStickers_2021.xlsx")
        the_file_2022 = os.path.join(the_folder, "LocStickers_2022.xlsx")
        email.attach_file(the_file_2021)
        email.attach_file(the_file_2022)
        email.send(fail_silently=False)

    def old_handle(self, *args, **options):
        subject = "Test Email"
        message = "Sample Message-2"
        from_email = "parkadmin@fpip.com"
        to_email = ['rolanvc@gmail.com']
        try:
            send_mail(subject, message, None, to_email, fail_silently=False)
        except SMTPException as e:
            print(str(e))
