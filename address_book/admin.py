from django.contrib import admin
from address_book.models import Entry


class EntryAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','street_address','email','phone_number')
	#list_filter = ('first_name','last_name','email')
	search_fields = ('first_name','last_name','phone_number')
	#fields = ('first_name','last_name','street_address','email','phone_number')

admin.site.register(Entry,EntryAdmin)