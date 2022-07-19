from rest_framework import generics
from .serializers import ShowSerializer
from .models import Show

class ShowList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Show.objects.all().order_by('id')
    # tell django what serializer to use
    serializer_class = ShowSerializer 
class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all().order_by('id')
    serializer_class = ShowSerializer
