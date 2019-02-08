from django import forms
from .models import Vehicle, VehicleBrand, VehicleColor, VehicleModel, VehicleYear

class AddCarForm(forms.Form):
	BRAND_OPTIONS = VehicleBrand.objects.filter(is_active=True)
	COLOR_OPTIONS = VehicleColor.objects.filter(is_active=True)
	MODEL_OPTIONS = VehicleModel.objects.filter(is_active=True)
	YEAR_OPTIONS = VehicleYear.objects.filter(is_active=True)
	vehicle_brand = forms.ModelChoiceField(BRAND_OPTIONS, initial='Choose Option')
	vehicle_color = forms.ModelChoiceField(COLOR_OPTIONS, initial='Choose Option')
	vehicle_model = forms.ModelChoiceField(MODEL_OPTIONS, initial='Choose Option')
	vehicle_year = forms.ModelChoiceField(YEAR_OPTIONS, initial='Choose Option')
	vehicle_used_for = forms.CharField()
	stnk_photo = forms.ImageField(allow_empty_file=False)
	front_side_photo = forms.ImageField(allow_empty_file=False)
    
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
		self.fields['vehicle_used_for'].widget.attrs['required'] = 'required'
		self.fields['stnk_photo'].widget.attrs['class'] = 'form-control'
		self.fields['stnk_photo'].widget.attrs['style'] = 'width:100%'
		self.fields['stnk_photo'].widget.attrs['required'] = 'required'
		self.fields['stnk_photo'].widget.attrs['onchange'] = 'previewImage(this.id);'
		self.fields['front_side_photo'].widget.attrs['class'] = 'form-control'
		self.fields['front_side_photo'].widget.attrs['style'] = 'width:100%'
		self.fields['front_side_photo'].widget.attrs['required'] = 'required'
		self.fields['front_side_photo'].widget.attrs['onchange'] = 'previewImage2(this.id);'