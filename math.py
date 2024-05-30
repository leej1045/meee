import math
a = 1
b = 4
c = 2
D = b * b - 4 * a * c 
if D >=  0:
  print('X=', (-b + math.sqrt(D)) / (2 * a), ',',(-b - math.sqrt(D)) /(2 *a))
else:
  print('해없음')  
