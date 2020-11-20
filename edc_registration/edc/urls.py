from django.conf.urls import url, include
from django.urls import path, re_path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from edc.register.views import register_user, select_dataset, thanks

urlpatterns = (
 
    path('register/', select_dataset),
    re_path(r'^register/user/(?P<datasetid>\d+)', register_user),
    
    path('register/thanks/', thanks),
    
    # Uncomment the admin/doc line below to enable admin documentation:
 #    path('admin/doc/',  django.contrib.admindocs.urls),

    # Uncomment the next line to enable the admin:
     path('admin/', admin.site.urls),
     
     path('captcha/', include('captcha.urls')),
     
)
