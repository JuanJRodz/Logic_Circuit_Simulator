class AND:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, x = [], y = [], z= [], zz= []):
        
        list_inputs = x + y + z + zz
        num_inputs = len(list_inputs)
        
        for i in range(len(list_inputs)):
            if list_inputs[i] == 0:
                return 0
        return 1
                
a = [1,2,3]
b = [4]
z = [0]

c = a + b + z

test = AND("AND1")

w=test.function(c, z)
print(w)