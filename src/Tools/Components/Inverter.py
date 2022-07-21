class INVERTER:
    def __init__(self, name, constant):
        
        self.name = name 
        self.constant = constant
    def function(self):
        if self.constant >= 1:
            return 0 
        else:
            return 1 

test = INVERTER("INVERTER1", 1)

print(test.function())