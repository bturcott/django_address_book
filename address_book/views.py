from django.shortcuts import render
from address_book.models import Entry
from address_book.forms import EntryForm

def index(request):
	first_name_list = Entry.objects.order_by('first_name')
	last_name_list = Entry.objects.order_by('last_name')
	street_list = Entry.objects.order_by('street_address')
	email_list = Entry.objects.order_by('email')
	phone_number_list = Entry.objects.order_by('phone_number')
	context_dict = {'first_name': first_name_list, 
		'last_name': last_name_list, 'street_address' : street_list, 'email': email_list, 'phone_number' : phone_number_list}
	return render(request, 'address_book/index.html', context_dict)


def add_entry(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = EntryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = EntryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'address_book/add_entry.html', {'form': form})