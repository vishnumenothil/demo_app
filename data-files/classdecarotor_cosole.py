from time import sleep
def filter_message(pattern):
    def _filter_message(cls):
        org_log=getattr(cls,'log')
        def new_log(self,message):
            if pattern in message:
               org_log(self,message)
        setattr(cls,"log",new_log)
        return cls
        
    return _filter_message




@filter_message('INFO')
class ConsoleLog():
    textlist=[]
    def log(self,message):
        message=message.strip()
        if message:
           ConsoleLog. textlist.append(message)
           print(ConsoleLog.text)

@filter_message('INFO')
class textFileLogger:                          
    def __init__(self,file) -> None:
        self.file=file
    
    def log(self,message):
        message=message.strip()
        if message:
            self.file.write(message)
            self.file.write("\n")
            self.file.flush()
    
# c1=ConsoleLog()
# c1.log("      vidgdsuhundsnkjsh")
# print(ConsoleLog.__dict__)

with open("data-files/sample.log","r" )as f:
   
    with open("data-files/info.txt",'w') as wf:
        t=textFileLogger(wf)
        for line in f:
            t.log(line)


