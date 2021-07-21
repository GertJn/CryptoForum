from django.forms import ModelForm
from .models import *


class CreateInForum(ModelForm):
    class Meta:
        model = Forum
        fields = "__all__"


class CreateInComments(ModelForm):
    class Meta:
        model = Comments
        fields = "__all__"
