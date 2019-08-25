from django.forms import ModelForm
from . models import approvals

class MyForm(ModelForm):
	class Meta:
		model=approvals
		fields = '__all__'
		#exclude = 'firstname'