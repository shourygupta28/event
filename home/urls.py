from django.urls import path
from . import views

urlpatterns = [
    path('', 				views.home ,			name='home'),
    path('comingsoon/', 	views.coming ,			name='comingsoon'),
    path('trading/', 		views.trading ,			name='trading'),
    path('bidding/', 		views.bidding ,			name='bidding'),
    path('my_companies/', 	views.mycompanies ,		name='mycompanies'),
]
