from django.forms import ModelForm
from .models import Play
from django.urls import reverse


class PlayForm(ModelForm):
    class Meta:
        model = Play
        fields = ["date", "winner"]

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
