class AND:
    def __init__(self, name, output = 0):
        
        self.name = name 
        self.output = output
        
    def __str__(self):
        return f'{self.name} Output: {self.output}'
    
    def function(self, *args):
        
        list_inputs = args
        if 0 in list_inputs:
            self.output = 0 
        else:
            self.output = 1
        
class CONST:
    def __init__(self, name, output):
        
        self.name = name
        self.output = output
    
    def __str__(self):
        return f'{self.name} Output: {self.output}'
        
    #Function that outputs the constant given
    def function(self):
        self.output = self.output 


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
    
connection_dict= {a: [], b: [], c:[a,b]}
#{a: [], b: [], c:[a,b]}
f = open('tets.txt','w')

comp_list = list(connection_dict.keys())
comp_ran = []
comp_layers = []

f.write('Initial state for all components:\r\n')
for i in comp_list:
    f.write(f"{i.__str__ ()}\r\n")

for comp, input in connection_dict.items():
    #print ("---------",comp_list)
    if input == []:
        comp.function()
        comp_ran.append(comp)
        print(comp_ran)
        comp_list.remove(comp) 
print("1: ", comp_ran)   
comp_layers.append(comp_ran)
print("2: ", comp_layers)  
      
while not (comp_list == []):
    i = 0 
    for comp in comp_list:
        if all(item in list(connection_dict[comp]) for item in comp_ran):   
            comp_out = []
            for used in list(connection_dict[comp]):
                comp_out.append(used.output)
                
            comp.function(comp_out)
            comp_ran.append(comp)
            comp_list.remove(comp)
            
        i -= 1
        print("3: ", comp_ran[i:])
        print("4: ", comp_layers) 
        comp_layers.append(comp_ran[i:])
        
print("5: ", comp_layers)        
f.write('The following is the network layot for the system:\r\n')
for layer in comp_layers:
    num = 1
    f.write(f"Layer {num}:\n")
    f.write(f"{layer}\r\n")
    num += 1
    
f.write('-------------------------------------------------\r\n')

f.write('Simulation Start\r\n')    

f.write('-------------------------------------------------\r\n')
          
# n = 0 
# #fh = open('test.txt', 'w')

# #fh.write("This text file is a simulation of the system Test\n\n --------------------------------------------------------\n")
# #fh.write('\n Simulation Start\n--------------------------------------------------------\n')
# while n < 10:
    
#     iter_dict = connection_dict                 # Won't run each iteration 
#     #fh.write('\n Run d%:\n' % (n+1))
    
#     for key, value in iter_dict.items():
    
#         v_list = []             
#         print(iter_dict)
        
#         if not value == None:                      #Checks arguments
#             #num_elem = len(value)
#             for i in value:
#                 v_list.append(iter_dict[i])   
#         else: 
#             v_list = None     
    
        
#         x = key.function(*v_list)                  #Runs functions
#         iter_dict[key] = key.function(*v_list)                   #Updates Value  
#         #fh.write(f'\n {key.name} = {x}\n')
        
        
    
#     print('---',x,value,iter_dict,'This is an iteration') #Checks Dict
    
#     n += 1
#     print(n)