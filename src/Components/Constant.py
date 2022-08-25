class CONST:
    def __init__(self, name, output):
        
        self.name = name
        self.output = output
        
    #Function that outputs the constant given
    def function(self):
        self.output = self.output 


#Test
item = CONST("CONS1", 1)

print(item.function())
