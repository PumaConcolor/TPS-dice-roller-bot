DICE_ROLL_REGEX = '[\\w|\\s|!-/|:-@]*?[\\s]' \
                  '([0-9]*[\\s]*)d[\\s]*([0-9]+)' \
                  '[\\s]*([\\+|\\-][\\s]*[0-9]*)*[\\s]*(.*)[\\s]*$'

HELP_MESSAGE = ('I can roll dice and do funny stuff!\n\n'
                'You can control me by sending these commands:\n\n'
                '/help - sends this help message\n'
                '/start - sends this help message\n\n'
                'To roll dice (each command has a long and short version):\n\n'
                '/roll - roll dice as indicated using dice notation\n'
                '/r - short version\n\n'
                '/ability_scores - rolls six ability scores for use in D&D style game systems\n'
                '/as - short version\n\n'
                '/alive - returns the emotional state of the bot\n'
                '/spongebob - takes your sentence and returns a saltier one\n'
                '/sp - short version\n\n'
                '/spongerep - reply to a message writing this, it will mock the first message\n'
                '/spr - short version\n\n'
                '/edgelord - give your character a reason to brood\n'
                'this command is the only one to just have a long version, for added edginess\n\n'
                '/character - creates a fully fledged character\n'
                '/char - short version')

ALIVE_SERVICE=[
    'Alive and kicking',
    'Lock \'n loaded',
    'My life for DnD',
    'Stop poking me',
    'I like when you try to reach me',
    'I\'m alive, not by my choice',
    'What does "alive" means?',
    'I\'m alive, be grateful to Pelor',
    'Who\'s summoning me?',
    '(/^▽^)/',
    '(つ ͡° ͜ʖ ͡°)つ',
    '(╯°□°）╯︵ ┻━┻',
    'ಠ_ಠ'
]

EDGELORD_PARTS=[
    # Edgy antagonist
    [
        'An evil wizard',
        'A dragon',
        'The drow',
        'Goblins',
        'Kobolds',
        'A mind flayer',
        'Evil cultists',
        'Orcs',
        'Trolls',
        'A banshee',
        'A demon lord',
        'An archdevil',
        'Giants',
        'Vampires',
        'Gnolls',
        'A werefolf',
        'A Djinni',
        'A mimic',
        'A tarrasque',
        'A beholder',
        'A hag coven',
        'A lich',
        'Barbarians',
        'An aboleth',
        'A succubus',
        'A criminal organizations',
        'A gelatinous cube',
        'A necromancer',
        'Corrupt nobles',
        'A death knight',
        'The BBEG',
        'The bard',
        'Natural selection',
        'The DM',
    ],
    # Edgy action
    [
        'killed',
        'murdered',
        'slaughtered',
        'massacred',
        'assassinated',
        'brainwashed',
        'captured',
        'banished',
        'enslaved',
        'betrayed',
        'sacrificed',
        'mauled',
        'stole',
        'blackmailed',
        'conned',
        'framed',
        'humiliated',
        'pillaged',
        'ruined',
        'ate',
        'cursed',
        'befriended',
        'seduced'
    ],
    # Edgy victim
    [
        'my family',
        'my hometown',
        'my parents',
        'my clan',
        'my sibling',
        'my mentors',
        'my significant other',
        'my master',
        'my side squeeze',
        'my apprentice',
        'my friends',
        'my previous adventuring party',
        'everyone I knew',
        'my crew of sailors',
        'my crew of pirates',
        'my crew of noble outlaws',
        'my crew of thieves',
        'the tavern I basically lived in',
        'my military unit',
        'my social status',
        'my treasure',
        'my aspirations',
        'my honour',
        'my confidence',
        'my imaginary friends'
    ],
    #Edgy outcome
    [
        'and it will have no effect on how i roleplay my character',
        'and now I\'m a murder hobo',
        'and now I\'m a lawful good stick in the mud',
        'and now I seek vengeance',
        'and now I trust no one',
        'and now I have a bleak outlook of the world',
        'and now I strive to live by their ideals',
        'and now I must become stronger',
        'and now I seek to bring back what I have lost',
        'and now I vow to prevent that from happening to anyone else',
        'and now I am haunted by their memory',
        'and now I seek to uncover the truth about what happened',
        'and now I fear it will happen again',
        'and now I am stronger because of it',
        'and now I\'m and alcoholic',
        'and now I have multiclassed into warlock',
        'and now I\'m Batman'
    ]
]

