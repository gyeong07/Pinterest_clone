from django.urls import path
from accountapp.views import hello_world

app_name="accountapp" # 주소를 간편하게 하기 위함

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]