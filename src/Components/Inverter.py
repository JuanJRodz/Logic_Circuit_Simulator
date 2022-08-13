class INVERTER:
    def __init__(self, name, constant):
        
        self.name = name 
        #self.constant = constant
        self.output = 0
    
    def function(self, input):   
    
        if input == 0:
            self.output = 1
        else:
            self.output = 0 

test = INVERTER("INVERTER1", 1)

print(test.function())