import threading

class Thread(threading.Thread):

    def __init__(self,callable,args):
        self.callable=callable
        self.args = args
        threading.Thread.__init__(self,daemon=True)

    def run(self) -> None:
        try:
            if self.args:
                self.callable(self.args)
            else:
                self.callable()
        except Exception as e:
            print(e)