
from django.urls import path 
from . import views

urlpatterns= [
    
    
    path('api/add',views.add_task),
    path('api/tasks',views.fetch_tasks),
    path('api/delete/<int:task_id>',views.delete_task),
    path('api/delete_all/',views.delete_all),
    path('api/marked/<int:task_id>',views.mark_as_completed),
    
]