def computeGCF(n, i):
   while(i):
       n, i = i, n % i
   return n