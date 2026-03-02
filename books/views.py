from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

# Create your views here.


# class BookListApiView(generics.ListAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer

class BookListApiView(APIView):

    def get(self, request):
        books=Book.objects.all()
        print(books)
        serializer_data=BookSerializer(books, many=True).data
        data={

            'status':"returned books",
            "books":serializer_data
        }
        return Response(data)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer

class BookDetailApiView(APIView):
    
    def get(self, request, pk):
        try:
            book=Book.objects.get(id=pk)
            serializer_data=BookSerializer(book).data
            return Response({
                "status":'muvaffaqiyatli',
                "book": serializer_data
            })
        except Exception:
            return Response(
                {
                "status":'false',
                "message": 'kitob topilmadi'
            }
            )
class BookDeleteApiView(generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book=Book.objects.get_object_or_404(id=pk)
            book.delete()
            return Response({
                "status":True,
                "message": "kitob o'chirildi."
            })
        except Exception:
            return Response({
                "status":False,
                "message": "kitob topilmadi"
            })


class BookUpdateApiView(APIView):
    serializer_class = BookSerializer
    def put(self, request, pk):
        book=get_object_or_404(Book.objects.all(), id=pk)
        # data=request.data
        serializer=BookSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {
                "status":True,
                "message":" muvaffaqiyatli o'zgartirildi.",
                "data": serializer.data
            }
        )

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer



# class BookCreateApiView(generics.CreateAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer

class BookCreateApiView(APIView):
    # serializer_class=BookSerializer
    def post (self, request):# request.user
        data=request.data
        serializer=BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            data={
                'status':"kitoblar bazaga saqlandi",
                "books":data

            }
            return Response(data)
        
        else:
            return Response(serializer.errors)

class BookViewSet(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer








