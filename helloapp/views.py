from re import L
from django.views import View
from django.http import HttpResponse

class HelloView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello docker. Please don`t bite me T_T')
