def total_treasures(treasure_map):
    total=0

    for land, treasure in treasure_map.items():
        total+=treasure

    return total

def can_trust_message(message):
    msg_set= set(filter(str.isalpha, message.lower()))
    return len(msg_set)==26

def find_duplicate_chests(chests):
    freq= {}
    ans=[]
    for chest in chests:
        if chest in freq:
            freq[chest]+=1
        else:
            freq[chest]=1
    
    for chest, count in freq.items():
        if count ==2:
            ans.append(chest)
    return ans

def is_balanced(code):
    

if __name__ == '__main__':

    treasure_map1 = {
        "Cove": 3,
        "Beach": 7,
        "Forest": 5
    }

    treasure_map2 = {
        "Shipwreck": 10,
        "Cave": 20,
        "Lagoon": 15,
        "Island Peak": 5
    }

    print(total_treasures(treasure_map1)) 
    print(total_treasures(treasure_map2)) 

    message1 = "sphinx of black quartz judge my vow"
    message2 = "trust me"

    print(can_trust_message(message1))
    print(can_trust_message(message2))

    chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
    chests2 = [1, 1, 2]
    chests3 = [1]

    print(find_duplicate_chests(chests1))
    print(find_duplicate_chests(chests2))
    print(find_duplicate_chests(chests3))