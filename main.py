
def pattern(rows:int):
    '''print number as halve pyramid'''
    for i in range(rows, 0, -1):
        for j in reversed(range(1 , i+1)):
            print(j,end=" ")
        print("\n")     
    
   
        
    
rows = int(input("Enter number of rows:"))
pattern(rows)
print(pattern.__doc__)

