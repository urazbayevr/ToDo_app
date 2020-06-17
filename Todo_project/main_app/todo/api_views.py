import logging

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .serializers import TaskSerializer
from .celery_email import Mailer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.tasks.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def execute(self, request, pk=True):
        queryset = self.get_queryset()
        task = get_object_or_404(queryset, pk=pk)
        task.done = True
        task.save()
        try:
            mail = Mailer()
            print(request)
            mail.send_email(recipient='John.White@gmail.com',
                            subject='Geography topic',
                            body='someone hunted a rare animal')
            mail.close()
        except Exception as e:
            logging.error(e)

        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
