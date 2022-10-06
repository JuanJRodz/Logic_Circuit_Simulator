class AND:
    def __init__(self, name, output = 0):
        
        self.name = name 
        self.output = output
    
    def __repr__(self):
        return self.name 
    
    def __str__(self):
        return f'{self.name} Output: {self.output}'
           
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