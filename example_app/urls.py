from django.urls import path

from example_app.views import example, example_2

urlpatterns = [
    path("", example, name="root"),
    path("example-2", example_2, name="example_2")
]
