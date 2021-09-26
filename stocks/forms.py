from django import forms

class StocksForm(forms.Form):
	name = forms.CharField(label=False, max_length=120,
		widget=forms.TextInput(attrs={'placeholder': 'Enter a Stock Name',
									'class': 'form-control'}))