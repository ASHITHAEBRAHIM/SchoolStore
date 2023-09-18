from django import forms
from .models import std_form,department,course
choices = [
    ('M', 'Male'),
    ('F', 'Female'),
]
materials_choices = [
    ('Notebook', 'Notebook'),
    ('Pen', 'Pen'),
    ('Exam Paper', 'Exam paper'),
    ('Pencil', 'Pencil'),
    ('Scale', 'Scale'),
    ('Eraser', 'Eraser'),
    ('Sharpener', 'Sharpener')
]
class regform_form(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=choices,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'}))
    materials_provided = forms.MultipleChoiceField(
        choices=materials_choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        model = std_form
        widgets = {'DOB':forms.DateInput(attrs={'type':'date','placeholder':'yyyy-mm-dd','class':'form-control'})}
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')

