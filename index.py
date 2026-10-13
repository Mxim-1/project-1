# x = int(input("Enter a number: "))
# count = 0
# while x <= 100:
#     count += x
#     x += 1
# print(count)
day = input("Enter a day of the week: ")
match day:
    case "sunday":
        print("Today is Sunday")
    case "monday":
        print("Today is Monday")
    case "tuesday":
        print("Today is Tuesday")
    case "wednesday":
        print("Today is Wednesday")