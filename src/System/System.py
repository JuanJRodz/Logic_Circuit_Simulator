class AND:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, *args):
        
        list_inputs = args
        
        for i in range(len(list_inputs)):
            if list_inputs[i] == 0:
                return 0
        return 1

class CONST:
    def __init__(self, name, constant):
        
        self.name = name
        self.constant = constant
     
    #Function that outputs the constant given
    def function(self):
        return self.constant 


class System:
    def __init__(self, dictionary, itirations):
        
        self.dictionary = dictionary 
        self.connections = connections 
        
    def System(self, dictionary, connections):
        
        for key in dictionary:
            
            print(key.function)
        
    
a = CONST("Entrada", 1)   
b = CONST("Señal", 0)
c = AND("AND1")
    
connection_dict= {a: [], b: [], c:[a,b]}
for key, value in connection_dict.items:
    
    x = key.function(value)      
    
    print(x)
    