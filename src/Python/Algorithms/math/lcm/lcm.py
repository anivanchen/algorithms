def lcm(n, i):
   if n > i: greater = n
   else: greater = i
   while(True):
       if((greater % n == 0) and (greater % i == 0)):
           return greater
       greater += 1