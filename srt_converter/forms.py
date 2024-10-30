from django import forms

class SRTUploadForm(forms.Form):
    srt_file = forms.FileField(label='Upload SRT file')

