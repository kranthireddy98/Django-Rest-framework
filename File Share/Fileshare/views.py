from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileListSerializer
from rest_framework.parsers import MultiPartParser

def home(request):
    return render(request,'home.html')

def download(request,uid):
    return render(request,'download.html',context={'uid':uid})

class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            data = request.data
            print(data)

            serializer = FileListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                print("hhh")
                return Response({
                    'status' : 200,
                    'message':'files uploaded successfully',
                    'data':serializer.data
                })
            else:
                return Response({
                'status' : 400,
                    'message':'files not uploaded successfully',
                    'data':serializer.errors
            })
        except Exception as e :
            print(e)
            return Response({"seer":str(e)})