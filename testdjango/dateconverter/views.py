from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import DateFunctionMap
from .tasks import dict_map
from rest_framework.response import Response
# Create your views here.


class DateConverterView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        input_string = request.data.get('input_string', None)
        print(input_string)
        if input_string:
            if DateFunctionMap.objects.filter(input_string=input_string).exists():
                function = DateFunctionMap.objects.get(input_string=input_string).related_function_name
                output = dict_map[function]().strftime("%m/%d/%Y")
                return Response({'output': output})

            else:
                return Response({'output': 'wrong inout'})
        else:
            return Response({'output': 'wrong inout'})

