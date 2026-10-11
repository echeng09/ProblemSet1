def main():
    blue()
    blastoff()
    candy_shop()

#blue():
#creates integer red = 3 and multiplies by 12 to make purple
#prints 36
def blue():
    red = 3
    purple = red*12
    print(purple)

#blastoff():
#takes user input for a number and counts down from that number for blastoff
#prints numbers and blastoff
def blastoff():
    count = int(input("Pick a number: "))
    for i in range(count):
        print(count-i)
    print("blastoff")

def candy_shop():
    candies = ["lollipops", "whoppers", "starbursts"]
    candies.append("kitkat")
    candies.insert(1, "skittles")
    candies.sort()
    idx = candies.index("kitkat")
    candies.remove(idx)
    print(candies)
    user_candies = []
    user_candies.append(input("Candy 1: "))
    user_candies.append(input("Candy 2: "))
    user_candies.append(input("Candy 3: "))
    all_candies = candies + user_candies
    print(len(all_candies))
    for i in all_candies:
        print(i)





    
if __name__ == "__main__":
    main()