from django.conf.urls import patterns, url, include
from care import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^situation_response/', views.situation, name='situation'),
        url(r'^webform/', views.webform, name='webform'),

        # ADD THIS NEW TUPLE!
)
