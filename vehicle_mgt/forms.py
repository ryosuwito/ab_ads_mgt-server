from django import forms
from .models import Vehicle, VehicleBrand, VehicleColor, VehicleModel, VehicleYear

class AddCarForm(forms.Form):
	YEAR_OPTIONS = VehicleYear.objects.all()
	vehicle_brand = forms.CharField()
	vehicle_color = forms.CharField()
	vehicle_model = forms.CharField()
	vehicle_year = forms.ModelChoiceField(YEAR_OPTIONS, initial='Choose Option')
	vehicle_used_for = forms.CharField(required=False)
	stnk_photo = forms.ImageField(required=False)#allow_empty_file=False)
	front_side_photo = forms.ImageField(required=False)#allow_empty_file=False)
    
	def __init__(self, *args, **kwargs):
		super(AddCarForm, self).__init__(*args, **kwargs)
		self.fields['vehicle_year'].widget.attrs['class'] = 'form-control'
		self.fields['vehicle_year'].widget.attrs['style'] = 'width:100%'
		self.fields['vehicle_year'].widget.attrs['required'] = 'required'
		self.fields['vehicle_brand'].widget.attrs['class'] = 'form-control'
		self.fields['vehicle_brand'].widget.attrs['style'] = 'width:100%'
		self.fields['vehicle_brand'].widget.attrs['required'] = 'required'
		self.fields['vehicle_color'].widget.attrs['class'] = 'form-control'
		self.fields['vehicle_color'].widget.attrs['style'] = 'width:100%'
		self.fields['vehicle_color'].widget.attrs['required'] = 'required'
		self.fields['vehicle_model'].widget.attrs['class'] = 'form-control'
		self.fields['vehicle_model'].widget.attrs['style'] = 'width:100%'
		self.fields['vehicle_model'].widget.attrs['required'] = 'required'
		self.fields['vehicle_used_for'].widget.attrs['class'] = 'form-control'
		self.fields['vehicle_used_for'].widget.attrs['style'] = 'width:100%'
		self.fields['stnk_photo'].widget.attrs['class'] = 'form-control'
		self.fields['stnk_photo'].widget.attrs['style'] = 'width:100%'
		#self.fields['stnk_photo'].widget.attrs['required'] = 'required'
		self.fields['stnk_photo'].widget.attrs['onchange'] = 'previewImage(this.id);'
		self.fields['front_side_photo'].widget.attrs['class'] = 'form-control'
		self.fields['front_side_photo'].widget.attrs['style'] = 'width:100%'
		#self.fields['front_side_photo'].widget.attrs['required'] = 'required'
		self.fields['front_side_photo'].widget.attrs['onchange'] = 'previewImage2(this.id);'