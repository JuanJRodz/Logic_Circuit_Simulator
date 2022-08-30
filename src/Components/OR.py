class OR:
    def __init__(self, name, output = 0):
        
        self.name = name 
        self.output = output
        
    def __str__(self):
        return f'{self.name} Output: {self.output}'
        
    def function(self, *args):
        list_inputs = x + y + z + zz
        list_value = sum(list_inputs)
        if list_value == 0:
            self.output = 0 
        else:
            self.output = 1
        
                
a = [0,0,0]
b = [0]
z = [0]

c = a + b + z

test = OR("OR1")

w=test.function(c, z)
print(w)