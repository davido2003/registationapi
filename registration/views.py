from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . serializers import SignupSerializer, loginSerializer
from . models import SignUp, login
# Create your views here.

class SignupAPIView(generics.GenericAPIView, mixins.CreateModelMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = SignupSerializer
    queryset = SignUp.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def  get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self,request,id=None):
        return self.create(request,id)
    def put(self,request):
        return self.update(request,id)
    def delete(self,request,id):
        return self.destroy(request,id)

class loginAPIView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = loginSerializer
    queryset = login.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def  get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self,request,id=None):
        return self.create(request,id)
    def put(self,request):
        return self.update(request,id)
    def delete(self,request,id):
        return self.destroy(request,id)
