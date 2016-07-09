from __future__ import unicode_literals
from datetime import *
import django
from django.db import models
from datetime import *
import django.utils
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect

#
class auctions(models.Model):

    def get_absolute_url(self):
        return reverse('list')

    How_many_for_reservation = models.IntegerField(blank = True, null = True, default=0)
    what_day = models.DateField(default = datetime.now())
    food_ordered = models.CharField(max_length = 300, blank = False, null = True)
    email_address = models.CharField(max_length = 300, blank = False, null = True)
    price_paid = models.IntegerField(blank = True, null = True, default=0)

    # is_live = models.BooleanField(default = True)
    # bids = models.CharField(max_length = 300, blank = False, null = True, default = '')
    # # reserve_price =  models.IntegerField(default= 0, blank = False, null = True)
    # seller = models.CharField(max_length = 300, blank = False, null = True)
