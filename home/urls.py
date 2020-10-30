from django.urls import path
from . import views

urlpatterns = [
    path('companies/<int:pg>/',                 views.company,              name='home'),
    # path('',                        views.coming,           name='comingsoon'),
    path('',                        views.home,         name='newpage'),
    # path('trading/',              views.trading_closed,   name='trading'),
    path('trade/begin/',            views.alert_update,     name='trade-begin'),
    path('trade/<int:pg>/',         views.tradingUpdateView,name='trading'),
    path('trading/<int:id>/<int:pg>/',views.tradingUpdateView,name='trading-update'),
    path('bid/<int:pg>/',           views.bidding,          name='bidding'),
    #path('bidding/',               views.comingbidding ,   name='bidding'),
    path('bidding/<int:id>/<int:pg>/',views.bidding,        name='bidding-update'),
    path('my-companies/',           views.mycompanies,      name='mycompanies'),
    path('my-companies/<int:id>/',    views.mycompanies,      name='mycompanies'),
    # path('my-companies/no-trade/',  views.mycompanies_notrade,name='notrade'),
    path('my-companies/add/',       views.add_mycompanies,  name='add-mycompanies'),
    path('my-trades/',              views.mytrade ,         name='mytrade'),
    path('my-bid/',                 views.mybid ,           name='mybids'),
    path('trade/close/<int:id>/',   views.tradingCloseView, name='close-trade'),
    path('time/',                   views.time,             name='time'),
    path('timepage/',               views.timepage,         name='timepage'),
]
