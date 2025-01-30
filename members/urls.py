from django.urls import path
from members import views

urlpatterns = [
    path('nasa_json/', views.fetch_json_from_s3, name='nasa_json'),
]
