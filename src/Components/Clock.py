class Clk:
    def __init__(self, name):
        
        self.name = name 
        self.output = 0
        
    def function(self, loops): #Must input the number of iterations 

        if (loops % 2) == 0:
                
            self.output = 1
            
        else:
                
            self.output = 0 
            
a = Clk("Clk1")

print(a.function(9))