from django.core.exceptions import SuspiciousFileOperation
from django.template import Origin
from django.template.loaders import app_directories
from django.utils._os import safe_join


class Loader(app_directories.Loader):
    def get_template_sources(self, template_name):
        template_dirs = (
            reversed(self.get_dirs())
            if template_name.startswith('homepage')
            else self.get_dirs()
        )
        for template_dir in template_dirs:
            try:
                name = safe_join(template_dir, template_name)
            except SuspiciousFileOperation:
                # The joined path was located outside of this template_dir
                # (it might be inside another one, so this isn't fatal).
                continue

            yield Origin(
                name=name,
                template_name=template_name,
                loader=self,
            )
