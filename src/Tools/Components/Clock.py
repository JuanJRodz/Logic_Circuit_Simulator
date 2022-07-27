class Clk:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, loops):

        if (loops % 2) == 0:
                
            return 1 
            
        else:
                
            return 0 
            
a = Clk("Clk1")

print(a.function(9))