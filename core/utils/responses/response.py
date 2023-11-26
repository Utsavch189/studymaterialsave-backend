from rest_framework.response import Response
from datetime import datetime
from ..jwt.jwt_builder import JwtBuilder

class Response(Response):

    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None,request=None):
        _data={**data,"timestamp":datetime.timestamp(datetime.now())}
        #print(request.META)
        _resp=super()
        
        if request!=None and request.META.get('login'):
            tokens=JwtBuilder(payload={
               "sub":request.META.get('sub')
           },access_token_exp=10,refresh_token_exp=25).get_token()

            _data={**_data,"login":"true","access_token_exp":tokens[0]['access_token_exp'],"refresh_token_exp":tokens[1]['refresh_token_exp']}
            _resp.__init__(_data, status, template_name, headers, exception, content_type)
            _resp.set_cookie(key='access_token',value=tokens[0]['access_token'],httponly=True,secure=True,max_age=tokens[0]['max_age'])
            _resp.set_cookie(key='refresh_token',value=tokens[1]['refresh_token'],httponly=True,secure=True,max_age=tokens[1]['max_age'])

        elif request!=None and request.META.get('logout'):
            _data={**_data,"logout":"true"}
            _resp.__init__(_data, status, template_name, headers, exception, content_type)
            _resp.delete_cookie(key='access_token')
            _resp.delete_cookie(key='refresh_token')
        
        else:
            _resp.__init__(_data, status, template_name, headers, exception, content_type)
        
    
   