from rest_framework import views
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from exampleApp.firebase import auth, db as firestore
from exampleApp.validators import validate_register
import re


class CsrfExemptMixin:
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CsrfExemptMixin, views.APIView):
    def post(self, request):
        data = request.data
        try:
            validate_register(data)

            name = data.get("name")
            last_name = data.get("last_name")
            phone = data.get("phone")
            email = data.get("email")
            password = data.get("password")

            user = auth.create_user_with_email_and_password(email, password)
            firestore.collection(u'users').document(user['localId']).set({
                u'name': name,
                u'last_name': last_name,
                u'email': email,
                u'phone': phone,
                u'uid': user['localId'],
            })
            return Response({"message": "User created successfully, \n your token is {}.".format(user['idToken'])}, status=201)
        except Exception as e:
            match = re.search(r'"message": "(.*?)"', str(e))
            error_message = match.group(1) if match else str(e)
            return Response({"error": error_message}, status=400)


class LoginView(CsrfExemptMixin, views.APIView):
    def post(self, request):
        data = request.data
        try:
            email = data.get("email")
            password = data.get("password")

            user = auth.sign_in_with_email_and_password(email, password)
            return Response({"message": "Login succesfully", "token": user['idToken']}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
