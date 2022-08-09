class XOR:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, *args):  # ** Research for unlimited inputs
        one = 0
        list_inputs = list(args)
        num_inputs = len(list_inputs)
        for i in range(num_inputs):
            if list_inputs[i] >= 1: 
                list_inputs[i] = 1
                one = one + 1

        if one == 0:
            return 0
        elif one == num_inputs:
            return 0
        else:
            return 1
             
a = [4,7,0]
b = [5]
z = [1]
c = a + b + z + z


test = XOR("XOR1")

w=test.function( 1, 0)
print(w)