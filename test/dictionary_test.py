from src.Tools.Components import *

a = CONST("Entrada", 1)   
b = CONST("Señal", 0)
c = AND("AND1")


print(a.function())    
connection_dict= {a: [], b: [], c:[a,b]}

d = System(connection_dict, 10)

for key in connection_dict:
    print(connection_dict.get(key))
    