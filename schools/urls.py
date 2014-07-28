from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'schools.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'attendance.views.profile', name='profile'),
    url(r'^register/$', 'attendance.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^profile/$', 'attendance.views.profile', name='profile'),
    url(r'^classrooms/new/$', 'attendance.views.new_classroom', name='new_classroom'),
    url(r'^classrooms/(?P<classroom_id>\w+)/$', 'attendance.views.view_classroom', name='view_classroom'),
    url(r'^students/new/$', 'attendance.views.new_student', name='new_student'),
    url(r'^students/(?P<student_id>\w+)/$', 'attendance.views.view_student', name='view_student'),
    url(r'^take_attendance/(?P<classroom_id>\w+)/$', 'attendance.views.take_attendance', name='take_attendance'),





    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)

