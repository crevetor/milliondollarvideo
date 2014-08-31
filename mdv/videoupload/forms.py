from django.forms import ModelForm
from .models import VideoFragment


class VideoUploadForm(ModelForm):

    class Meta:
        model = VideoFragment
        fields = ['vidfile', 'link', 'description']
