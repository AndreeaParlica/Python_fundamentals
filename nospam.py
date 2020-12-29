menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

item_removed = "spam"
for meal in menu:
    for i in range(meal.count(item_removed)):
        meal.remove(item_removed)
    print(meal)
for item in menu:
    print(item)

    #solutie tim

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(",".join(meal))
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ")
#     print()