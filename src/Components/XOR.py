class XOR:
    def __init__(self, name, output = 0):
        
        self.name = name 
        self.output = output
        
    def function(self, *args):  # ** Research for unlimited inputs
        list_inputs = list(args)
        num_inputs = len(list_inputs)
        for i in range(num_inputs):
            if list_inputs[i] >= 1: 
                list_inputs[i] = 1
        sum = sum(list_inputs)
        if (sum % 2) == 0:
            self.output = 0
        else:
            self.output = 1
             
a = [4,7,0]
b = [5]
z = [1]
c = a + b + z + z


test = XOR("XOR1")

w=test.function( 1, 0)
print(w)