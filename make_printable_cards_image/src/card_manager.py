from curses import killchar
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math
import random
from src.dashed_image_draw import DashedImageDraw
from src.data import Data


class CardManager:
    # dpi 300
    a9_vertical_step = 438
    a9_horizontal_step = 620
    # dpi 72
    # a9_vertical_step = 105 * 4
    # a9_horizontal_step = 149 * 4
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
        if (self.size_to_orientation_map[size] != orientation):
            image = self.rotate_image_90(image)
        image = self.make_blank(image)

        cards_count = self.size_to_cards_number_map[size]
        resources_keys = self.get_random_resources_keys(size)
        assert(cards_count == len(resources_keys))
        for index in range(cards_count):
            image = self.add_card_to_image(image, size, index, resources_keys[index])

        return image

    # private

    def add_card_to_image(self, image: Image, size: str, index: int, resource_key: str) -> Image:
        x, y = self.get_coordinates_by_size(size, index)
        image = self.insert_card(image, x, y, resource_key)
        return image

    def get_coordinates_by_size(self, size: str, index: int):
        if (index == 0):
            return 0, 0

        in_a_row = self.size_to_cards_in_a_row_map[size]
        horizontal_coefficient = self.a9_horizontal_step * (index % in_a_row)
        vertical_coefficient = self.a9_vertical_step * \
            math.floor(index / in_a_row)

        return horizontal_coefficient, vertical_coefficient

    def insert_card(self, image: Image, x: int, y: int, resource_key: str) -> Image:
        assert (image != None)
        image = self.draw_border(image, x, y)
        image = self.write_card(image, x, y, resource_key)
        return image

    def make_blank(self, image: Image) -> Image:
        white = (255, 255, 255)
        draw = ImageDraw.Draw(image)
        draw.rectangle(
            [(0, 0), image.size],
            fill=white
        )
        return image

    def draw_border(self, image: Image, x: int, y: int) -> Image:
        d = DashedImageDraw(image)

        d.dashed_rectangle(
            [(x, y), (x + self.a9_horizontal_step, y + self.a9_vertical_step)],
            dash=(5, 40),
            outline='black',
            width=1
        )

        return image

    def write_card(self, image: Image, x: int, y: int, resource_key: str) -> Image:
        image_draw = ImageDraw.Draw(image)
        font_path = '/Users/gena/Library/Fonts/NotoSansMono-Regular.ttf'
        my_font = ImageFont.truetype(font_path, 76)

        black = (0, 0, 0)
        resource = Data.get_resources()[resource_key]
        image_draw.text(
            (x + 10, y),
            resource_key,
            font=my_font,
            fill=black
        )

        i = 0
        for key, value in resource.items():
            if key == 'quantity':
                continue
            width_in_chars = 15
            spaces = width_in_chars - 1 - len(key)
            if value != 0:
                image_draw.text(
                    (x + 20, y + (130 + (i * 70))),
                    key + ' ' * spaces + str(value),
                    font=ImageFont.truetype(font_path, 44),
                    fill=black
                )
            i += 1
        return image


    def get_random_resource(self, ) -> dict:
        resources = Data.get_resources()
        keys = list(resources.keys())
        resource_key = random.choice(keys)
        return resource_key, resources[resource_key]
    
    def get_random_resources_keys(self, size: str) -> dict:
        resources = Data.get_resources()
        keys = list(resources.keys())
        weights = []
        for k in keys:
            weights.append(resources[k]['quantity'])

        resource_keys = random.choices(keys, weights, k=self.size_to_cards_number_map[size])
        return resource_keys