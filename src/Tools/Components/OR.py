class OR:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, x = [], y = [], z= [], zz= []):
        
        list_inputs = x + y + z + zz
        num_inputs = len(list_inputs)
        
        for i in range(len(list_inputs)):
            if list_inputs[i] >= 1:
                return 1
        return 0
                
a = [0,0,0]
b = [0]
z = [0]

c = a + b + z

test = OR("OR1")

w=test.function(c, z)
print(w)