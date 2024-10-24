from .models import Comment, Category
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CategoryForm(forms.ModelForm):
    """Form for the Category model."""
    class Meta:
        model = Category
        fields = ['name', 'is_active']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'title': 'max_length=50',
                    'placeholder': 'Category Name',
                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            )
        }

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    review = forms.CharField(widget=forms.Textarea, label='Your Review')