# Author: MOG 9/29/21

team_points = input("How many points did the team score? ")

if int(team_points) <= 8:
    print("No medal :(")
else:
    if int(team_points) <= 11:
        print("The team wins a bronze medal!")
    else:
        if int(team_points) <= 14:
            print("The team wins a silver medal!")
        else:
            print("The team wins gold :)")