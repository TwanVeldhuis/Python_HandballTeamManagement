# Creating the team itself

class Team():
    # the team ID that starts with number 0
    id = 0
    
    # __init__ method creates the attributes, with certain input
    def __init__(self, date, team_name, team_type, fee_paid, enterance_fee):
        # the team ID is assigned to the __id property
        self.__id = Team.id
        self.__date = date
        self.__name = team_name
        self.__type = team_type
        self.__fee_paid = fee_paid
        self.__fee = enterance_fee
        self.__cancel_date = None
        # the team ID is brought up 1 index point so for the next team it is 1+
        Team.id += 1
    
    # function to get the ID of the current team
    def get_team_id(self):
        return self.__id
    
    # function to get the creation date of the current team
    def get_team_date(self):
        return self.__date
    
    # function to get the name of the current team
    def get_team_name(self):
        return self.__name
    
    # function to get the type (boys or girls) of the current team
    def get_team_type(self):
        return self.__type
    
    # function to get if the current team paid the fee (True or False)
    def get_team_fee_paid(self):
        return self.__fee_paid
    
    # function to get the fee amount of the current team
    def get_team_fee(self):
        return self.__fee
    
    # function to get cancellation date of the current team
    def get_cancel_date(self):
        return self.__cancel_date
    
    # function to set a new name for the current team
    def set_team_name(self, team_name):
        self.__name = team_name
    
    # function to set a new type (boys or girls) for the current team
    def set_team_type(self, team_type):
        self.__type = team_type
    
    # function to set/change if the current team paid the fee (True or False)
    def set_team_fee_paid(self, team_fee_paid):
        self.__fee_paid = team_fee_paid
    
    # function to set a new fee amount for the current team
    def set_team_fee(self, team_enterance_fee):
        self.__fee = team_enterance_fee
    
    # function to set the cancellation date for the current team
    def set_cancel_date(self, team_cancellation_date):
        self.__cancel_date = team_cancellation_date
    
    # function that returns the object as a string
    def __str__(self):
        string = ("======= TEAM INFO ======= \n")
        string += (f"Team ID:           {self.__id} \n")
        string += (f"Registration Date: {self.__date} \n")
        string += (f"Team Name:         {self.__name} \n")
        string += (f"Team Type:         {self.__type} \n")
        string += (f"Fee Paid:          {self.__fee_paid} \n")
        string += (f"Fee Amount:        {self.__fee} \n")
        if self.__cancel_date:
            string += (f"Cancellation Day:  {self.__cancel_date} \n")
        return string