from django.shortcuts import render
from .models import ProductModel
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSer

# Create your views here.
class ProductView(APIView):
    def get(self, request):
        prd_obj = ProductModel.objects.all()
        serobj = ProductSer(prd_obj, many=True)
        return Response(serobj.data)

    def post(self,request):
        serobj = ProductSer(data=request.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        prd = ProductModel.objects.get(pk=pk)
        serobj = ProductSer(prd,data=request.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        prd = ProductModel.objects.get(pk=pk)
        ser = Response(prd)
        prd.delete()
        return Response(status=status.HTTP_200_OK)

      




