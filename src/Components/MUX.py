from imaplib import Int2AP


class MUX:
    def __init__(self, name, output = 0): 
        
        self.name = name 
        self.output = output
        
    def function(self, *inputs): #Locked to only 4x1 Mux 
        
        #Reduce size of inputs
        while len(inputs) < 4: 
            inputs = inputs[:4]
        
        #Reduce size of modes
        while len(mode) < 2: 
            mode = mode[:2]
            
        I0 = inputs[0]
        I1 = inputs[1]
        I2 = inputs[2]
        I3 = inputs[3]
        
        s1 = mode[0]
        s0 = mode[1]
        
        if not s0 == 0:
            s0 = 1
        if not s1 == 0:
            s1 = 1
            
        if s0 == 0:
            if s1 == 0:
                self.output = I0
            else:
                self.output = I2
        else: 
            if s1 == 0:
                self.output = I1
            else:
                self.output = I3

a = MUX("MUX1")

w=a.function(1,2,3,4,5,0)
print(w)

            