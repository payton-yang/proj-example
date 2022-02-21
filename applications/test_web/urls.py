from django.urls import path

from applications.test_web.views import TestView

app_name = 'test'
urlpatterns = [
    path('test', TestView.as_view())
]
