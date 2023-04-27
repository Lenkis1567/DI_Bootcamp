from django import forms
from .models import Gif, Category

class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields = ('title', 'url', 'uploader_name')
        exclude = ('likes')
        widgets = {
            'title': forms.Textarea(attrs={'class': 'title-class', 'id': '1'})
        }
        
    catagories=forms.ModelMultipleChoiceField(queryset=Category.objects.all())

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

class LikeForm(forms.Form):
    gif = forms.ModelChoiceField(queryset=Gif.objects.all())
    like = forms.BooleanField()
    like = forms.BooleanField()