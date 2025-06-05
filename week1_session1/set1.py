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
    print(count) 

def print_todo_list(task):
    print ("Pooh's To Dos:")
    for i, t in enumerate (task, start=1):
        print(f'{i}. {t}')

def can_pair(item_quantities):
    for item in item_quantities:
        if item %2 !=0:
            return False
    return True

def split_haycorns(quantity):
    ans = []
    for i in range(1, quantity+1):
        if quantity % i ==0:
            ans.append(i)
    print(ans)

def tiggerfy(s):
    tigger_set = {'T', 't', 'I','i', 'G','g', 'E','e', 'R','r'}
    ans=''
    for letter in s:
        if letter not in tigger_set:
            ans+=letter
    print(ans)

def locate_thistles(items):
    ans=[]
    for index, item in enumerate(items):
        if item == 'thistle':
            ans.append(index)
    print(ans)

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

    task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
    print_todo_list(task)

    task = []
    print_todo_list(task)

    item_quantities = [2, 4, 6, 8]
    can_pair(item_quantities)

    item_quantities = [1, 2, 3, 4]
    can_pair(item_quantities)

    item_quantities = []
    can_pair(item_quantities)

    quantity = 6
    split_haycorns(quantity)

    quantity = 1
    split_haycorns(quantity)

    s = "suspicerous"
    tiggerfy(s)

    s = "Trigger"
    tiggerfy(s)

    s = "Hunny"
    tiggerfy(s)

    items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
    locate_thistles(items)

    items = ["book", "bouncy ball", "leaf", "red balloon"]
    locate_thistles(items)