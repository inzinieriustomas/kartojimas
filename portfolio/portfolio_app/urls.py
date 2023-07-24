from django.urls import path
from portfolio_app.views import project_view
from . import views

urlpatterns = [

    path('', views.home_view, name='home'),
    path('project/',views.project_view, name='project'),
    path('contacts/', views.contacts_view, name='contacts'),
]