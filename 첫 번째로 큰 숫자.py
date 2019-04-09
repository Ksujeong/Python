A = int(input("정수를 입력하세요.: "))
B = int(input("정수를 입력하세요.: "))
C = int(input("정수를 입력하세요.: "))

if(A>C and C>B):
    print("A 가 첫번째로 큽니다.",A)

elif(A>B and B>C):
    print("A 가 첫번쨰로 큽니다.", A)
    
elif(B>C and C>A):
    print("B 가 첫번째로 큽니다.", B)

elif(B>A and A>C):
    print("B 가 첫번쨰로 큽니다.", B)

elif(C>A and 
