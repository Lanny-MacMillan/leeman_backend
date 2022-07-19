from rest_framework import serializers 
from .models import Show 

class ShowSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        # tell django which model to use
        model = Show
        # tell django which fields to include
        fields = ('id', 'venue', 'date', 'time', 'description', 'image', 'location', 'coverPrice', 'other',)
