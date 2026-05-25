def can_reach(chats, start, end):
# make adjecncy list
    adj_l= {}
    chats = (
    ("Dwayne", "Minh", "Aisha"),
    ("Priya", "Noor", "Dwayne"),
    ("Juan", "Jelly"),
    ("Allison", "Gus"),
    ("Priya", "Bethel", "Janelle", "Ken"),
    ("Noor", "Kimi", "Rubens"),
    ("Minh", "Elora"),
    ("Allison", "Gus", "Juan"),
    ("Priya", "Noor"),
)
    # {'Dwayne': ['Minh', 'Aisha', 'Priya', 'Noor'], 
    #  'Minh': ['Dwayne', 'Aisha', 'Elora'], 
    #  'Aisha': ['Dwayne', 'Minh'], 
    #  'Priya': ['Noor', 'Dwayne', 'Bethel', 'Janelle', 'Ken'], 
    #  'Noor': ['Priya', 'Dwayne', 'Kimi', 'Rubens'], 
    #  'Juan': ['Jelly', 'Allison', 'Gus'], 
    #  'Jelly': ['Juan'], 
    #  'Allison': ['Gus', 'Juan'], 
    #  'Gus': ['Allison', 'Juan'], 
    #  'Bethel': ['Priya', 'Janelle', 'Ken'], 
    #  'Janelle': ['Priya', 'Bethel', 'Ken'], 
    #  'Ken': ['Priya', 'Bethel', 'Janelle'], 
    #  'Kimi': ['Noor', 'Rubens'], 
    #  'Rubens': ['Noor', 'Kimi'], 
    #  'Elora': ['Minh']}
    
    # Janelle → Priya → Dwayne → Minh → Elora

def can_message(chats, start, end):


    adj_l = {}

    for t in chats:
        for person in t:

            if person not in adj_l:
                adj_l[person] = []

            for per in t:
                if per not in adj_l[person] and per != person:
                    adj_l[person].append(per)


    q = []

    visited = set()

    q.append(start)

    while q:


        current = q.pop(0)


        if current == end:
            return True


        if current in visited:
            continue


        visited.add(current)

        for neighbor in adj_l.get(current, []):

            if neighbor not in visited:
                q.append(neighbor)

    return False


    


chats = (
    ("Dwayne", "Minh", "Aisha"),
    ("Priya", "Noor", "Dwayne"),
    ("Juan", "Jelly"),
    ("Allison", "Gus"),
    ("Priya", "Bethel", "Janelle", "Ken"),
    ("Noor", "Kimi", "Rubens"),
    ("Minh", "Elora"),
    ("Allison", "Gus", "Juan"),
    ("Priya", "Noor"),
)
assert can_reach(chats, "Janelle", "Elora") == True
assert can_reach(chats, "Bethel", "Gus") == False
assert can_reach(chats, "Priya", "Noor") == True
assert can_reach(chats, "Rubens", "Ken") == True
assert can_reach(chats, "Allison", "Priya") == False

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
