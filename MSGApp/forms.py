from django import forms  
from MSGApp.models import   UploadForm  #models.py
     
class UploadForm(forms.ModelForm):  
    class Meta:  
        model = UploadForm  
        fields = "__all__"
 
    def __init__(self, *args, **kwargs):
            super(UploadForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'   