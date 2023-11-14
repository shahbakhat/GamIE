from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Customize the appearance and behavior of file inputs used in the forms.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    Input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'