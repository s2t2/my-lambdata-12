

# teams (OOP)

class Team():

    def __init__(self, name, city, starting_pitcher_name):
        self.name = name
        self.city = city
        self.starting_pitcher_name = starting_pitcher_name

    #def __str__(self):
    #    return f"<Team {self.city} {self.name}>"
#
    #def __repr__(self):
    #    return f"<Team {self.city} {self.name}>"

    @property
    def full_name(self):
        return f"{self.city} {self.name}"

    def advertise_pitcher(self):
        print(f"HELLO PLEASE COME TO SEE OUR STARTING PITCHER {self.starting_pitcher_name} TO SEE OUR GAMES!")

    def advertise(self):
        print(f"HELLO PLEASE COME TO {self.city.upper()} TO SEE OUR GAMES!")

    @staticmethod
    def advertise_generically():
        print("HELLO PLEASE COME TO OUR GAMES!")

if __name__ == "__main__":
    team1 = Team("Terriers", "Hometown")
    print(team1.full_name)

    team2 = Team("Yankees", "New York")
    print(team2.full_name)

    team_dicts = [
        {"city": "New York", "name": "Yankees"},
        {"city": "New York", "name": "Mets"},
        {"city": "Boston", "name": "Red Sox"},
        {"city": "New Haven", "name": "Ravens"},
        {"city": "Washington", "name": "Nationals"}
    ]

    for team_d in team_dicts:
        team = Team(team_d["name"], team_d["city"])
        print(team.name)
        print(team.city)
        print(team.full_name)
        print(team.advertise_generically())
