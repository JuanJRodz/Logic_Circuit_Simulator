class USR:
    def __init__(self, name): 
        
        self.name = name 
        
    def function(self, inputs, s1, s0):
        
        while len(inputs) < 4: 
            args = args + [0] 

     
        if s1 == 0 and s0 == 1: #Shift right
            del inputs[3]
            inputs = [0] + inputs
            return inputs
        
        if s1 == 1 and s0 == 0: #Shift Left
            del inputs[0]
            inputs.append(0)
            return inputs
        
        if s1 == 1 and s0 == 1: #Parallel load
            return inputs

        else:
            return inputs

a = USR("USR1")

w=a.function([1,2,3,4],5,0)
print(w)

            