from django.conf.urls import url

from challenge import views

urlpatterns = [
    url(r'^run_task/$', views.run_task, name='run_task')
]
