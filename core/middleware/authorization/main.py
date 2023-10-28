import json
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime
from core.utils.responses.response import Response
import os
from .tokenValid import TokenValidity

middleware_json=os.path.join(settings.BASE_DIR,'middleware.json')

class Authorization:
    def __init__(self, get_response):
        self.get_response = get_response
        with open(middleware_json, "r") as read_file:
            self._register_paths:dict=json.load(read_file)
    
    def get_exact_loc(self,request:object)->dict:
        incoming_req_path=str(request.path).split("/")
        all_registered_paths=self._register_paths['paths']
        for path in all_registered_paths:
            if path['endpoint'] in incoming_req_path:
                return path
    
    def hasToken(self,request):
        try:
            if 'access_token' in request.META.get('HTTP_COOKIE').replace(';','').split(' ')[0].split('=') and 'refresh_token' in request.META.get('HTTP_COOKIE').replace(';','').split(' ')[1].split('='):
                return True
            else:
               return False
        except:
            return False
        
    def _notadmin(self,request):
        if "admin" in str(request.path).split("/"):
            return False
        return True
    

    def __call__(self, request):
        if self._notadmin(request):
            loc=self.get_exact_loc(request=request)
            if loc:
                if not self.hasToken(request=request):
                    return JsonResponse({'message': 'no token found!',"timestamp":datetime.timestamp(datetime.now())}, status=403)
                else:
                    stat=TokenValidity().validate(request=request)
                    if not stat:
                        return Response({'message': 'unauthorized!'}, status=403,request=request)
        
        response = self.get_response(request)
        #print(response.data) return api reqturned data
        return response