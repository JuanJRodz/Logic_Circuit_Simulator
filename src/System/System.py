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
    def __init__(self, dictionary, iterations):
        
        self.dictionary = dictionary 
        self.iterations = iterations 
        
    def System(self):
        
        for key in self.dictionary:
            while n > 0:
                iter_dict = connection_dict                 # Won't run each iteration 
    
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
            
            
        
    
a = CONST("Entrada", 1)   
b = CONST("Señal", 1)
c = AND("AND1")
    
connection_dict= {a: [], b:[d ]}
#{a: [], b: [], c:[a,b]}

n = 0 
#fh = open('test.txt', 'w')

#fh.write("This text file is a simulation of the system Test\n\n --------------------------------------------------------\n")
#fh.write('\n Simulation Start\n--------------------------------------------------------\n')
while n < 10:
    
    iter_dict = connection_dict                 # Won't run each iteration 
    #fh.write('\n Run d%:\n' % (n+1))
    
    for key, value in iter_dict.items():
    
        v_list = []             
        print(iter_dict)
        
        if not value == None:                      #Checks arguments
            #num_elem = len(value)
            for i in value:
                v_list.append(iter_dict[i])   
        else: 
            v_list = None     
    
        
        x = key.function(*v_list)                  #Runs functions
        iter_dict[key] = key.function(*v_list)                   #Updates Value  
        #fh.write(f'\n {key.name} = {x}\n')
        
        
    
    print('---',x,value,iter_dict,'This is an iteration') #Checks Dict
    
    n += 1
    print (n)