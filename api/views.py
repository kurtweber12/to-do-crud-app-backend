from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.serializers import TaskSerializer
from todoapp.models import Task
import datetime

# Create your views here.
class TasksView(APIView):
    def get(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskView(APIView):
    def single_task(self, id_arg):
        try:
            queryset = Task.objects.get(id=id_arg)
            return queryset
        except:
            return None
        
    def get(self, request, id_arg):
        task = self.single_task(id_arg)
        serialzer = TaskSerializer(task)
        return Response(serialzer.data)

    def put(self, request, id_arg):
        task = self.single_task(id_arg)
        task.name = request.data.get("name")
        task.date_updated = datetime.date.today()
        # data_to_change = { "name": request.data.get("name"), "date_updated": datetime.date.today()}
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_arg):
        task = self.single_task(id_arg)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NewTaskView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)