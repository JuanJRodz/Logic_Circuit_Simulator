class XOR:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, x = [], y = [], z= [], zz= []):
        one = 0
        list_inputs = x + y + z + zz
        num_inputs = len(list_inputs)
        
        for i in range(num_inputs):
            if list_inputs[i] >= 1: 
                list_inputs[i] = 1
                one = one + 1
        if(one % 2) == 0:
            return 0
        else:
            return 1
             
a = [4,6,0]
b = [5]
z = [0]
c = a + b + z

test = XOR("XOR1")

w=test.function(c, z)
print(w)