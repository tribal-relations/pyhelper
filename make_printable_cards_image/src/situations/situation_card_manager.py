from curses import killchar
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math
from src.card_manager import CardManager
from src.dashed_image_draw import DashedImageDraw
from src.data import Data
import random

A4WIDTH = 2479
A4HEIGHT = 3508

class SituationCardManager:
    def __init__(self):
        self.card_manager = CardManager()
        # dpi 300 with dynamic margins
        # self.page_margin = 80  # from all sides
        self.vertical_page_margin = 160
        self.horizontal_page_margin = 80
        height_with_margins = A4HEIGHT - (2 * self.vertical_page_margin)
        width_with_margins = A4WIDTH - (2 * self.horizontal_page_margin)

        self.a9_vertical_step = math.floor(height_with_margins / 8)
        self.a9_horizontal_step = math.floor(width_with_margins / 4)
        self.card_left_margin = 20
        
        # dpi 300 with margins to accomodate smaller cardboard
        # 2479x3508 px => 2319x3348
        # page_margin = 80  # from all sides
        # a9_vertical_step = 418
        # a9_horizontal_step = 580
        # card_left_margin = 80

        # dpi 300
        # a9_vertical_step = 438
        # a9_horizontal_step = 620
        # card_left_margin = 80

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

    def add_cards(self, image: Image, size: str, orientation: str) -> Image:
        if (self.size_to_orientation_map[size] != orientation):
            image = self.rotate_image_90(image)
        image = self.make_blank(image)

        cards_count = self.size_to_cards_number_map[size]
        resources_keys = self.get_situations_keys(size)
        resources_keys_count = len(resources_keys)
        for index in range(cards_count):
            image = self.add_card_to_image(
                image, size, index, resources_keys[index % resources_keys_count])

        return image

    # private

    def add_card_to_image(self, image: Image, size: str, index: int, tech_key: str) -> Image:
        x, y = self.card_manager.get_coordinates_by_size(size, index)
        image = self.insert_card(image, x, y, tech_key)
        return image

    def insert_card(self, image: Image, x: int, y: int, tech_key: str) -> Image:
        assert (image != None)
        image = self.draw_border(image, x, y)
        image = self.write_card(image, x, y, tech_key)
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

    def write_card(self, image: Image, x: int, y: int, tech_key: str) -> Image:
        image_draw = ImageDraw.Draw(image)
        font_path = '/Users/gena/Library/Fonts/NotoSansMono-Regular.ttf'
        my_font = ImageFont.truetype(font_path, 50)

        black = (0, 0, 0)
        resource = Data.get_situations()[tech_key]
        image_draw.text(
            (x + self.card_left_margin, y),
            tech_key,
            font=my_font,
            fill=black
        )

        self.card_manager.write_multiline_text(image, x, y, resource['description'],ImageFont.truetype(font_path, 40), 20)

        return image

    def wrap_string(self, target, wrap)->str:
        return target
        res = ''
        total_lines = len(target) // wrap
        for i in range(0, total_lines, wrap):
            res += target[i:wrap] + "\n"
        return res

    def get_situations_keys(self, size: str) -> dict:
        resources = Data.get_situations()
        keys = list(resources.keys())
        weights = []
        for k in keys:
            weights.append(resources[k]['quantity'])

        resource_keys = random.choices(
            keys, weights, k=self.size_to_cards_number_map[size])
        return resource_keys

