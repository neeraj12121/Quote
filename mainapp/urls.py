from django.conf.urls import url,include
from mainapp.views import hello
urlpatterns = [
    url(r'^', hello),    
]

