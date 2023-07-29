from pyhelper.make_printable_cards_image.src.card_manager import CardManager
from pyhelper.make_printable_cards_image.src.template_manager import TemplateManager
from PIL import Image


class Territory:
    orientation = 'horizontal'
    size = 'a9'
    output_filename = ''
    # public

    def create_printable_cards_images(self):
        template_file_name = self.get_template_file_name()
        template_image = self.get_template_image(template_file_name)
        updated_image = self.add_territory_cards(template_image)
        self.save_image(updated_image)

    def get_resources():
        return {
            "Fruit": {
                "food": 2,
                "trading_ability": 1,
                "production": 0,
                "culture": 0
            },
            "Lake": {
                "food": 2,
                "trading_ability": 0,
                "production": 0,
                "culture": 1
            },
            "Silver": {
                "food": 0,
                "trading_ability": 2,
                "production": 0,
                "culture": 1
            },
            "River": {
                "food": 1,
                "trading_ability": 2,
                "production": 0,
                "culture": 1
            },
            "Pasture": {
                "food": 3,
                "trading_ability": 0,
                "production": 0,
                "culture": 0
            },
            "Metal": {
                "food": 0,
                "trading_ability": 1,
                "production": 2,
                "culture": 0
            },
            "Forest": {
                "food": 1,
                "trading_ability": 0,
                "production": 2,
                "culture": 0
            },
            "Desert": {
                "food": 0,
                "trading_ability": 1,
                "production": 0,
                "culture": 1
            },
            "Stone": {
                "food": 0,
                "trading_ability": 0,
                "production": 2,
                "culture": 1
            },
            "Gold": {
                "food": 0,
                "trading_ability": 3,
                "production": 0,
                "culture": 0
            }
        }

    # private

    def get_template_file_name(self) -> str:
        tm = TemplateManager()
        return tm.get_template_file_name_by_size(self.size, title='territory')
        return f'{self.size}.png'

    def get_template_image(self, template_file_name: str) -> Image:
        ''' PIL get image from file'''
        self.output_filename = template_file_name
        image = Image.open(template_file_name)
        return image

    def add_territory_cards(self, image: Image) -> Image:
        cm = CardManager()
        updated_image = cm.add_territory_cards(
            image, self.size, self.orientation)
        return updated_image

    def save_image(self, image: Image):
        image.save(self.output_filename)
