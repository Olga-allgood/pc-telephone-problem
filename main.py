def can_reach(chats, start, end):


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