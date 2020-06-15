#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

a = 0 # O(1)
    while (a < n * n * n): # (1 + n^3 )
      a = a + n * n # (1 + n^2)
      # removing constant & exponents 


b) O(n^2) 

sum = 0 # O(1)
    for i in range(n): # O(n)
      j = 1 # 0(1)
      while j < n: # 0(n)
        j *= 2 O(1)
        sum += 1 O(1)


c) O(n) function recursivley calls itself until it hits 0, sub 1 from its value every recurivs. n times in linear fashion with size of input

## Exercise II
    Probable use Binary Search O(log(n)). If the egg is drops from a specific floor, you can determine which section above or below you can filter out based on if the egg breaks. 

