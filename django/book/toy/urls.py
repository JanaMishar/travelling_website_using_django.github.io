from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('registration',views.registration),
    path('reg',views.reg),
    path('show',views.show),
    path('del/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('edcode/<int:id>',views.edcode),
    path('signin',views.login),
    path('logcode',views.logcode),
    
    path('signup',views.form),
    path('indexhome',views.indexhome),
    path('insert',views.registration),

    # 2nd
    path('registrations',views.registrations),
    path('shows',views.shows),
    path('regs',views.regs),

    # places
    # path('international',views.international),


    # crud
    path('dels/<int:id>',views.deletes),
    path('edits/<int:id>',views.edits),
    path('edcodes/<int:id>',views.edcodes),
    path('inserts',views.registrations),


    # 3rd
    path('outbooked',views.output),

    path('booked',views.booked),


    # 
    
    path('admina',views.test),
    path('adpow',views.admina),
    path('trip',views.trip),
    path('indian',views.indian),
    path('international',views.international),
    
    

    

    

]