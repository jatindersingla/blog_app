from django import forms
from .models import Comments
class Commentsform(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('name','email','body')
    def __init__(self,*args,**kwargs):
        super(Commentsform,self).__init__(*args,**kwargs)
        self.fields["name"].widget.attrs={'placeholder':'Enter Name','class':'form-control'}
        self.fields["email"].widget.attrs = {'placeholder': 'Enter Email', 'class': 'form-control'}
        self.fields["body"].widget.attrs = {'placeholder': 'Body', 'class': 'form-control','rows':'5'}



