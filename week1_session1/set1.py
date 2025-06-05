def welcome():
    print ("Welcome to The Hundred Acre Wood!")

def greetings(name):
    print (f"Welcome to Acre Wood {name}! My name is Christopher Robin")

def print_catchphrase(character):
    if character == 'Pooh':
        print("Oh bother!")
    elif character =="Tigger":
        print(' TTFN: Ta-ta for now!')
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")
              
def get_item(items, x):
    if x >=0 and x < len(items):
        print(items[x])
    else:
        return None

def sum_honey(hunny_jars):
    print(sum(hunny_jars))

def doubled(hunny_jars):
    doubled_jars=[]
    for hunny in hunny_jars:
        doubled_jars.append(hunny*2)
    print (doubled_jars)

def count_less_than(race_times, threshold):
    count =0
    for time in race_times:
        if time < threshold:
            count+=1
    return count



if __name__ == "__main__":
    welcome()

    greetings("Michael")
    greetings("Winnie the Pooh")

    character = "Pooh"
    print_catchphrase(character)

    character = "Piglet"
    print_catchphrase(character)


    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 2
    get_item(items, x)

    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 5
    get_item(items, x)

    hunny_jars = [2, 3, 4, 5]
    sum_honey(hunny_jars)

    hunny_jars = []
    sum_honey(hunny_jars)

    hunny_jars = [1, 2, 3]
    doubled(hunny_jars)

    race_times = [1, 2, 3, 4, 5, 6]
    threshold = 4
    count_less_than(race_times, threshold)

    race_times = []
    threshold = 4
    count_less_than(race_times, threshold)