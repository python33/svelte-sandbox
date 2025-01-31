from django.contrib import admin

from .models import Test, Question, Option, Discipline


class OptionInline(admin.TabularInline):
    model = Option


class QuestionInline(admin.TabularInline):
    model = Question
    show_change_link = True



@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['title', 'published']
    list_filter = ['published']


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'topic']
    list_filter = ['topic__discipline', 'published']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_filter = ['test']
