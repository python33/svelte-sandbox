from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone

from .models import Test, Attempt, Answer
from .forms import AnswerForm
from .utils import get_test_and_attempt, get_current_question


def tests_list(request):
    context = {
        'tests': Test.objects.filter(published=True)
    }
    return render(request, 'knowledge_control/tests-list.html', context)


def attempt_test(request, test_id):
    test, attempt = get_test_and_attempt(test_id, request.user)
    question = get_current_question(test, attempt)

    context = {
        'test': test,
        'attempt': attempt,
        'question': question,
    }

    return render(request, 'knowledge_control/attempt-test.html', context)


def answer_question(request, test_id):
    test, attempt = get_test_and_attempt(test_id, request.user)
    question = get_current_question(test, attempt)

    answer = Answer(
        attempt=attempt,
        user=request.user,
        question=question,
    )

    form = AnswerForm(data=request.POST, instance=answer)

    if not form.is_valid():
        raise Exception(form.errors)

    form.save()

    redirect_url = reverse('knowledge_control:attempt', args=[test.id])
    return redirect(redirect_url)


def finish_test(request, test_id, attempt_id):
    test = get_object_or_404(Test, pk=test_id)
    attempt = get_object_or_404(Attempt, pk=attempt_id, test=test)

    if attempt.finished_at is None:
        attempt.finished_at = timezone.now()
        attempt.save(update_fields=['finished_at'])

    result = {
        'correct_answers': len([
            1
            for row in
            attempt.answer_set.all() if row.is_correct()
        ]),
        'total_questions': test.questions.count()
    }
    result['grade'] = round(result['correct_answers'] / result['total_questions'] * 10)

    context = {
        'test': test,
        'attempt': attempt,
        'result': result,
    }

    return render(request, 'knowledge_control/finish-test.html', context)
