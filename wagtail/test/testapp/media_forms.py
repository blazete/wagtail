from django import forms

from wagtail.admin.widgets import AdminDateTimeInput
from wagtail.contrib.images.forms import BaseImageForm
from wagtail.documents.forms import BaseDocumentForm


class OverriddenWidget(forms.Widget):
    pass


class AlternateImageForm(BaseImageForm):
    form_only_field = forms.DateTimeField()

    class Meta:
        widgets = {
            **BaseImageForm.Meta.widgets,
            "tags": OverriddenWidget,
            "file": OverriddenWidget,
            "form_only_field": AdminDateTimeInput
        }


class AlternateDocumentForm(BaseDocumentForm):
    form_only_field = forms.DateTimeField()

    class Meta:
        widgets = {
            "tags": OverriddenWidget,
            "file": OverriddenWidget,
            "form_only_field": AdminDateTimeInput
        }