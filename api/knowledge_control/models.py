from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title or 'New Test'


class Question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(
        Test,
        related_name='questions',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.text or 'New question'


class Option(models.Model):
    text = models.TextField()
    correct = models.BooleanField()
    question = models.ForeignKey(
        Question,
        related_name='options',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text or 'New option'


class Attempt(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)

    def is_finished(self):
        return self.test.questions.count() == self.answer_set.count()


class Answer(models.Model):
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    selected_options = models.ManyToManyField(Option)

    class Meta:
        unique_together = [
            ['attempt', 'user', 'question']
        ]

    def is_correct(self):
        incorrect_answers = self.selected_options.filter(correct=False).count()

        if incorrect_answers > 0:
            return False

        correct_answers = self.selected_options.filter(correct=True).count()
        correct_options = self.question.option_set.filter(correct=True).count()

        return correct_answers == correct_options
