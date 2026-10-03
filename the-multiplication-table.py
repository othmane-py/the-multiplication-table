print("****welcome to the multiplication table****")
nmb = int(input("enter a number: "))
for x in range(1,11):
    result = nmb * x
    print(f"{nmb}*{x} = {result}")