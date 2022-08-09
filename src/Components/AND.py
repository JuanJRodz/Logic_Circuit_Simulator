class AND:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, *args):
        
        list_inputs = args
        print (args)
        for i in range(len(list_inputs)):
            if list_inputs[i] == 0:
                return 0
        return 1
                
a = [1,2,3]
b = [4]
z = [0]

c = a + b + z

test = AND("AND1")

w=test.function(1, 0, 3, 4, 1, 3)
print(w)