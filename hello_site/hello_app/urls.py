from django.urls import path
from hello_app.views import HelloWorldView, HelloView


urlpatterns = [

    path('', HelloWorldView.as_view()),
    path('<str:name>', HelloView.as_view()  )
]
