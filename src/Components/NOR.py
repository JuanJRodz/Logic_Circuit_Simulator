class NOR:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, *inputs):   #Only accepts two inputs 
        if(inputs[0] or inputs[1]) == 1:
            return 0
        else:
            return 1       
a = 1
b = 0

test = NOR("NOR1")

w=test.function(a, b)
print(w)