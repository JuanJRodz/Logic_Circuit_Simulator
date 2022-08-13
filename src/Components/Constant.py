class CONST:
    def __init__(self, name, constant):
        
        self.name = name
        self.constant = constant
        
    #Function that outputs the constant given
    def function(self):
        return self.constant 


#Test
item = CONST("CONS1", 1)

print(item.function())
