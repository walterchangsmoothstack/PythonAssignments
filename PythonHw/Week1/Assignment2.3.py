# Three is a Crowd
people = ["foo", "tom", "jerry", "john"]

def crowd_test(people):
    if(len(people) >= 3):
        print("It is crowded")

crowd_test(people)

people = people[2:]

crowd_test(people)

#Three is a Crowd Part 2

def crowd_test(people):
    if(len(people) >= 3):
        print("It is crowded")
    else:
        print("It is not very crowded")

crowd_test(people)

#Six is a Mob

def crowd_test(people):
    if(len(people) > 5):
        print("It is a mob")
    elif(len(people) >= 3):
        print("It is crowded")
    elif(len(people) == 0):
        print("It is empty")
    else:
        print("It is not very crowded")

people += ["gandalf", "frodo", "sam", "aragorn"]

crowd_test(people)

people.pop()

crowd_test(people)

people.pop(0)
del(people[0])
people = people[:-1]

crowd_test(people)

people = []
crowd_test(people)