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
            _cookie_contents=request.META.get('HTTP_COOKIE').replace(';','').split(' ')
            _tokens={}
            for i in _cookie_contents:
                _contents=i.split('=')
                if _contents[0]=='access_token':
                    _tokens['access_token']=_contents[1]
                elif _contents[0]=='refresh_token':
                    _tokens['refresh_token']=_contents[1]

            if _tokens.get('access_token') or _tokens.get('refresh_token'):
                return _tokens
            else:      
               return False
        except Exception as e:
            print(e)
            return False
        
    def _notadmin(self,request):
        if "admin" in str(request.path).split("/"):
            return False
        return True
    

    def __call__(self, request):
        if self._notadmin(request):
            loc=self.get_exact_loc(request=request)
            if loc:
                _tokens=self.hasToken(request=request)
                if not _tokens:
                    return JsonResponse({'message': 'no token found!',"timestamp":datetime.timestamp(datetime.now())}, status=403)
                else:
                    stat=TokenValidity().validate(request=request,tokens=_tokens)
                    if not stat:
                        return Response({'message': 'unauthorized!'}, status=403,request=request)
        
        response = self.get_response(request)
        #print(response.data) return api reqturned data
        return response