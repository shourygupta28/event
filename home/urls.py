from django.urls import path
from . import views

urlpatterns = [
    path('companies/', 				views.home ,			name='home'),
    path('', 	views.coming ,			name='comingsoon'),
    path('trading/', 		views.tradingUpdateView,name='trading'),
    path('trading/<int:id>/',views.tradingUpdateView,name='trading-update'),
    path('bidding/', 		views.bidding ,			name='bidding'),
    path('bidding/<int:id>',views.bidding ,			name='bidding-update'),
    path('my_companies/', 	views.mycompanies ,		name='mycompanies'),
]
