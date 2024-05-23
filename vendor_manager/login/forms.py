from django import forms

class UserForm(forms.Form):
	name = forms.ChoiceField(
			help_text="Select the User",
			required=True,
			label="Select User ",
			widget=forms.RadioSelect(attrs={'class': 'form-control'}),
			choices=((1, 'Admin'), (2, 'Officer')),
			initial=1,
			)
	password = forms.CharField(label="Password", required=True, 
		widget=forms.PasswordInput(attrs={'class': 'form-control'}))
