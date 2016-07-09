# from django.core.management import BaseCommand
#
# class Command(BaseCommand):
#     # Show this when the user types help
#
#
#     # A command must define handle()
#     def handle(self, *args, **options):
#         self.stdout.write("Doing All The Things!")

# get an access code https://instagram.com/oauth/authorize/?client_id=d3e64ab0dbf447dba162d7e8c30105c7&redirect_uri=http://www.ljfui.com&response_type=token
from geopy.geocoders import Nominatim
# from geopy.geocoders import GoogleV3
from results.models import *
from urllib2 import *
import ast
from django.core.management.base import NoArgsCommand
import json
from hub3.test_run import *
from django.core.mail import send_mail
from hub3.views import *

class Command(NoArgsCommand):
    help = "Describe the Command Here"
    def handle_noargs(self, **options):


        while True:
            try:
                like_stuff_on_pinterest()

            except Exception as e:
                print '[error]'
                print e
