class OR:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, *args):
        one = 0
        list_inputs = list(args)
        num_inputs = len(list_inputs)
        for i in range(num_inputs):
            if list_inputs[i] >= 1: 
                list_inputs[i] = 1
                one = one + 1

        if one == 0:
            return 0
        else:
            return 1     
                

test = OR("OR1")

w=test.function(0,0,0)
print(w)