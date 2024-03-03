#   Reflex Based Agent

goalState = {'A':'0', 'B':'0', 'C':'0'}          # 0=Clean, 1=Dirty
action = 0
cost = 0
roomState = {'A': '1', 'B':'1', 'C':'1'}         # 0=Clean, 1=Dirty

#initial inputs
print("Enter the starting location of rooms(A/B/C)")
location = input()

for room in roomState:
    action = input("Enter the state of " + room + "(0 means Clean and 1 means Dirty)")
    roomState[room] = action

print("Current State: " + str(roomState))
print("Goal State: " + str(goalState))
print("Vaccum cleaner is placed in location " + str(location))


if(roomState != goalState):
    if(location=="A"):
        if(roomState['A'] == '1'):      #if dirty
            roomState['A'] = '0'
            cost+=1
            print("Location A was dirty\nLocation A has been cleaned")
    
        if(roomState == goalState):
            print("Goal state has been met!")
            print("\nTotal cost: " + str(cost))

        location="B"
        cost+=1

#-------------If A is clean. Going from A -> B-------------
            
    if(location=="B"):
            print("\nA is clean")
            print("\nA -> B")
            print("\nCost for moving within rooms = 1")
            

            if(roomState['B'] == '1'):   #if dirty
                roomState['B'] = '0'
                cost+=1
                print("Location B was dirty\nLocation B has been cleaned")

            if(roomState == goalState):
                print("Goal state has been met!")
                print("\nTotal cost: " + str(cost))

            location="C"
            cost+=1

            #-------------If B is clean. Going from B -> C-------------
    if(location=="C"):
            print("\nB is clean")
            print("\nB -> C")
            print("\nCost for moving within rooms = 1")
            

            if(roomState['C'] == '1'):   #if dirty
                roomState['C'] = '0'
                cost+=1
                print("Location C was dirty\nLocation C has been cleaned")

            if(roomState == goalState):
                print("Goal state has been met!")
                print("\nTotal cost: " + str(cost))





else:
    print("\nAll rooms are already clean")
    print("\nTotal Cost: " + str(cost))