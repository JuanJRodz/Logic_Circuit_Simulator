class NAND:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, x, y):
        if(x and y) >= 1:
            return 0
        else:
            return 1       
a = 1
b = 0

test = NAND("NAND1")

w=test.function(a, b)
print(w)