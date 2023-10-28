from core.utils.jwt.jwt_builder import JwtBuilder
from apps.auths.models.user import User

class TokenValidity:

    def _is_tokenValid(self,token)->tuple:
        try:
            res=JwtBuilder(token=token).decode()
            if res.get('sub'):
                return (True,res.get('sub'))
            return (False,"")
        except:
            return (False,"")

    def validate(self,request)->bool:
        try:
            _cookie_array=request.META.get('HTTP_COOKIE').split(';')
            _access_token=_cookie_array[0].split('=')[1]
            _refresh_token=_cookie_array[1].split('=')[1]

            _access_token_stat=self._is_tokenValid(_access_token)
            if _access_token_stat:
                setattr(request,'User',User.objects.get(username=_access_token_stat[1]))
                return True
            else:
                 _refresh_token_stat=self._is_tokenValid(_refresh_token)
                 if _refresh_token_stat:
                    user=User.objects.get(username=_access_token_stat[1])
                    setattr(request,'User',user)
                    _login={
                        "login":True,
                        "sub":user.username
                    }
                    request.META={**request.META,**_login}
                    return True
    
                 else:
                    _logout={
                        "logout":True
                    }
                    request.META={**request.META,**_logout}
                    return False

        except Exception as e:
            print(e)