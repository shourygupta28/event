from django.urls import path
from . import views

urlpatterns = [
    path('companies/', 			    views.home ,			name='home'),
    path('', 	                    views.coming ,			name='comingsoon'),
    # path('trading/',                views.trading_closed,name='trading'),
    path('trading/', 		        views.tradingUpdateView,name='trading'),
    path('trading/<int:id>/',       views.tradingUpdateView,name='trading-update'),
    path('bidding/', 		        views.bidding ,			name='bidding'),
    #path('bidding/', 		views.comingbidding ,			name='bidding'),
    path('bidding/<int:id>/',       views.bidding ,			name='bidding-update'),
    path('my-companies/',           views.mycompanies ,     name='mycompanies'),
    path('my-companies/<int:id>/', 	        views.mycompanies ,		name='mycompanies'),
    path('homepage/',                views.newpage,          name='newpage'),
    path('my-trades/', 	            views.mytrade ,		    name='mytrade'),
    path('trade/close/<int:id>/',   views.tradingCloseView, name='close-trade'),

    path('time/', views.time,   name='time'),
    path('timepage/', views.timepage,	name='timepage'),
]
