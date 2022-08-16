class SWITCH: 
    def __init__(self, name, output = 0): 
        
        self.name = name 
        self.output = output
            
    def function(self, *input):
        
        variables = list(input)
        num_var = len(input)
        
        if variables(-1) == 0: 
            pass
        else: 
            variables(-1) = 1
            
        if num_var == 2: 
            #Basic Switch Function  
            if input(1) == True: 
                return input[0] 
            else: 
                return 0
        elif num_var == 3: 
             if self.mode == True:
                 return input[0]
             else:
                 return input[1]
        
        else: 
            print("Component wrongly used")
              

x = SWITCH("SWT1", True)

w= x.function(1)
print(w)


