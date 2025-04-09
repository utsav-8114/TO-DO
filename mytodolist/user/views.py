from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User



@csrf_exempt
def register(request):
    if request.method == "POST":
        data= json.loads(request.body.decode("utf-8"))
        user_name = data.get("username")
        password = data.get("password")
        email = data.get("email")

        if not user_name or not email or not password:
            return JsonResponse({"message": "please enter the details and dont keep any null spaces"})
        else:
            if User.objects.filter(username=user_name).exists() and User.objects.filter(email=email).exists():
                return JsonResponse({"error":"email or username already exists"})
            else:
                user = User.objects.create_user(username=user_name,password=password,email=email)
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                     "message":"user registered succesfully",
                     "refresh" : str(refresh),
                     "access" : str(refresh.access_token),
                     })

