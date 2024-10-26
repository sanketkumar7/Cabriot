# app_name/forms.py

from django import forms
from .models import DailyDisplayAssignment, MenuItem, Ingredient, Bread

class DailyDisplayAssignmentForm(forms.ModelForm):
    class Meta:
        model = DailyDisplayAssignment
        fields = ['date', 'meal_period', 'section', 'item_name', 'quantity', 'quantity_type']

    item_name = forms.ChoiceField(choices=[], label="Item Name")

    def __init__(self, *args, **kwargs):
        super(DailyDisplayAssignmentForm, self).__init__(*args, **kwargs)
        if 'section' in self.data:
            section = self.data.get('section')
            self.fields['item_name'].choices = self.get_item_choices(section)
        elif self.instance.pk:
            section = self.instance.section
            self.fields['item_name'].choices = self.get_item_choices(section)

    def get_item_choices(self, section):
        """Fetch items based on the selected section."""
        if section == 'MenuItem':
            return [(item.id, item.name) for item in MenuItem.objects.all()]
        elif section == 'Ingredient':
            return [(item.id, item.name) for item in Ingredient.objects.all()]
        elif section == 'Bread':
            return [(item.id, item.name) for item in Bread.objects.all()]
        return []
