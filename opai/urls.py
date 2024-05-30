from django.urls import path

from .views import uploadPPT
from opai import views
app_name = 'opai'

urlpatterns = [
    path('', views.slides),
    path('uploadPPT/', uploadPPT.as_view(), name='uploadPPT'),
    path('list-ppt/', views.ListPPT),
]
