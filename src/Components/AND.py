class AND:
    def __init__(self, name):
        
        self.name = name 
        self.output = 0
        
    def function(self, *args):
        
        list_inputs = args
        if 0 in list_inputs:
            self.output = 0 
        else:
            self.output = 1
        
                
a = [1,2,3]
b = [4]
z = [0]

c = a + b + z

test = AND("AND1")

w=test.function(1, 0, 3, 4, 1, 3)
print(w)