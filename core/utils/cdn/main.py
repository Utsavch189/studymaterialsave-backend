import cloudinary
import cloudinary.uploader
import cloudinary.api
from ..b64Decode.decode import Decode

class CDN:
    def __init__(self) -> None:
        try:
            cloudinary.config(
                cloud_name="dcf6uk047",
                api_key="176572318442856",
                api_secret="C0hg2pOkd-7MoOdoeXLcF-RMHTk",
                secure=True,
            )
            self._decode=Decode()
        except Exception as e:
            raise Exception(str(e))
    
    def upload(self,source:str,destination:str,resource_type:str='auto')->dict:
        try:
            res=cloudinary.uploader.upload(
                self._decode.decodes(source),
                use_filename=True,
                unique_filename=False,
                resource_type=resource_type,
                public_id=destination
            )
            return res
        except Exception as e:
            raise Exception(str(e))
    
    def delete(self,public_ids:str,resource_type:str,type:str):
        try:
            cloudinary.api.delete_resources(public_ids, resource_type=resource_type, type=type)
        except Exception as e:
            raise Exception(str(e))