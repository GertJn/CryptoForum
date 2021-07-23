from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateInForum(ModelForm):
    class Meta:
        model = Forum
        fields = "__all__"


class CreateInComments(ModelForm):
    class Meta:
        model = Comments
        fields = "__all__"

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
