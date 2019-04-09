while True:
    year = int(input("연도: "))

    if(year%4==0 and year%100==0 and year%400==0):
        print("윤년")

    elif(year%4==0 and year%100==0):
        print("윤년x")

    else:
        print("윤년")
