import random


class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
       max_attack = self.attack_strength
       min_attack = max_attack // 2
       attack = random.randint(min_attack,max_attack)
       return attack
        # Return attack value

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength
    
class Hero:  
     
    def __init__(self, name):
        self.abilities = list()
        self.name = name

        
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    

    def attack(self):
        total_attack = 0
        for items in self.abilities:
            total_attack += items.attack()
        return total_attack
    # Call the attack method on every ability in our ability list
    # Add up and return the total of all attacks 

class Weapon(Ability):
    def attack(self):
        max_attack = self.attack_strength
        attack = random.randint(0,max_attack)
        return attack 
    
class Team:
    def init(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        heroes.append(Hero)

    def remove_hero(self, name):
        if name in self.heroes:
            self.heroes.remove(name)
        else:
            return 0


    def find_hero(self, name):
        if name in self.heroes:
            return name
        else:
            return 0
    

    def view_all_heroes(self):
        for heroe in self.heroes:
            print(heroe)
    
    

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Sup Homie", 800)
    hero.add_ability(new_ability)
    print(hero.attack())



    

        

    

