from datetimewidget.widgets import DateTimeWidget

from datetime import datetime
from re import *
import json
import ast
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from simple_salesforce import Salesforce
from django import forms
from django.shortcuts import render, get_object_or_404,redirect
from random import randint
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from django.views.generic.edit import UpdateView, CreateView
from results.models import *
from django.views.generic.list import ListView

class IncidentForm(ModelForm):

    class Meta:
        model = auctions
        fields = ['How_many_for_reservation',
                    'what_day',
                    'food_ordered',
                    'email_address',
                    'price_paid']
        widgets = {
        'what_day': DateTimeWidget(attrs = {'id':'id_what_day'}, bootstrap_version=3, usel10n=True)
}
        # widgets = {'what_tiem': forms.DateInput(attrs={'class': 'datepicker', 'id': 'my_date'})}


    def __init__(self, *args, **kwargs):
        # user = kwargs.pop('pk')
        # bids = kwargs.pop('bids')
        self.what_day = forms.DateField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
        super(IncidentForm, self).__init__(*args, **kwargs)



    def clean(self,**kwargs):

        cleaned_data = super(IncidentForm, self).clean()

        # field_1 = cleaned_data.get('current_price')


        return cleaned_data



class ProfileView(ListView):
    model = auctions
    template_name = 'profile.html'



def end(request,name):
    if request.user.is_superuser:
        print '[name]'
        print name
        k = auctions.objects.get(pk=name)
        if k.is_live:
            k.is_live = False
        else:
            k.is_live = True


        k.save()
        return redirect('list')


class updateview(LoginRequiredMixin,UpdateView):
    template_name = 'create.html'

    model = auctions
    fields = ['How_many_for_reservation',
                'what_day',
                'food_ordered',
                'email_address',
                'price_paid'

                ]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super(createview, self).form_valid(form)
    def form_valid(self, form):


        self.object = form.save()
        return super(updateview, self).form_valid(form)



class createview(LoginRequiredMixin, CreateView):
    template_name = 'create.html'

    model = auctions
    fields = ['How_many_for_reservation',
                'what_day',
                'food_ordered',
                'email_address',
                'price_paid'

                ]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super(createview, self).form_valid(form)


class detailview(DetailView):

    template_name = 'detail.html'


    def get_context_data(self, **kwargs):
        data = super(detailview, self).get_context_data(**kwargs)
        price = auctions.objects.get(pk=self.kwargs['pk'])
        # data['current_price'] = price.current_price
        print ' '
        print ' '
        karen = []
        # print '[print breakdown of json object]'
        # kevin = findall('!(.*?)!',price.bids)
        # for ab in range(0,len(kevin)):
        #
        #
        #     kevin[ab] = findall('~(.*?)~',kevin[ab])
        #
        #
        # data['bids'] = kevin
        # self.request.session['current_price'] = data['current_price']

        return data

    def get_object(self):

        return auctions.objects.get(pk=self.kwargs['pk'])


class deleteview(SuperuserRequiredMixin,DeleteView):
    template_name = 'delete.html'
    model = auctions

    def get_success_url(self):
        return reverse('list')



class startingpage(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        data = super(startingpage, self).get_context_data(**kwargs)
        print  '[text]'
        data['kevina'] = auctions.objects.all()

        return data


class listview(ListView):
    queryset = auctions.objects.all()
    template_name = 'list.html'




def logout(request):
    logout(request)

def success_registration(request):

    return render(request, "success_registration.html")

def about_us(request):
    return render(request, "about_us.html")

def writer(request, name):
    namea = name + '.html'
    return render(request, namea)

def analytics(request):

    k = auctions.objects.all()



    total_sales = sum([f.price_paid for f in k])
    l = [f.price_paid for f in k]


    avg_per_customer = sum(l) / float(len(l))
    number_of_sale = len(l)
    print '[ number of sales ]'
    print number_of_sale
    food_choices = [f.food_ordered for f in k]

    return render(request, 'analytics.html', {'total_sales':total_sales,'avg_per_customer':avg_per_customer,'number_of_sale':number_of_sale,'food_choices':food_choices}    )
