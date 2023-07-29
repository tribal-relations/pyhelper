import datetime
import os

class TemplateManager:
    root_dir = '/Users/gena/code/projects/tribal-relations/pyhelper'
    template_storage_dir = 'storage/templates/dpi300'
    output_storage_dir = 'storage/output'

    size_to_filename_map = {
        'a8': f'{template_storage_dir}/a8.png'
    }

    def get_template_file():
        pass

    def get_template_file_name_by_size(self, size: str, title='') -> str:
        ''' to not accidentally edit templates, create output beforehand'''

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        
        template_filename = f'{self.root_dir}/{self.template_storage_dir}/{size}.png'
        new_filename = f'{self.root_dir}/{self.output_storage_dir}/{size}_{title}_{timestamp}.png'
        # return template_filename, new_filename
        # print(f'cp {template_filename} {new_filename}')
        # exit()

        os.system(f'cp {template_filename} {new_filename}')
        return f'{self.output_storage_dir}/{size}_{title}_{timestamp}.png'

        return self.size_to_filename_map[size]
