from django.urls import path
from . import views

urlpatterns = [
    path('', 				views.home ,			name='home'),
    path('trading/', 		views.trading ,			name='trading'),
    path('my_companies', 	views.mycompanies ,		name='mycompanies'),
]
