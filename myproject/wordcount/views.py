# from django.shortcuts import render
# from wordcount.models import Blog
# from wordcount.serializer import BlogSerializer
# status에 따라 직접 Response를 처리할 것
# from django.http import Http404 # Get Object or 404 직접 구현


from django.shortcuts import render
from .models import Blog,BlogPic,BlogFile
from .serializer import BlogSerializer,BlogPicSerializer,BlogFileSerializer
from rest_framework import viewsets


from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

# from rest_framework.response import Response
# from rest_framework import status
# APIView를 상속받은 CBV


# from rest_framework.views import APIView
# from rest_framework import viewsets
# from rest_framework import renderers
# from rest_framework.decorators import action

# from django.http import HttpResponse


# Create your views here.
# def index(request):
#     return render(request,'index.html')

# class BlogList(APIView):
#     def get(self, request):
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True) # 쿼리셋 넘기기 (many=True인자)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():   # 직접 유효성 검사
#             serializer.save()       # 저장
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BlogDetail(APIView):  #각 instance 객체는 url뒤에 auto created 된 pk, id값을 붙여줌으로서 우리가 detail을 확인해 줄 수 있다.
    # get_object_or_404를 구현해주는 helper function
    # def get_object(self, pk):
    #     try:
    #         return Blog.objects.get(pk=pk)
    #     except Blog.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     blog = self.get_object(pk)
    #     # post = get_object_or_404(Post, pk)
    #     serializer = BlogSerializer(blog)
    #     return Response(serializer.data)


    # def put(self, request, pk, format=None):
    #     blog = self.get_object(pk)
    #     serializer = BlogSerializer(blog, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # def delete(self, request, pk, format=None):
    #     blog = self.get_object(pk)
    #     blog.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
        
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('id') 
    serializer_class = BlogSerializer  

    filter_backends = [SearchFilter]
    search_fields = ('title',)


    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    # def highlight(self, request, *args, **kwargs):
    #     return HttpResponse("얍")    

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs=super().get_queryset()

        if self.request.user.is_authenticated:
            qs=qs.filter(author=self.request.user)
        else:
            qs=qs.none() 
        return qs

class BlogPicViewSet(viewsets.ModelViewSet):            
    queryset = BlogPic.objects.all().order_by('id')
    serializer_class = BlogPicSerializer

class BlogFileViewSet(viewsets.ModelViewSet):
    queryset=BlogFile.objects.all().order_by('id')
    serializer_class=BlogFileSerializer

class Mypagination(PageNumberPagination):
    page_size = 100 