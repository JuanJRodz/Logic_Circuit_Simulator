class CONST:
    def __init__(self, name, constant):
        
        self.name = name
        self.constant = constant
        
        #Constant divided into Bits 
    
a = CONST("CONS1", (1, 0, 1, 1))

print (a.constant)
    