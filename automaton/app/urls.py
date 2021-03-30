from django.urls import path
from .views import *
urlpatterns = [
    path('home', home,  name='home'),
    # path('submit_data', submit_data, name='submit_data'),
    path('associate', associate, name='associate'),
    path('manager', manager, name='manager'),
    path('ajax/submit_data/', submit_data, name='submit_data'),
    path('ajax/manager/', manager, name='manager'),
]
