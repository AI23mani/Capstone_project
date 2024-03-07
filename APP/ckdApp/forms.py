from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=['radius_mean','concavity_mean','radius_worst','compactness_worst','concavity_worst']
