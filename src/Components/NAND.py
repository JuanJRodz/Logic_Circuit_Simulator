class NAND:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, *inputs):   #Only accepts two inputs 
        if(inputs[0] and inputs[1]) >= 1:
            return 0
        else:
            return 1       
a = 1
b = 0

test = NAND("NAND1")

w=test.function(a, b)
print(w)