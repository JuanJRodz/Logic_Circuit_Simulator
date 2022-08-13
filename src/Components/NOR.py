class NOR:
    def __init__(self, name):
        
        self.name = name 
        self.output = 0
        
    def function(self, *inputs):   #Only accepts two inputs 
        if(inputs[0] or inputs[1]) == 1:
            self.output = 0
        else:
            self.output = 1   
a = 1
b = 0

test = NOR("NOR1")

w=test.function(a, b)
print(w)