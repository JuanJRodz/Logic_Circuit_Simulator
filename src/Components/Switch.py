class SWITCH: 
    def __init__(self, name, mode:bool): 
        
        self.name = name 
        self.mode = mode 
            
    def function(self, *input):
        
        num_var = len(input)
        
        if num_var == 1: 
            #Basic Switch Function  
            if self.mode == True: 
                return input[0] 
            else: 
                return 0
        elif num_var == 2: 
             if self.mode == True:
                 return input[0]
             else:
                 return input[1]
        
        else: 
            print("Component wrongly used")
              

x = SWITCH("SWT1", True)

w= x.function(1)
print(w)


