from rest_framework import generics
from core.models import Message
from .serializers import MessageSerializer
from .permissions import Pub



# Create your views here.
class Postlistview(generics.ListAPIView):
    queryset = Message.message_objects.all()
    serializer_class = MessageSerializer


class PostDetailview(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class PostCreateview(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [Pub]



class PostManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [Pub]

