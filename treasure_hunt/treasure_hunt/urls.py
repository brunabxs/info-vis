from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from treasure_hunt.views.login import login, home, user_logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'treasure_hunt.views.home', name='home'),
    # url(r'^treasure_hunt/', include('treasure_hunt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
  url(r'^home/', home),
  url(r'^login/$', login),
  url(r'^logout/$', user_logout),
)