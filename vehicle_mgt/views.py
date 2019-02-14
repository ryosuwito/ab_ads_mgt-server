from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token
from area_db.models import Province, City, MainRoute
from driver_mgt.models import Driver

from .forms import AddCarForm
from .models import VehicleBrand, VehicleModel, VehicleColor, VehicleType, Vehicle

class AddCarView(View):
	form = AddCarForm()
	form_messages = ''
	def get(self, request, *args, **kwargs):
		drivers = Driver.objects.filter(is_active=True)
		colors = VehicleColor.objects.filter(is_active=True).order_by('name')
		main_routes = MainRoute.objects.filter(is_active=True).order_by('name')
		provinces = Province.objects.all().order_by('name')
		return render(request, 'backend/registration/add_vehicle.html',
		{'form': self.form,
		'colors': colors,
		'drivers': drivers,
		'main_routes': main_routes,
		'provinces': provinces,
		'token': get_token(request),
		'form_messages': self.form_messages})

	def post(self, request, *args, **kwargs):
		self.form = AddCarForm(request.POST, request.FILES)
		if self.form.is_valid():
			data = self.form.cleaned_data
			driver_pk = request.POST.get('driver')
			vehicle_type_name = request.POST.get('vehicle_type')
			try:
				driver = Driver.objects.get(pk=driver_pk)
				vehicle_province = Province.objects.get(pk=request.POST.get('provinsi'))
				vehicle_city = City.objects.get(pk=request.POST.get('kota'))
				vehicle_type = VehicleType.objects.get(name=vehicle_type_name.title())
			except Exception as e:
				print(e)
				return HttpResponse(driver_pk)

			if driver:
				try:
					vehicles = Vehicle.objects.filter(driver=driver)
				except Exception as e:
					print(e)

				if vehicles:
					for vehicle in vehicles:
						vehicle.is_active=False
						vehicle.save()


			vehicle = Vehicle.objects.create(
					driver=driver,
					vehicle_model=data.get('vehicle_model'),
					vehicle_type=vehicle_type,
					vehicle_year=data.get('vehicle_year'),
					vehicle_brand=data.get('vehicle_brand'),
					vehicle_color=data.get('vehicle_color'),
					vehicle_city=vehicle_city,
					vehicle_province=vehicle_province,
					vehicle_used_for=data.get('vehicle_used_for'),
					daily_main_route=request.POST.get('daily_main_route'),
					stnk_photo=data.get('stnk_photo'),
					front_side_photo=data.get('front_side_photo'),
					license_no=request.POST.get('license_no').upper(),

				)
			if vehicle:
				return HttpResponse(vehicle)

			return JsonResponse(request.POST)
		return JsonResponse(request.POST)

class GetBrandsView(View):
    def get(self, request, vehicle_type, **kwargs):
        vehicle_brands = VehicleBrand.objects.filter(
        					is_active=True,
        					vehicle_type__name=vehicle_type.title()
        				)
        return JsonResponse([brand.name for brand in vehicle_brands], safe=False)

class GetModelsView(View):
    def get(self, request, vehicle_type, vehicle_brand, **kwargs):
        vehicle_models = VehicleModel.objects.filter(
        					is_active=True,
        					vehicle_brand__name=vehicle_brand.lower(),
        					vehicle_brand__vehicle_type__name=vehicle_type.title()
        				)
        return JsonResponse([model.name for model in vehicle_models], safe=False)