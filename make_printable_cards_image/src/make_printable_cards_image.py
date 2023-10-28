from src.situations.situations import Situations
from src.technologies.technologies import Technologies
from src.territory import Territory
from src.relations import Relations


class MakePrintableCardsImage:
    def territory(self):
        territory = Territory()
        territory.create_printable_cards_images()

    def relations(self):
        relations = Relations()
        relations.create_printable_cards_images()

    def technologies(self):
        techs = Technologies()
        techs.create_printable_cards_images()

    def situations(self):
        situations = Situations()
        situations.create_printable_cards_images()

    def actions(self):
        print('two')
        # Cartesian.cartesian()
