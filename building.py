from datetime import date

class Building:
    
    def __init__(self, address, stories):
        self.designer = "Alyssa Nycum"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        today = date.today()
        self.date_constructed = today.strftime("%m/%d/%y")

    def purchase(self, ownerName):
        self.owner = ownerName

    def print_details(self):
        print(f"{self.address} was purchased by {self.owner} from {self.designer} on {self.date_constructed} and has {self.stories} stories.")