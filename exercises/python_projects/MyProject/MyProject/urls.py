from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyProject.views.home', name='home'),
    # url(r'^MyProject/', include('MyProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

    # Uncomment the next line to enable the admin:
    # url(r'^$', 'MyApp.views.home'),
    # url(r'^hello/(?P<name>[a-zA-Z]+)','MyApp.views.say_hello'),
    # url(r'^counter$','MyApp.views.counter'),
    # url(r'^blackjack/$','MyApp.views.game'),
    # url(r'^hello1/(?P<name>[a-zA-Z]+)?','MyApp.views.hello')
    # url(r'^card$','MyApp.views.cards')
    url(r'^poll/(?P<poll_id>\d+)$', 'polls.views.poll'),
    url(r'^poll/results/(?P<poll_id>\d+)$', 'polls.views.poll_results', name='results'),
    url(r'^add-poll-answer$', 'polls.views.add_poll_answer', name='add_answer'),
    url(r'^add-poll$', 'polls.views.add_poll', name='add_poll'),
    url(r"^admin/latest-poll$", "polls.views.latest_poll"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^sampleform', 'polls.views.sample_form'),
    url(r'^loginform', 'polls.views.login_form')

    # url(r'^radio-poll/(?P<poll_id>\d+)$', 'polls.views.radio_poll', name='radio_add')
)
