from django.urls import path
from . import api

urlpatterns = [
    path("tests/", api.TestListView.as_view()),
    path("tests/<int:id>/", api.TestDetailView.as_view()),
]
