from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import Test, Attempt


def get_test_and_attempt(test_id, user):
    test = get_object_or_404(Test, pk=test_id)

    attempt, _ = Attempt.objects.get_or_create(
        test=test,
        user=user,
        finished_at__isnull=True,
    )

    return test, attempt


def get_current_question(test, attempt):
    return test.questions.filter(
        ~Q(id__in=attempt.answer_set.values_list('question_id'))
    ).first()
