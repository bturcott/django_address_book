from django import forms
from address_book.models import Entry

class EntryForm(forms.ModelForm):
	first_name = forms.CharField(max_length = 25)
	last_name = forms.CharField(max_length = 25)
	street_address = forms.CharField(max_length = 150)
	email = forms.EmailField(max_length = 254)
	phone_number = forms.CharField(max_length = 14)

	class Meta:
		model = Entry
		fields = ('first_name','last_name',
			'street_address', 'email', 'phone_number')




