class USR:
    def __init__(self, name, register = [0, 0, 0, 0], output = 0, ): 
        
        self.name = name 
        self.output = output
        self.register = register
        
    def function(self, *inputs):
        #while len(inputs) < 4: 
        #    args = args + [0]
        register = list(inputs[0:3]) 
        num_var = len(inputs)
        s1 = inputs[-3]
        s0 = inputs[-2]
        clock = inputs[-1]
        if clock == 1:
            if num_var == 4:
                input = inputs[0]
                if s1 == 0 and s0 == 1: #Shift right
                    self.output = self.register[3]
                    del self.register[3]
                    self.register.insert(input)
                
                if s1 == 1 and s0 == 0: #Shift Left
                    self.output = self.register[0]
                    del register[0]
                    self.register.append(input)

                else:  #No changes
                    self.output = input
            
            else: #Parallel load
                self.output = register
                self.output = inputs[0:3]
        else:
            pass 
        

a = USR("USR1")

w=a.function([1,2,3,4],5,0)
print(w)

            