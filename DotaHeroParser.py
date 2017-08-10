
from KeyValueParser import ValveKeyValueParser

class HeroParser:
    """ API to Parse Valve Key-Value Pairs.
    """

    # Constants
    HERO_NAME_KEYWORD          = "\"npc_dota_hero_"
    ABILITY_NAME_KEYWORD       = "\"Ability"
    FIRST_ABILITY_NAME_KEYWORD = ABILITY_NAME_KEYWORD + "1"
    END_JUNK_CHARS = 2
    OMIT_NAMES = ["base", "target_dummy"]

    def __init__(self):
        """ Inits ValveKeyValueParser.
        """

    def get_hero_list(self):
        """ Gets a list of all heroes in Dota 2

        Note:

        Args:
            npc_hero_contents (str): Hero contents to retrieve list from

        Returns:
            List of Dota 2 hero names
        """
        hero_list = []

        with open("npc_heroes") as npc_hero_contents:
            for line in npc_hero_contents:
                line = line.lstrip()
                hero_name = self.get_hero_name(line)

                if hero_name != "":
                    hero_list.append(hero_name)
                # this into adding to list then return hero list name
        # print(hero_list)
        return hero_list

    def get_hero_ability_list(self):
        """ Gets a dictionary of all heroes and their abilities

        Note:
            Dictionary is the following format: <hero_name, <ability_1, ability_2, ... >
        Args:
            npc_hero_contents (str): Hero contents to retrieve list from

        Returns:
            Dictionary of Dota 2 Heros and their abilities
        """
        hero_ability_dict = { }
        hero_list  = self.get_hero_list()
        #hero index
        i = 0
        is_reading_abilities = False

        with open("npc_heroes") as npc_hero_contents:
            for line in npc_hero_contents:
                line = line.lstrip()
                # Enable Ability parsing
                if line.startswith(self.FIRST_ABILITY_NAME_KEYWORD):
                    is_reading_abilities = True

                # Disable ability parsing
                if not line.startswith(self.ABILITY_NAME_KEYWORD):
                    is_reading_abilities = False

                if is_reading_abilities:
                    abilityKeyVal = ValveKeyValueParser.get_key_value(line)
                    print(abilityKeyVal)
                # Found the hero to get abilities for
                # if line.startswith(self.HERO_NAME_KEYWORD + hero_list[i]):

                    # hero_ability_dict[hero_list[i]]
                #if hero_name != "":
                  #  hero_list.append(hero_name)
                # this into adding to list then return hero list name
        # print(hero_list)
        return hero_list



    def get_hero_name(self, npc_hero_line):
        """ Attempts to get a hero name from the line

        Note:

        Args:
            npc_hero_line (str): Line from Valve's npc_heroes text file

        Returns:
            Hero name if found, otherwise empty string.
        """
        hero_name = ""

        if npc_hero_line.startswith(self.HERO_NAME_KEYWORD):
            hero_name_start_index = npc_hero_line.find(self.HERO_NAME_KEYWORD) + len(self.HERO_NAME_KEYWORD)
            hero_name_end_index   = len(npc_hero_line) - self.END_JUNK_CHARS
            hero_name             = npc_hero_line[hero_name_start_index:hero_name_end_index]

        return hero_name

