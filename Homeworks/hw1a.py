#a program reverse halfs of list
A = [1,2,3,4,5,6]
B = A[:len(A)//2]
C = A[len(A)//2:]
print(A)
print(B)
print(C)
reverseA = C + B
print(reverseA)
