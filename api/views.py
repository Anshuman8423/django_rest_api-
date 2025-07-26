from rest_framework import viewsets, filters
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['course']
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'email']
