from django.urls import path
from . import views
app_name = 'nlp_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_records/', views.get_records, name='get_records')

    ]