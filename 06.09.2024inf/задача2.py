#Попадюк Олександр
import math
r = float(input('r= '))
a = r*math.sqrt(3)
s_t = a*a*math.sqrt(3)/4
s_k = math.pi*r*r
s = s_k - s_t
print("S=", round(s,2))