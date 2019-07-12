from django.conf.urls import url
from first_app import views

urlpatterns = [
        url(r'^$',views.main,name='main'),
        url(r'index/',views.index,name='index'),
        url(r'help/',views.help,name='help')
]