class Clk:
    def __init__(self, name):
        
        self.name = name 
        
    def function(self, loops):

        if (loops % 2) == 0:
                
                loops -= 1
                return 1 
            
        else:
                
            loops -= 1
            return 0 
            
a = Clk("Clk1")

print(a.function(9))