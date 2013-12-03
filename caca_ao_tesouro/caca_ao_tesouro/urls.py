from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from caca_ao_tesouro.views.login import login, home, user_logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'caca_ao_tesouro.views.home', name='home'),
    # url(r'^caca_ao_tesouro/', include('caca_ao_tesouro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
  url(r'^home/', home),
  url(r'^login/$', login),
  url(r'^logout/$', user_logout),
)
