class MUX:
    def __init__(self, name): 
        
        self.name = name 
        
    def function(self, *inputs): #Locked to only 4x1 Mux 
        
        #while len(inputs) < 4: 
        #    args = args + [0] 
        s1 = inputs[4]
        s0 = inputs[5]
        
        if not s0 == 0:
            s0 = 1
        if not s1 == 0:
            s1 = 1
            
        if s0 == 0:
            if s1 == 0:
                return inputs[0]
            else:
                return inputs[2]
        else: 
            if s1 == 0:
                return inputs[1]
            else:
                return inputs[3]

a = MUX("MUX1")

w=a.function(1,2,3,4,5,0)
print(w)

            