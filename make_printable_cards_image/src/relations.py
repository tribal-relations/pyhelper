from src.relations_card_manager import RelationsCardManager
from src.template_manager import TemplateManager
from PIL import Image


class Relations:
    def __init__(self) -> None:
        self.orientation = 'vertical'
        self.size = 'a8'
        self.output_filename = ''
    
    # public
    
    def create_printable_cards_images(self):
        template_file_name = self.get_template_file_name()
        template_image = self.get_template_image(template_file_name)
        updated_image = self.add_relations_cards(template_image)
        self.save_image(updated_image)


    # private

    def get_template_file_name(self) -> str:
        tm = TemplateManager()
        return tm.get_template_file_name_by_size(self.size, title='relations')
        return f'{self.size}.png'

    def get_template_image(self, template_file_name: str) -> Image:
        ''' PIL get image from file'''
        self.output_filename = template_file_name
        image = Image.open(template_file_name)
        return image

    def add_relations_cards(self, image: Image) -> Image:
        cm = RelationsCardManager()
        updated_image = cm.add_cards(
            image, self.size, self.orientation)
        return updated_image

    def save_image(self, image: Image):
        image.save(self.output_filename)