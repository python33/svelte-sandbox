from django.urls import path, include

from . import views

app_name = 'knowledge_control'

urlpatterns = [
    path("", views.tests_list, name="list"),
    path("<int:test_id>/attempt/", views.attempt_test, name="attempt"),
    path("<int:test_id>/attempt/answer/", views.answer_question, name="answer"),
    path("<int:test_id>/attempt/<int:attempt_id>/finish/", views.finish_test, name="finish"),
    # API urls
    path("api/", include("knowledge_control.api_urls")),
]
