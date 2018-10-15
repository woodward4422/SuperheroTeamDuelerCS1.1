import random


class Ability:

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        max_attack = self.attack_strength
        min_attack = max_attack // 2
        attack = random.randint(min_attack, max_attack)
        return attack

        # Return attack va lue

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength


class Hero:

    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        total_armor = 0
        for items in self.armors:
            total_armor += items.defend()
        return total_armor

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the 
        hero's health. 

        If the hero dies update number of deaths.
        """

        self.health -= damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_attack = 0
        for item in self.abilities:
            total_attack += item.attack()
        return total_attack
    
    def add_armor(self,armor):
        self.armors.append(armor)


    # Call the attack method on every ability in our ability list
    # Add up and return the total of all attacks

class Weapon(Ability):

    def attack(self):
        max_attack = self.attack_strength
        attack = random.randint(0, max_attack)
        return attack


class Team:

    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return
        return 0

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """

        
        total_damage = 0 
        print("Total Damage: {}".format(total_damage))
        total_kills = 0
        print("Total Kills: {}".format(total_kills))

        for hero in self.heroes:
            print("Hero: {}".format(hero.name))
            total_damage += hero.attack()
            print("Damage: {}".format(total_damage))
        
        # for other_hero in other_team.heroes:
        #     print("OtherHero: {}".format(other_hero.name))
        
        total_kills = other_team.defend(total_damage)
        print("total_kills: {}".format(total_kills))
        
        

        for hero in self.heroes:
            print("HERE")
            hero.add_kill(total_kills)



        


    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """

        total_armor = 0
        for hero in self.heroes:
            total_armor += hero.defend()
            print("total armor {}".format(total_armor))

        damage_through_armor = damage_amt - total_armor
        print("dmage thru armor: {}".format(damage_through_armor))
        if damage_through_armor < 0:
            damage_through_armor = 0

        divided_damage = damage_through_armor / len(self.heroes)
        death_counter = 0
        for hero in self.heroes:
            hero.take_damage(divided_damage)
            if hero.health < 0:
                death_counter += 1
        print("Death count: {}".format(death_counter))
        # returns an int
        return death_counter

    

    def revive_heroes(self, health=60):
        """
        This method should reset all heroes health to their
        original starting value.
        """

        for hero in self.heroes:
            hero.health = health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen. 

        This data must be output to the terminal.
        """

        for hero in self.heroes:
            ratio = hero.kills / hero.deaths
            print(str(ratio))

    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """

        for hero in self.heroes:
            hero.kills += 1


class Armor:

    def __init__(self, name, defense):

        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
       

    def build_team_one(self,team_name):
      self.team_one = Team(input('What should we call team one?:'))
      for _ in range(0,3):
          add_hero = input('Name for the hero to be added:')
          self.team_one.add_hero(add_hero)
          

    def build_team_two(self,team_name):
      self.team_one = Team(input('What should we call team two?:'))
      for _ in range(0,3):
          add_hero = input('Name for the hero to be added:')
          self.team_one.add_hero(add_hero)

    def team_battle(self):
        """
        This method should continue to battle teams until 
        one or both teams are dead.
        """
        self.team_one.attack(self.team_two)
        self.team_two.attack(self.team_one)

        

    def show_stats(self):
        """
        This method should print out the battle statistics 
        including each heroes kill/death ratio.
        """
        
        self.team_one.stats()
        self.team_two.stats()


if __name__ == '__main__':
    hero = Hero('Wonder Woman')
    print(hero.attack())
    ability = Ability('Divine Speed', 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability('Sup Homie', 800)
    hero.add_ability(new_ability)
    print(hero.attack())


