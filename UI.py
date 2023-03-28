# import the Team file as t
# import csv and datetime (datetime/date classes) module
import Team as t
from datetime import datetime, date
import csv

# User_Interface class that contains all the executing functions
class User_Interface:
    # function that prints the menu and asks for input
    def print_menu(self):
        # print the whole menu
        print('--- TEAM MENU ---')
        print('1) Create team')
        print('2) Read individual team')
        print('3) Read teams, boys or girls')
        print('4) Read all teams')
        print('5) Update team')
        print('6) Delete team')
        print('7) Number of current teams and percentage of fee payment')
        print('8) Cancel team participation')
        print('9) Export to file')
        print('10) Import file')
        print('11) Quit')
        # ask of input for what choice
        choice = input("Select Option: ")
        print("")
        # returning the choice
        return choice
    
    # function that creates the team
    def create_team(self):
        # set the creation day to today (date only)
        creation_date = date.today()
        print("===== CREATE NEW TEAM =====")
        
        # get the team name as input
        team_name = str(input("What is the name of the team: "))
        
        # gathering the team_type with check if it is indeed boy or girl
        team_type = ""
        while team_type != "b" and team_type != "boy" and team_type != "boys" and team_type != "g" and team_type != "girl" and team_type != "girls":
            team_type = str(input("What is the type of the team (b for boys or g for girls): ")).lower()
            if team_type == "b" or team_type == "boy" or team_type == "boys":
                team_type = "boys"
            elif team_type == "g" or team_type == "girl" or team_type == "girls":
                team_type = "girls"
            else:
                print("Incorrect type, please fill in boys(b) or girls(g).")
        
        # gathering the fee_paid and fee_to_pay with check if it is yes or no and if the amount is a number
        fee_paid = ""
        while fee_paid != "y" and fee_paid != "yes" and fee_paid != "n" and fee_paid != "no" and fee_paid != True and fee_paid != False:
            fee_paid = str(input("Is the fee paid (Yes or No): ")).lower()
            if(fee_paid == "y" or fee_paid == "yes"):
                fee_paid = True
                fee_to_pay = 0
            elif(fee_paid == "n" or fee_paid == "no"):
                fee_paid = False
                while True:
                    try:
                        fee_to_pay = int(input("What is the fee amount that needs to be paid (write the number that needs to be paid in SEK): "))
                        break
                    except ValueError:
                        print("Oops! That was no valid number. Try again...")
            else:
                print("Incorrect type, please fill yes or no.")

        # creating the new team as an object and returning the object
        print("")
        team = t.Team(creation_date, team_name, team_type, fee_paid, fee_to_pay)
        return team

    # function that returns an individual team based on your input
    def read_individual_team(self, teams):
        # if no teams are available then state this and skip
        if len(teams) == 0:
            print("There are no teams in the list \n")
        # else start the function
        else:
            # print out a nice overview of all the teams
            for team in teams:
                print(f"ID: {team.get_team_id()} | Team Name: {team.get_team_name()}")
            print("")
            
            # gather input the ID of the team that needs to be displayed in detail
            selected_id = int(input("Enter the ID of the team that must be displayed: "))
            print("")
            
            # for loop through all the teams 
            # and if the ID is in the list the team will be printed
            number_of_teams_found = 0
            for team in teams:
                if selected_id == team.get_team_id():
                    number_of_teams_found += 1
                    print(team)

            # if more than one teams are displayed respond with an error that the ID is duplicated
            if number_of_teams_found > 1:
                print("WATCH OUT!! There are multiple teams with the same ID.")
            # elif there are not teams found with the ID, report this with a print statement
            elif number_of_teams_found == 0:
                print("ID not found")
            # else do nothing
            else:
                pass
            
            # press enter to end the function and go back to the menu
            input("PRESS ENTER TO GO BACK TO THE MENU")
            print("")

    # function that returns teams based on your gender input (boys or girls)
    def read_boys_or_girls_teams(self, teams):
        # if no teams are available then state this and skip
        if len(teams) == 0:
            print("There are no teams in the list \n")
        # else start the function
        else:
            # ask for input about what gender you want to see
            selected_gender = str(input("You want to see the boy or girl teams (enter b or g): ")).lower()
            print("")
            # check if the correct gender was put in, else return error and request again for input
            while selected_gender != "b" and selected_gender != "boy" and selected_gender != "boys" and selected_gender != "g" and selected_gender != "girl" and selected_gender != "girls":
                print("Ooops!! Input incorrect. Try again...")
                selected_gender = str(input("You want to see the boy or girl teams (enter b or g): ")).lower()

            # generalize the input to the same statement
            if selected_gender == "g" or selected_gender == "girl" or selected_gender == "girls":
                selected_gender = "girls"
            else:
                selected_gender = "boys"

            # for loop through all the teams 
            # and if the gender is in the team it will be printed
            number_of_teams_found = 0
            for team in teams:
                if selected_gender == team.get_team_type():
                    # only print this statement the first round, if any teams are found
                    if number_of_teams_found == 0:
                        print("=== FOLLOWING TEAM(S) ARE FOUND === \n")
                    number_of_teams_found += 1
                    print(team)

            # if there are not teams found with the gender, report this with a print statement
            if number_of_teams_found == 0:
                print("No teams found with this gender")
            # else do nothing
            else:
                pass
            
            # press enter to end the function and go back to the menu
            input("PRESS ENTER TO GO BACK TO THE MENU")
            print("")
    
    # function that returns all teams
    def read_all_teams(self, teams):
        # if no teams are available then state this and skip
        if len(teams) == 0:
            print("There are no teams in the list \n")
        # else start the function
        else:
            # for loop through all the teams and return all of them
            number_of_teams_found = 0
            for team in teams:
                # only print this statement the first round, if any teams are found
                if number_of_teams_found == 0:
                    print("=== FOLLOWING TEAM(S) ARE FOUND === \n")
                number_of_teams_found += 1
                print(team)
            
            # press enter to end the function and go back to the menu
            input("PRESS ENTER TO GO BACK TO THE MENU")
            print("")
    
    # function that updates one property at a time for one team at a time
    def update_team_property(self, teams):
        # if no teams are available then state this and skip
        if len(teams) == 0:
            print("There are no teams in the list \n")
        # else start the function
        else:
            # print out a nice overview of all the teams
            for team in teams:
                print(f"ID: {team.get_team_id()} | Team Name: {team.get_team_name()}")
            print("")
            
            # get the ID of the team that needs to be updated
            selected_id = int(input("Enter the ID of the team you want to update: "))
            print("")
            
            # for loop through all the teams 
            # and if the ID is in the team it will be printed and updated
            number_of_teams_updated = 0
            for team in teams:
                if selected_id == team.get_team_id():
                    number_of_teams_updated += 1
                    print(team)
                    
                    # print all the updateable properties and ask for the input
                    print("These are the properties: team_name, team_type, fee_paid, fee_amount")
                    update_property = str(input("What property do you want to update: ")).lower()
                    while update_property != "team_name" and update_property != "team_type" and update_property != "fee_paid" and update_property != "fee_amount":
                        print("Ooops!! Input incorrect. Try again...")
                        update_property = str(input("What property do you want to update (See above for examples): ")).lower()
                    
                    # if team name needs to be updated it will be this choice
                    if update_property == "team_name":
                        # new name will be asked and will be set afterwards
                        team_name = str(input("What should the new teamname be: "))
                        team.set_team_name(team_name)
                    # elif the team type needs to be updated it will be this choice
                    elif update_property == "team_type":
                        # the new team type will be asked and checked if it is a correct gender (boys or girls)
                        team_type = ""
                        while team_type != "b" and team_type != "boy" and team_type != "boys" and team_type != "g" and team_type != "girl" and team_type != "girls":
                            team_type = str(input("What should the new team type be (b for boys or g for girls): ")).lower()
                            if team_type == "b" or team_type == "boy" or team_type == "boys":
                                team_type = "boys"
                            elif team_type == "g" or team_type == "girl" or team_type == "girls":
                                team_type = "girls"
                            else:
                                print("Incorrect type, please fill in boys(b) or girls(g).")
                        team.set_team_type(team_type)
                    # elif the fee paid (Yes or No) needs to be updated it will be this choice
                    elif update_property == "fee_paid":
                        # the new payment status will be asked and checked if it is a correct (yes or no)
                        fee_paid = ""
                        while fee_paid != "y" and fee_paid != "yes" and fee_paid != "n" and fee_paid != "no" and fee_paid != True and fee_paid != False:
                            fee_paid = str(input("Is the fee paid (Yes or No): ")).lower()
                            # if the payment status is yes then the fee amount will be set to 0 too
                            if(fee_paid == "y" or fee_paid == "yes"):
                                fee_paid = True
                                fee_to_pay = 0
                            # if the payment status is no then the fee amount needs to be set again
                            elif(fee_paid == "n" or fee_paid == "no"):
                                fee_paid = False
                                # the fee amount is gathered again and checked if it is a valid number
                                while True:
                                    try:
                                        fee_to_pay = int(input("What is the new fee amount that needs to be paid: "))
                                        break
                                    except ValueError:
                                        print("Oops! That was no valid number. Try again...")
                            else:
                                print("Incorrect type, please fill yes or no.")
                        team.set_team_fee_paid(fee_paid)
                        team.set_team_fee(fee_to_pay)
                    # elif the fee amount changed needs to be updated it will be this choice
                    elif update_property == "fee_amount":
                        if team.get_team_fee_paid() == False:
                            # the fee amount is gathered and checked if it is a valid number and changed if correct
                            while True:
                                try:
                                    fee_to_pay = int(input("What is the new fee amount that needs to be paid: "))
                                    break
                                except ValueError:
                                    print("Oops! That was no valid number. Try again...")
                            team.set_team_fee(fee_to_pay)
                        else:
                            print("Fee is already paid, so you can not change the amount!!")
                    else:
                        # an statement will be printed and you will go back to the menu
                        print("Error!!! Property does not exist!")
                        break
                    
                    # if something is changed the team will be printed with the new properties
                    print("\n== NEW TEAM PROPERTIES ==")
                    print(team)

            # if more than one teams are displayed respond with an error that the ID is duplicated
            if number_of_teams_updated > 1:
                print("WATCH OUT!! There are multiple teams with the same ID.")
            # elif there are not teams found with the ID, report this with a print statement
            elif number_of_teams_updated == 0:
                print("ID not found")
            # else do nothing
            else:
                pass
            
            # press enter to end the function and go back to the menu
            input("PRESS ENTER TO GO BACK TO THE MENU")
            print("")

    # function that deletes a team
    def delete_team(self, teams):
        # if no teams are available then state this and skip
        if len(teams) == 0:
            print("There are no teams in the list \n")
        # else start the function
        else:
            # print out a nice overview of all the teams
            for team in teams:
                print(f"ID: {team.get_team_id()} | Team Name: {team.get_team_name()}")
            print("")
            
            # get the ID of the team that needs to be deleted
            delete_id = int(input("Enter the ID of the team that must be deleted: "))
            print("")
            
            # for loop through all the teams 
            # and if the ID is in the list the team will be printed and afterwards deleted with confirmation
            number_of_teams_found = 0
            for index in range(len(teams)):
                if delete_id == teams[index].get_team_id():
                    # print the team and ask for confirmation
                    print(teams[index])
                    number_of_teams_found += 1
                    confirm = str(input("You confirm that this team must be deleted (Yes or No): ")).lower()

                    # while confirmation input is incorrect then re-request the input
                    while confirm != "y" and confirm != "yes" and confirm != "no" and confirm != "n":
                        print("Ooops!! Input incorrect. Try again...")
                        confirm = str(input("You confirm that this team must be deleted (Yes or No): ")).lower()
                    
                    # if the input is correct and yes then delete the team
                    if confirm == "y" or confirm == "yes":
                        teams.pop(index)
                        print("Team has been deleted! \n")
                    # else the team will not be deleted if the answer is no
                    else:
                        print("The team has not been deleted! \n")
    
    # function that returns the number of teams 
    # and percentage of teams that have paid their fee
    def number_of_teams_and_percentage(self, teams):
        # if no teams are available then state this and skip
        if len(teams) == 0:
            print("There are no teams in the list \n")
        # else start the function
        else:
            # get all the participating teams
            participating_teams = []
            for team in teams:
                if team.get_cancel_date() == None:
                    participating_teams.append(team)
            
            # print out a statement with the number of current teams
            print(f"The number of teams is {len(participating_teams)} team(s). \n")
            
            # add up the number of teams that paid the fees
            number_of_fees_paid = 0
            for team in participating_teams:
                if team.get_team_fee_paid() == True:
                    number_of_fees_paid += 1
            
            # calculate the percentage of the teams that paid the fee and return it
            percentage = int(number_of_fees_paid / len(participating_teams) * 100)
            print(f"Percentage of teams that paid the fee: {percentage}% \n")
            
        # press enter to end the function and go back to the menu
        input("PRESS ENTER TO GO BACK TO THE MENU")
        print("")

    # function that cancels the team for partitioning without deletion
    def cancel_team(self, teams):
        # if no teams are available then state this and skip
        if len(teams) == 0:
            print("There are no teams in the list \n")
        # else start the function
        else:
            # print out a nice overview of all the teams
            for team in teams:
                print(f"ID: {team.get_team_id()} | Team Name: {team.get_team_name()}")
            print("")
            
            # get the ID of the team that needs to bee cancelled 
            cancel_id = int(input("Enter the ID of the team that needs to be cancelled: "))
            print("")
            
            # for loop through all the teams 
            # and if the ID is in the list the team cancelled if...
            number_of_teams_found = 0
            for team in teams:
                if cancel_id == team.get_team_id():
                    # if the team is already cancelled it will not be cancelled again
                    if team.get_cancel_date() != None:
                        print("Team participation has already been cancelled \n")
                        break
                    # else start the team cancellation
                    else:
                        # print the team and ask for confirmation if it needs to be cancelled
                        print(team)
                        number_of_teams_found += 1
                        confirm = str(input("You confirm that this team must be cancelled (Yes or No): ")).lower()

                        # while confirmation input is incorrect then re-request the input
                        while confirm != "y" and confirm != "yes" and confirm != "no" and confirm != "n":
                            print("Ooops!! Input incorrect. Try again...")
                            confirm = str(input("You confirm that this team must be cancelled (Yes or No): ")).lower()
                        
                        # if the input is correct and yes then cancel the team
                        if confirm == "y" or confirm == "yes":
                            cancellation_date = date.today()
                            team.set_cancel_date(cancellation_date)
                            print("The team has been cancelled! \n")
                        # else the team will not be cancelled if the answer is no
                        else:
                            print("The team has not been cancelled! \n")
                
            # if more than one teams are displayed respond with an error that the ID is duplicated
            if number_of_teams_found > 1:
                print("WATCH OUT!! There are multiple teams with the same ID.")
            # elif there are not teams found with the ID, report this with a print statement
            elif number_of_teams_found == 0:
                print("ID not found")
            # else do nothing
            else:
                pass
            
             # press enter to end the function and go back to the menu
            input("PRESS ENTER TO GO BACK TO THE MENU")
            print("")
    
    # function that exports all the teams to txt file
    def export_to_file(self, teams):
        # if no teams are available then state this and skip
        if len(teams) == 0:
            print("There are no teams in the list \n")
        # else start the function
        else:
            # print a statement about the export and set some variables about the file and header
            print("All the teams will be exported a file in this folder...")
            filename = 'teams.txt'
            headers = ['team_id','creation_date','team_name','team_type','fee_paid','fee_amount','cancel_date']
            try:
                # open the file
                with open(filename, 'w', newline='') as f:
                    # write the header
                    writer = csv.writer(f)
                    writer.writerow(headers)
                    
                    # loop through all the current teams
                    for team in teams:
                        # if no cancellation date is mentioned then add None as the cancellation date
                        if team.get_cancel_date() == None:
                            cancel_date = "None"
                        # else, so if a cancellation date is mentioned, then add this date as variable
                        else:
                            cancel_date = team.get_cancel_date()
                        
                        # write the current team as a csv row into a txt file
                        writer.writerow([team.get_team_id(), team.get_team_date(), team.get_team_name(), team.get_team_type(), team.get_team_fee_paid(), team.get_team_fee(), cancel_date])
            # if there are any errors catch them here
            except BaseException as e:
                print('BaseException:', filename)
            # else print the success-statement if the file has been successfully created
            else:
                print('Data has been successfully saved in file teams.txt in this folder! \n')
                
        # press enter to end the function and go back to the menu
        input("PRESS ENTER TO GO BACK TO THE MENU")
        print("")
    
    # function that imports all the teams from a txt file
    def import_from_file(self, teams):
        # print a statement about the export and set the name of the file that will be used
        print("All the teams will be imported from file in this folder...")
        filename = 'teams.txt'
        
        # try to open the file and gather the information
        try:
            # open the file
            with open(filename, newline='') as f:
                # read the lines and skip the header line by using 'next'
                csvreader = csv.reader(f)
                next(csvreader)
                
                # loop through all the lines 
                for row in csvreader:
                    # assign the row properties based on the index
                    creation_date = datetime.date(datetime.strptime(row[1], '%Y-%m-%d'))
                    team_name = row[2]
                    team_type = row[3]
                    fee_paid = row[4]
                    fee_amount = row[5]
                    cancel_date = row[6]
                    
                    # create the team using the just created variables
                    team = t.Team(creation_date, team_name, team_type, fee_paid, fee_amount)
                    
                    # if the cancel date is 'None' append the team to the teams list
                    if cancel_date == "None":
                        teams.append(team)
                    # else if there is a cancel date noted:
                    else:
                        # convert the string to a date type (without the time)
                        cancel_date_converted = datetime.date(datetime.strptime(cancel_date, '%Y-%m-%d'))
                        
                        # set the cancel date and append the team now to the teams list
                        team.set_cancel_date(cancel_date_converted)
                        teams.append(team)
        # if there are any errors catch them here
        except BaseException as e:
            print('BaseException:', filename)
        # else print the success-statement if the file has been successfully created
        else:
            print('Data has been successfully imported from teams.txt file! \n')
        
        # press enter to end the function and go back to the menu
        input("PRESS ENTER TO GO BACK TO THE MENU")
        print("")