#!/usr/bin/env python 3
from DotaHeroParser import HeroParser

if __name__ == '__main__':
    test_line = "\"npc_dota_hero_antimage\"\nnot hero line\n\"npc_dota_hero_axe\""
    parser    = HeroParser()

    parser.get_hero_ability_list()
