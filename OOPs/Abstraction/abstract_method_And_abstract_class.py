from abc import ABC, abstractmethod
class Senior(ABC):
    def add(self,x,y):
        print(x+y)
        
    def sub(self,x,y):
        print(x-y)   
        
    def mul(self,x,y):
        print(x*y)    
  
    @abstractmethod    
    def div(self):
        pass 
    
class Junior(Senior):
    def div(self,x,y):
        print(x/y)  
obj = Junior()     
obj.add(10,2)  
obj.sub(10,2)
obj.mul(10,2)       
obj.div(10,2)