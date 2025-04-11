from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post 
        fields = ("group",'text')
        labels = {
          "group": "группа",
          "text": "Текст записи"
        }
        help_texts = {
          'group':'При желании выберите группу',
          'text':'Здесь напишите текст записи'
        }