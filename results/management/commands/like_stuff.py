from geopy.geocoders import Nominatim


from results.models import *
from urllib2 import *
import ast
from django.core.management.base import NoArgsCommand
import json

from django.core.mail import send_mail
from hub3.views import *

class Command(NoArgsCommand):
    help = "Describe the Command Here"
    def handle_noargs(self, **options):


        while True:
            try:
                like_stuff('random')

            except Exception as e:
                print '[error at python command]'
                print e
