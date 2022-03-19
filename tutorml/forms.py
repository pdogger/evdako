from django import forms

from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["email", "notify_tutorials", "notify_datasets"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "input sub_input", "required": True}),
            "notify_tutorials": forms.CheckboxInput(attrs={"class": "switch"}),
            "notify_datasets": forms.CheckboxInput(attrs={"class": "switch"})
        }

