from django.urls import path
from . import views

urlpatterns = [
    # api/shows will be routed to the ShowList view for handling
    path('api/shows', views.ShowList.as_view(), name='show_list'),
    # api/shows will be routed to the ShowDetail view for handling
    path('api/shows/<int:pk>', views.ShowDetail.as_view(), name='show_detail'), 
]
