from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math
import random
import json
from pyhelper.make_printable_cards_image.src.territory import Territory


class CardManager:
    a9_vertical_step = 105
    a9_horizontal_step = 149
    size_to_orientation_map = {
        'a8': 'vertical',
        'a9': 'horizontal',

    }
    size_to_cards_number_map = {
        'a8': 16,
        'a9': 32,
    }

    '''portrait'''
    size_to_cards_in_a_row_map = {
        'a8': 4,
        'a9': 4,
    }

    # public

    def add_territory_cards(self, image: Image, size: str, orientation: str) -> Image:
        ''' this place knows '''
        if (self.size_to_orientation_map[size] != orientation):
            image = self.rotate_image_90(image)

        for index in range(self.size_to_cards_number_map[size]):
            image = self.add_card_to_image(image, size, index)

        return image

    # private

    def add_card_to_image(self, image: Image, size: str, index: int) -> Image:
        x, y = self.get_coordinates_by_size(size, index)
        image = self.insert_card(image, x, y)
        return image

    def get_coordinates_by_size(self, size: str, index: int):
        if (index == 0):
            return 0, 0

        in_a_row = self.size_to_cards_in_a_row_map[size]
        horizontal_coefficient = self.a9_horizontal_step * (index % in_a_row)
        vertical_coefficient = self.a9_vertical_step * \
            math.floor(index / in_a_row)

        return horizontal_coefficient, vertical_coefficient

    def insert_card(self, image: Image, x: int, y: int) -> Image:
        image_draw = ImageDraw.Draw(image)
        my_font = ImageFont.truetype('FreeMono.ttf', 16)
        black = (0, 0, 0)
        resource_name, resource = self.get_random_resource()
        image_draw.text(
            (x, y), 
            resource_name,
            font=my_font,
            fill=black
        )
        
        description = json.dumps(resource)
        image_draw.text(
            (x, y), 
            description,
            font=ImageFont.truetype('FreeMono.ttf', 8),
            fill=black
        )
        return image
    
    def get_random_resource(self, ) -> dict:
        resources = Territory.get_resources()
        l = len(resources)
        resource_key = random.choice(resources.keys())
        return resource_key, resources[resource_key]