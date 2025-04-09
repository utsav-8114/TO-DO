from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Task
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@api_view(["POST"])
@permission_classes([IsAuthenticated])

def add_task(request):#first we take the json response and dump it into python dict and then we did what we want to do
    data= json.loads(request.body.decode('utf-8'))
    title = data.get("title")
    description = data.get("description")
    user = request.user
    created_user  = data.get("timestamp")
    remind_user  = data.get("reminder_time")
    Task.objects.create(
        title=title,
        description=description,
        user=user,
        timestamp= created_user,
        reminder_time = remind_user,
    )
    return JsonResponse({"message":"task was added sucessfully!"})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_tasks(request): 
    
    user=request.user
    data = Task.objects.filter(user=user)
    tasks=[]
    for i in data:
        task_dict= {
            "id" : i.id,
            "title": i.title,
            "description" : i.description
        }
        tasks.append(task_dict)
        
    return JsonResponse(tasks,safe=False)#added safe because to return list we use safe=false and if we returned dict by default it is safe=true


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_task(request,task_id):
    
    try:
        
        task = Task.objects.get(id = task_id)

        if task.user != request.user:
            return JsonResponse({"error":"authentication error not allowed!"},status=403)
        else:
            task.delete()
            return JsonResponse({"message","task deleted successfully"},safe=False,status=201)
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"},status = 404)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])     
def delete_all(request):
    
        
        try:
            user=request.user
            Task.objects.filter(user=user).delete()
            
            return JsonResponse({"message":"All tasks deleted sucessfully"})
        except Task.DoesNotExist:
            return JsonResponse({"error": "Table is empty"},status = 404)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def mark_as_completed(request,task_id):
        
        task = Task.objects.get(id= task_id)
        if task.user == request.user:
             if not task.marked:
                task.marked = True
                task.save()
        return JsonResponse({"message": "task is completed"})
        






