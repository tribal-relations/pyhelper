import datetime


class TemplateManager:
    template_storage_dir = 'storage/templates'
    output_storage_dir = 'storage/output'

    size_to_filename_map = {
        'a8': f'{template_storage_dir}/a8.png'
    }

    def get_template_file():
        pass

    def get_template_file_name_by_size(self, size: str, title='') -> str:
        ''' to not accidentally edit templates, create output beforehand'''

        datetime.datetime.microsecond = 0
        timestamp = datetime.datetime.isoformat()
        return f'{self.output_storage_dir}/{size}_{title}_{timestamp}.png'

        return self.size_to_filename_map[size]
