from Components.AND import AND
from Components.Constant import CONST


class System:
    def __init__(self, dictionary, connections):
        
        self.dictionary = dictionary 
        self.connections = connections 
        
    def System(self, dictionary, connections):
        
        for key in dictionary:
            
            key.function
        
    
a = CONST("Entrada", 1)   
b = CONST("Señal", 0)
c = AND("AND1")
    
connection_dict= {a: [], b: [], c:[a,b]}
