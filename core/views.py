from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import CheckListSerializer
from .serializers import CheckListItemsSerializer

# Create your views here.


class TestApiViews(APIView):
    def get(self, request, format=None):
        return Response({'Name': 'Shreya Panchal'})

class ChecklistsApiViews(APIView):
    serializer_class =CheckListSerializer

    def get(self, request, format=None):
        data = CheckList.objects.all()

        serializer = self.serializer_class(data, many = True)

        serialized_data = serializer.data
        return Response(serialized_data, status= status.HTTP_202_ACCEPTED)

    def post(self, request, format=None):
        # creation code
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class to check single id of checklist
class ChecklistApiViews(APIView):
    serializer_class = CheckListSerializer

    def get_obj(self,pk):
        try:
            return CheckList.objects.get(pk = pk)
        except:
            raise Http404

    def get(self, request, pk, format = None):
        serializer = self.serializer_class(self.get_obj(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)


    def put(self,request,pk, format = None):
        checklist = self.get_obj(pk)
        serializer = self.serializer_class(checklist, data =request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk, format= None):
        checklist = self.get_obj(pk)
        checklist.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



class ChecklistItemsCreateApiViews(APIView):
    serializer_class = CheckListItemsSerializer

    def post(self, request, format=None):
        # creation code
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChecklistItemsApiViews(APIView):
    serializer_class = CheckListItemsSerializer
    def get_obj(self,pk):
        try:
            return CheckListItems.objects.get(pk = pk)
        except:
            raise Http404

    def get(self, request, pk, format = None):
        checklist_item = self.get_obj(pk)
        serializer = self.serializer_class(checklist_item)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)


    def put(self,request,pk, format = None):
        checklist_item = self.get_obj(pk)
        serializer = self.serializer_class(checklist_item, data =request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk, format= None):
        checklist_item = self.get_obj(pk)
        checklist_item.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
