def can_reach(chats, start, end):
    pass


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