PG_CREATION_PARTS={
    'Sex': [
     'Male',
     'Female',
     'You choose'
    ],
    'Sexual orientation': [
      'Heterosexual',
      'Homosexual',
      'Bisexual',
      'Pansexual',
      'Asexual',
      'you choose'
    ],
    'Race': [
        'Aarakocra',
        'Aasimar (Fallen)',
        'Aasimar (Protector)',
        'Aasimar (Scourge)',
        'Bugbear',
        'Centaur',
        'Changeling',
        'Dragonborn (Base)',
        'Dragonborn (Draconblood)',
        'Dragonborn (Ravenite)',
        'Dwarf',
        'Dwarf (Duergar)',
        'Dwarf (Hill)',
        'Dwarf (Mark of Warding)',
        'Dwarf (Mountain)',
        'Elf (Drow)',
        'Elf (Eladrin)',
        'Elf (High)',
        'Elf (Mark of Shadow)',
        'Elf (Pallid)',
        'Elf (Sea)',
        'Elf (Shadar-kai)',
        'Elf (Wood)',
        'Firbolg',
        'Genasi (Air)',
        'Genasi (Earth)',
        'Genasi (Fire)',
        'Genasi (Water)',
        'Gith (Githyanki)',
        'Gith (Githzerai)',
        'Gnome (Deep)',
        'Gnome (Deep/Svirfneblin)',
        'Gnome (Forest)',
        'Gnome (Mark of Scribing)',
        'Gnome (Rock)',
        'Goblin',
        'Goliath',
        'Half-Elf',
        'Half-Elf (Variant)',
        'Half-Elf (Variant; Aquatic Elf Descent)',
        'Half-Elf (Variant; Drow Descent)',
        'Half-Elf (Variant; Mark of Detection)',
        'Half-Elf (Variant; Mark of Storm)',
        'Half-Elf (Variant; Moon Elf or Sun Elf Descent)',
        'Half-Elf (Variant; Wood Elf Descent)',
        'Half-Orc',
        'Half-Orc (Mark of Finding)',
        'Halfling (Ghostwise)',
        'Halfling (Lightfoot)',
        'Halfling (Lotusden)',
        'Halfling (Mark of Healing)',
        'Halfling (Mark of Hospitality)',
        'Halfling (Stout)',
        'Hobgoblin',
        'Human (Base)',
        'Human (Mark of Finding)',
        'Human (Mark of Handling)',
        'Human (Mark of Making)',
        'Human (Mark of Passage)',
        'Human (Mark of Sentinel)',
        'Human (Variant)',
        'Kalashtar',
        'Kenku',
        'Kobold',
        'Leonin',
        'Lizardfolk',
        'Loxodon',
        'Minotaur',
        'Orc',
        'Satyr',
        'Shifter (Beasthide)',
        'Shifter (Longtooth)',
        'Shifter (Swiftstride)',
        'Shifter (Wildhunt)',
        'Simic Hybrid',
        'Tabaxi',
        'Tiefling (Asmodeus)',
        'Tiefling (Baalzebul)',
        'Tiefling (Base)',
        'Tiefling (Dispater)',
        'Tiefling (Fierna)',
        'Tiefling (Glasya)',
        'Tiefling (Levistus)',
        'Tiefling (Mammon)',
        'Tiefling (Mephistopheles)',
        'Tiefling (Variant; Devil\'s Tongue)',
        'Tiefling (Variant; Hellfire)',
        'Tiefling (Variant; Infernal Legacy)',
        'Tiefling (Variant; Winged)',
        'Tiefling (Zariel)',
        'Triton',
        'Vedalken',
        'Verdan',
        'Warforged',
        'Yuan-ti Pureblood',
        'You choose'
    ],
    'Class': [
        'Artificer',
        'Barbarian',
        'Bard',
        'Cleric',
        'Druid',
        'Fighter',
        'Monk',
        'Paladin',
        'Ranger',
        'Rogue',
        'Sorcerer',
        'Warlock',
        'Wizard',
        'You choose'
    ],
    'Background': [
        'Acolyte',
        'Anthropologist',
        'Archaeologist',
        'Athlete',
        'Augen Trust (Spy)',
        'Azorius Functionary',
        'Boros Legionnaire',
        'Celebrity Adventurer\'s Scion',
        'Charlatan',
        'City Watch',
        'Variant City Watch (Investigator)',
        'Clan Crafter',
        'Cloistered Scholar',
        'Cobalt Scholar (Sage)',
        'Courtier',
        'Criminal',
        'Variant Criminal (Spy)',
        'Dimir Operative',
        'Entertainer',
        'Variant Entertainer (Gladiator)',
        'Faceless',
        'Faction Agent',
        'Failed Merchant',
        'Far Traveler',
        'Fisher',
        'Folk Hero',
        'Gambler',
        'Golgari Agent',
        'Grinner',
        'Gruul Anarch',
        'Guild Artisan',
        'Variant Guild Artisan (Guild Merchant)',
        'Haunted One',
        'Hermit',
        'House Agent',
        'Inheritor',
        'Izzet Engineer',
        'Knight of the Order',
        'Luxonborn (Acolyte)',
        'Marine',
        'Mercenary Veteran',
        'Myriad Operative (Criminal)',
        'Noble',
        'Variant Noble (Knight)',
        'Orzhov Representative',
        'Outlander',
        'Plaintiff',
        'Rakdos Cultist',
        'Revelry Pirate (Sailor)',
        'Rival Intern',
        'Sage',
        'Sailor',
        'Variant Sailor (Pirate)',
        'Selesnya Initiate',
        'Shipwright',
        'Simic Scientist',
        'Smuggler',
        'Soldier',
        'Urban Bounty Hunter',
        'Urchin',
        'Uthgardt Tribe Member',
        'Volstrucker Agent',
        'Waterdhavian Noble',
        'You choose'
    ]
}
