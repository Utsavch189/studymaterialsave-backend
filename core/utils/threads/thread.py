import threading

class Thread(threading.Thread):

    def __init__(self,inst):
        self.inst=inst
        threading.Thread.__init__(self,daemon=True)

    def run(self) -> None:
        self.inst.sends()