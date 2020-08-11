from django.urls import path
from . import views

urlpatterns = [
    path('', 				views.home ,			name='home'),
    path('trading/', 		views.trading ,			name='trading'),
    path('trading/<int:id>',views.tradingUpdateView,name='trading-update'),
    path('bidding/', 		views.bidding ,			name='bidding'),
    path('my_companies/', 	views.mycompanies ,		name='mycompanies'),
]
