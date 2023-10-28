class Data:
    def get_resources():
        return {
            "Metal": {
                "quantity": 10,
                "food": 0,
                "wealth": 1,
                "production": 2,
                "culture": 0
            },
            "Fruit": {
                "quantity": 8,
                "food": 2,
                "wealth": 1,
                "production": 0,
                "culture": 0
            },
            "Lake": {
                "quantity": 4,
                "food": 2,
                "wealth": 0,
                "production": 0,
                "culture": 1
            },
            "Forest": {
                "quantity": 20,
                "food": 1,
                "wealth": 0,
                "production": 2,
                "culture": 0
            },
            "River": {
                "quantity": 6,
                "food": 1,
                "wealth": 2,
                "production": 0,
                "culture": 1
            },
            "Pasture": {
                "quantity": 10,
                "food": 3,
                "wealth": 0,
                "production": 0,
                "culture": 0
            },
            "Stone": {
                "quantity": 10,
                "food": 0,
                "wealth": 0,
                "production": 2,
                "culture": 1
            },
            "Gold": {
                "quantity": 2,
                "food": 0,
                "wealth": 4,
                "production": 0,
                "culture": 0
            },
            "Silver": {
                "quantity": 4,
                "food": 0,
                "wealth": 2,
                "production": 0,
                "culture": 1
            },
            "Desert": {
                "quantity": 6,
                "food": 0,
                "wealth": 1,
                "production": 0,
                "culture": 1
            }
        }

    def get_relations():
        return {
            "Equals": {
                "name": "Equals",
                "agent_bonus": 0,
                "recipient_bonus": 0
            },
            "Respectable": {
                "name": "Respectable",
                "agent_bonus": 1,
                "recipient_bonus": 2
            },
            "Proteges": {
                "name": "Proteges",
                "agent_bonus": 1,
                "recipient_bonus": 4
            },
            "KnowItAlls": {
                "name": "KnowItAlls",
                "agent_bonus": 1,
                "recipient_bonus": -1
            },
            "Barbarians": {
                "name": "Barbarians",
                "agent_bonus": 1,
                "recipient_bonus": -2
            },
            "Rogues": {
                "name": "Rogues",
                "agent_bonus": 2,
                "recipient_bonus": -1
            },
            "Bourgeois": {
                "name": "Bourgeois",
                "agent_bonus": 2,
                "recipient_bonus": 0
            },
            "Mates": {
                "name": "Mates",
                "agent_bonus": 2,
                "recipient_bonus": 2
            },
            "Idols": {
                "name": "Idols",
                "agent_bonus": 3,
                "recipient_bonus": 2
            },
            "Cannibals": {
                "name": "Cannibals",
                "agent_bonus": 0,
                "recipient_bonus": -3
            }
        }

    def get_technologies():
        return {
            "Pottery": {
                "name": "Pottery",
                "description": "Harvest result +2",
                "prerequisites": {}
            },
            "Animal Husbandry": {
                "name": "Animal Husbandry",
                "description": "Pasture +2 Food",
                "prerequisites": {}
            },
            "Hunting": {
                "name": "Hunting",
                "description": "Forest +1 Food",
                "prerequisites": {}
            },
            "Plough": {
                "name": "Plough",
                "description": "Harvest result +2. Throw 2 dice if Animal Husbandry is discovered",
                "prerequisites": {
                    "Calendar": True
                }
            },
            "Advanced Writing": {
                "name": "Advanced Writing",
                "description": "Culture *2",
                "prerequisites": {
                    "Primitive Writing": True
                }
            },
            "Fishing": {
                "name": "Fishing",
                "description": "River and Lake +2 Food",
                "prerequisites": {}
            },
            "Archery": {
                "name": "Archery",
                "description": "Combat Readiness *2",
                "prerequisites": {}
            },
            "Organized Army": {
                "name": "Organized Army",
                "description": "Combat Readiness *3",
                "prerequisites": {
                    "Bronze Weapons": True
                }
            },
            "Musical Instruments": {
                "name": "Musical Instruments",
                "description": "Culture *2",
                "prerequisites": {}
            },
            "Bronze Weapons": {
                "name": "Bronze Weapons",
                "description": "Metal +1 Wealth +1 Production. Combat Readiness *2",
                "prerequisites": {
                    "Stone Working": True
                }
            },
            "Idols": {
                "name": "Idols",
                "description": "Stone +2 Culture",
                "prerequisites": {
                    "Stone Working": True
                }
            },
            "Poetry": {
                "name": "Poetry",
                "description": "Culture *2",
                "prerequisites": {}
            },
            "Calendar": {
                "name": "Calendar",
                "description": "Food *2",
                "prerequisites": {
                    "Primitive Writing": True
                }
            },
            "Primitive Writing": {
                "name": "Primitive Writing",
                "description": "Wealth +3",
                "prerequisites": {
                    "Pottery": True
                }
            },
            "Stone Working": {
                "name": "Stone Working",
                "description": "Stone +2 Production +1 Culture",
                "prerequisites": {}
            }
        }

    def get_situations():
        return {
            "Columbus": {
                "name": "Columbus",
                "description": "Only you can discover new tiles next round",
                "quantity": 2
            },
            "Vulnerability": {
                "name": "Vulnerability",
                "description": "Rome is weaker 1000pts next round",
                "quantity": 2
            },
            "Nothing": {
                "name": "Nothing",
                "description": "Nothing happens",
                "quantity": 10
            },
            "Flood": {
                "name": "Flood",
                "description": "Remove River tile. If you don't have one - remove one from the next player",
                "quantity": 5
            },
            "Nessie": {
                "name": "Nessie",
                "description": "Remove Lake tile. If you don't have one - remove one from the next player",
                "quantity": 1
            },
            "Desertification": {
                "name": "Desertification",
                "description": "Turn one Pasture tile into Desert. If you don't have one - do so with one from the next player",
                "quantity": 2
            },
            "Blessing": {
                "name": "Blessing",
                "description": "+1 Action this round",
                "quantity": 2
            },
            "Divine Shield": {
                "name": "Divine Shield",
                "description": "You win every fight if defending",
                "quantity": 2
            },
            "Forest Fire": {
                "name": "Forest Fire",
                "description": "Remove Forest tile. If you don't have one - remove one from the next player",
                "quantity": 4
            },
            "Pacifism": {
                "name": "Pacifism",
                "description": "Nobody can arm next round",
                "quantity": 5
            }
        }
