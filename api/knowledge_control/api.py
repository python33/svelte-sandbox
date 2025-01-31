from rest_framework import generics

from knowledge_control import models, serializers


class DisciplineListView(generics.ListAPIView):
    serializer_class = serializers.DisciplineSerializer

    def get_queryset(self):
        return models.Discipline.objects.filter(published=True)


class TestListView(generics.ListAPIView):
    serializer_class = serializers.TestSerializer

    def get_queryset(self):
        return models.Test.objects.filter(published=True)


class TestDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.TestDetailSerializer

    def get_queryset(self):
        return models.Test.objects.filter(published=True)

    def get_object(self):
        queryset = self.get_queryset()
        return queryset.get(pk=self.kwargs['id'])
