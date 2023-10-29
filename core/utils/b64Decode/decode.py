import base64

class Decode:

    @staticmethod
    def decodes(b64)->dict:
        try:
            if len(b64.split(','))>1:
                return base64.b64decode(b64.split(',')[1])
            else:
                return base64.b64decode(b64)
        except Exception as e:
            raise Exception(str(e))