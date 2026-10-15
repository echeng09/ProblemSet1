#main method
#where i will call and test my functions
def main():
    blue()
    blastoff()
    tot = candy_shop()
    print("Cost: " + str(tot))
    fruit_pricing()


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
    print("blastoff!")


#candy_shop():
#adds a list of candies with 3 of users choice and returns total cost where each is $1.25
def candy_shop():
    candies = ["lollipops", "whoppers", "starbursts"]
    candies.append("kitkat")
    candies.insert(1, "skittles")
    candies.sort()
    idx = candies.index("kitkat")
    candies.pop(idx)
    print(candies)
    user_candies = []
    user_candies.append(input("Candy 1: "))
    user_candies.append(input("Candy 2: "))
    user_candies.append(input("Candy 3: "))
    all_candies = candies + user_candies
    print(len(all_candies))
    for i in all_candies:
        print(i)
    cost = len(all_candies) * 1.25
    return cost

#fruits_pricing():
#creates fruit and price dictionary, adds pear, and calcs cost of shopping
def fruit_pricing():
    fruits = {"apple": 0.75, "banana": 1.25, "orange": 0.80, "peach": 2.25, "coconut": 2.80}
    fruits["pear"] = 1.15
    print(fruits.get("peach"))
    for fruit, price in fruits.items():
        if price >= 1.25:
            print(fruit)
    total = 3 * fruits["apple"] + 2 * fruits["banana"] + fruits["coconut"]
    print(total)
    #or could make a for loop like earlier. make dictionary w/ quantities for each. then multiply price and quantity for each fruit



    
if __name__ == "__main__":
    main()