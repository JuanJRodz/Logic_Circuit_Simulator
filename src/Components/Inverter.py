class INVERTER:
    def __init__(self, name, constant):
        
        self.name = name 
        #self.constant = constant
    
    def function(self, input):   
    
        if input == 0:
            return 1 
        else:
            return 0 

test = INVERTER("INVERTER1", 1)

print(test.function())