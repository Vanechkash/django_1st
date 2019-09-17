from django.urls import path
from . import views


urlpatterns = [
    path('world/', views.hello),
    path('', views.show_all),
    path('addcomment/<int:id>/', views.addcomment),
]
