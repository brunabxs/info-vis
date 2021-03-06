from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from treasure_hunt.views.login import login, home, user_logout
from treasure_hunt.views.object_tip import show_tip

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
  url(r'^home/', home),
  url(r'^login/$', login),
  url(r'^logout/$', user_logout),
  url(r'^ver_dica/(?P<id>\d+)/$', show_tip),
)
