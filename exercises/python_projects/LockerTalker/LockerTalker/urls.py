from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^index$','prototype.views.index', name= 'home' ),#index
    url(r'^main$','prototype.views.main', name = 'main')#main - feed_page/main
    # url()#settings/edit edit settings
    # url()#settings view settings
    # url()#favorite/NEWS_ITEM_ID
    # url()#block/NEWS_ITEM_IDs
    #      #more/NEWS_SOURCE_ID
         #less/NEWS_SOURCE_ID
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^poll/(?P<poll_id>\d+)$', 'polls.views.poll'),
    # url(r'^poll/results/(?P<poll_id>\d+)$', 'polls.views.poll_results', name='results')

    # url(r'^LockerTalker/', include('LockerTalker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:


    # Uncomment the next line to enable the admin:

)
