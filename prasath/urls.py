from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('',views.child,name="home"),
    path('event', views.event, name="event"),  # Added a trailing slash for consistency
    path('staff', views.staff, name="staff"),  # Added a trailing slash for consistency
    path('contact', views.contact, name="contact"), 
    path('about', views.about, name="about"), 
    path('Developer', views.Developer, name="Developer"), 
    path('registration',views.registration_event, name="registration"),
    path('registration_payment',views.registration_payment,name="registration_payment")

    # Add other URL patterns as needed
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
