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
b = CONST("Señal", 1)
c = AND("AND1")
    
connection_dict= {a: [], b: [], c:[a,b]}


n = 10 

while n > 0:
    iter_dict = connection_dict                   #
    
    for key, value in iter_dict.items():
    
        v_list = []             
        print(iter_dict)
    
        if not value == None:                      #Checks arguments
            num_elem = len(value)
            for i in value:
                e = iter_dict[i] 
                v_list.append(e)   
        else: 
            v_list = None     
    
        
        x = key.function(*v_list)                  #Runs functions
        connection_dict[key] = x                   #Updates Value
    
    print('---',x,value,iter_dict,'This is an iteration') #Checks Dict
    
    n -= 1
    print (n)