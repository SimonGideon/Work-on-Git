# #EURO ---> 130.37
# #YEN ----->75
# #RAND -----> 7.75
# #UGS ------->30.75
# #GBP-------->140.75
# #USD ------> 155
# #TNZ -------> 40.75
# print("1. EURO 3. RAND    5.GBP    7.TNZ")
# print("2. YEN  4. UGS     6.USD")
# n = input("Enter your option: ")
# a = input("Enter amount in Ksh: ")
# if n==1:
#     b = a/130.37
#     print(b, "Euros")
# if n==2:
#     b= a/75
#     print(b, "YEN")
# if n==3:
#     b= a/7.75
#     print(b, "RAND")
# if n==4:
#     b= a*30.75
#     print(b, "UGS")
# if n==5:
#     b= a/140.75
#     print(b, "GPB")
# if n==6:
#     b= a/155
#     print(b, "USD")
# if n==7:
#     b= a/40.75
#     print(b, "TNZS")

convert={
    'EURO': {
        1:130.37
        },
    'YEN': {
        1:75
        },
    'RAND': {
        1:7.75
        },
    'UGS': {
        30.75:1
        },
    'GBP': {
        1:140.75
        },
    'USD': {
        1:155
        },
    'TNZ': {
        1:40.75
        },
}
print(convert)
currency=str(input("Enter the currency")).upper()
amount=eval(input("Input amount: "))
c=convert[currency]
for key,value in c.items():
    if key==1:
        v=amount/value
        print(v)
    elif key>1:
        v=amount*key
        print(v)