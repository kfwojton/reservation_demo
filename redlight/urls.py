"""salesforce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'about_us', about_us),
    # url(r'^accounts/profile', admin.site.urls),
    url(r'^logout2', logout),
    url(r'^success_registration', success_registration),
    url(r'^accounts/profile/', ProfileView.as_view(), name='profile'),
    url(
    regex=r'^$',
    view=startingpage.as_view(),
    name='start'
    ),
    url(r'^a/(.*?)$',writer),
    url(
    regex=r'^list$',
    view=listview.as_view(),
    name='list'
    ),

    url(
    regex=r'^delete/(?P<pk>\d+)/$',
    view=deleteview.as_view(),
    name='delete'
    ),

    url(
    regex=r'^update/(?P<pk>\d+)/$',
    view=updateview.as_view(),
    name='update'
    ),

    url(
    regex=r'^update/(?P<pk>\d+)/$',
    view=updateview.as_view(),
    name='update'
    ),

    url(r'^end/(.*?)$',end),


    url(
    regex=r'^detail/(?P<pk>\d+)/$',
    view=detailview.as_view(),
    name='detail'
    ),


    url(
    regex=r'^create/$',
    view=createview.as_view(),
    name='create'
    ),

    url(
     regex=r'^update/(?P<pk>\d+)$',
    view=updateview.as_view(),
    name='update'
    ),
    url(r'^accounts/', include('allauth.urls')),
    ]



    #
    # url(
    # regex=r'^$',
    # view=views.CampaignListView.as_view(),
    # name='campaign_list'
    # ),
    #
    #
    # # URL pattern for the CampaignRedirectView
    # url(
    #     regex=r'^(?P<campaign_id>\d+)/$',
    #     view=views.CampaignDetailView.as_view(),
    #     name='details'
    # ),

    # URL pattern for the CampaignDetailView
    # url(
    #     # regex=r'^(?P<username>[\w.@+-]+)/$',
    #     regex=r'^(?P<pk>\d+)/$',
    #     view=views.CampaignDetailView.as_view(),
    #     name='detail'
    # ),
    #
    # url(
    #     regex=r'^update/$',
    #     view=views.CampaignUpdateView.as_view(),
    #     name='update'
    # ),
    #
    # url(
    #     regex=r'^(?P<pk>\d+)/part_update/$',
    #     view=views.CampaignPartUpdateView.as_view(),
    #     name='part_update'
    # ),
    #
    # url(
    #     regex=r'^create/$',
    #     view=views.CampaignCreateView.as_view(),
    #     name='create'
    # ),
    #
    # url(
    #     regex=r'^(?P<pk>\d+)/update/$',
    #     view=views.CampaignUpdateView.as_view(),
    #     name='update'
    # ),
    #
    # url(
    #     regex=r'^(?P<campaign_id>\d+)/formc/create/$',
    #     view=views.FormcCreateView.as_view(),
    #     name='create_formc'
    # ),
    #
    #
    #
    # url(
    #     regex=r'^(?P<campaign_id>\d+)/formc_part_update/$',
    #     view=views.FormcPartUpdateView.as_view(),
    #     name='formc_part_update'
    # ),
