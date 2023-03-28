import UI

# main program which uses the UI file to execute
def main():
    # creation of empty team and choice as "0" to start program over again
    teams = []
    choice = "0"
    while choice != "11":
        # save the User_Interface class as ui
        ui = UI.User_Interface()
        
        # print the menu and save the response in choice
        choice = ui.print_menu()
        
        # create a else-elif-else statement where every number has another function behind it
        if choice == "1":
            # if 1 is entered, create a team and append it to the teams list
            team = ui.create_team()
            teams.append(team)
        elif choice == "2":
            # if 2 is entered, read individual team based on teams list
            ui.read_individual_team(teams)
        elif choice == "3":
            # if 3 is entered, read all boys or girls teams based on teams list
            ui.read_boys_or_girls_teams(teams)
        elif choice == "4":
            # if 4 is entered, read all teams based on teams list
            ui.read_all_teams(teams)
        elif choice == "5":
            # if 5 is entered, update individual property from specific team based on teams list
            ui.update_team_property(teams)
        elif choice == "6":
            # if 6 is entered, delete individual team from teams list
            ui.delete_team(teams)
        elif choice == "7":
            # if 7 is entered, get number of teams and percentage of paying teams from lists
            ui.number_of_teams_and_percentage(teams)
        elif choice == "8":
            # if 8 is entered, cancel a team from partitioning in the teams list
            ui.cancel_team(teams)
        elif choice == "9":
            # if 9 is entered, export all teams to a file from the teams list
            ui.export_to_file(teams)
        elif choice == "10":
            # if 9 is entered, import teams from a file the teams list
            ui.import_from_file(teams)
        elif choice == "11":
            # exit the program if 11 is entered
            print("Exiting the program... \n")
        else:
            # if none of the numbers have been entered, give an error and repeat the process
            print("Error, incorrect input! \n")

# run the main program
main()