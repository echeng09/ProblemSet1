#1) main method
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
    #2a) Create an integer, red, and assign it a value of 3
    red = 3
    #2b) Multiply your new variable by 12 and store the result in purple
    purple = red*12
    #2c) Print purple
    print(purple)

#blastoff():
#takes user input for a number and counts down from that number for blastoff
#prints numbers and blastoff
def blastoff():
    #3a) Ask the user for a number and store it in a variable, count
    count = int(input("Pick a number: "))
    #3b) Using a loop, print each number from count to 1 (inclusive)
    for i in range(count):
        print(count-i)
    #3c) At the end of the count, print “blastoff!“
    print("blastoff!")


#candy_shop():
#adds a list of candies with 3 of users choice and returns total cost where each is $1.25
def candy_shop():
    #4a) Initialize a new list, candies, with three of your favorite candies
    candies = ["lollipops", "whoppers", "starbursts"]
    #4b) Append “kitkat” to the end of the list
    candies.append("kitkat")
    #4c) Insert another candy at index 1
    candies.insert(1, "skittles")
    #4d) Sort the list
    candies.sort()
    #4e) Find and remove “kitkat” in the list (do not manually count the index yourself!)
    idx = candies.index("kitkat")
    candies.pop(idx)
    #4f) Print the list
    print(candies)
    #4g) Create a new empty list called, user_candies 
    user_candies = []
    #4h) Ask the user for 3 favorite candies and store them in user_candies
    user_candies.append(input("Candy 1: "))
    user_candies.append(input("Candy 2: "))
    user_candies.append(input("Candy 3: "))
    #4i) Add the content of candies and user_candies together in a variable called all_candies
    all_candies = candies + user_candies
    #4j) Print the length of all_candies
    print(len(all_candies))
    #4k) Print each item in all_candies on separate lines
    for i in all_candies:
        print(i)
    #4l) Let’s say each candy costs $1.25. Return the total cost of all_candies if you purchased one of each.
    cost = len(all_candies) * 1.25
    #4m) Print the total cost in the main method
    return cost

#fruits_pricing():
#creates fruit and price dictionary, adds pear, and calcs cost of shopping
def fruit_pricing():
    #5a) Create and initialize a dictionary, fruits, with the following key-value (fruit-price) pairs: apple - 0.75, banana - 1.25, orange - 0.80, peach - 2.25, coconut - 2.80
    fruits = {"apple": 0.75, "banana": 1.25, "orange": 0.80, "peach": 2.25, "coconut": 2.80}
    #5b) Add “pear” to the inventory, costing $1.15
    fruits["pear"] = 1.15
    #5c) Print the cost of a peach using get()
    print(fruits.get("peach"))
    #5d) Using a for loop, print out all fruits that cost at least $1.25
    for fruit, price in fruits.items():
        if price >= 1.25:
            print(fruit)
    #5e) Print out the total cost of this shopping trip: 3 apples, 2 bananas, 0 oranges, 0 peaches, 1 coconut
    total = 3 * fruits["apple"] + 2 * fruits["banana"] + fruits["coconut"]
    print(total)
    #or could make a for loop like earlier. make dictionary w/ quantities for each. then multiply price and quantity for each fruit



    
if __name__ == "__main__":
    main()