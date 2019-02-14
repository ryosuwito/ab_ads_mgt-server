from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Province, City, Kecamatan, Kelurahan

def get_provinsi(request):
    if request.method == "GET":
        provinsi_list = Province.objects.all()
        if provinsi_list:
            results = []
            for provinsi in provinsi_list :
                a = {}
                a['nama'] = provinsi.name
                a['value'] = provinsi.pk
                results.append(a)
            return JsonResponse({'results':list(results)})
        else:
            response = HttpResponse("NOT FOUND", status=404)
            return response

def get_kota(request, nama_provinsi):
    if request.method == "GET":
        provinsi = Province.objects.get(name=nama_provinsi)
        if provinsi:
            kota_list = City.objects.filter(provinsi=provinsi)
            results = []
            i = 0;
            for kota in kota_list :
                i += 1
                a = {}
                a['nama'] = kota.name
                a['value'] = kota.pk
                results.append(a)
            return JsonResponse({'results':list(results)})
        else:
            response = HttpResponse("NOT FOUND", status=404)
            return response


def get_kecamatan(request, pk):
    if request.method == "GET":
        kota = City.objects.get(id=pk)
        if kota:
            kecamatan_list = Kecamatan.objects.filter(kota=kota)
            results = []
            i = 0;
            for kecamatan in kecamatan_list :
                i += 1
                a = {}
                a['nama'] = kecamatan.name
                a['value'] = kecamatan.pk
                results.append(a)
            return JsonResponse({'results':list(results)})
        else:
            response = HttpResponse("NOT FOUND", status=404)
            return response

def get_kelurahan(request, pk):
    if request.method == "GET":
        kecamatan = Kecamatan.objects.get(id=pk)
        if kecamatan:
            kelurahan_list = Kelurahan.objects.filter(kecamatan=kecamatan)
            results = []
            i = 0;
            for kelurahan in kelurahan_list :
                i += 1
                a = {}
                a['nama'] = kelurahan.name
                a['value'] = kelurahan.pk
                results.append(a)
            return JsonResponse({'results':list(results)})
        else:
            response = HttpResponse("NOT FOUND", status=404)
            return response


def get_by_postal_code(request, postal_code):
    if request.method == "GET":
        kelurahan_list = Kelurahan.objects.filter(postal_code=postal_code)
        if kelurahan_list:
            results = []
            for kelurahan in kelurahan_list :
                a = {}
                a['nama'] = kelurahan.name.title()
                a['value'] = kelurahan.pk
                results.append(a)
            return JsonResponse({'results':list(results)})
        else:
            response = HttpResponse("NOT FOUND", status=404)
            return response

def get_by_code(request, kelurahan_code):
    if request.method == "GET":
        kelurahan = Kelurahan.objects.get(pk=kelurahan_code)
        if kelurahan:
            results = []
            a = {}
            a['kelurahan'] = kelurahan.name
            a['kelurahan_pk'] = kelurahan.pk
            a['kecamatan'] = kelurahan.kecamatan.name
            a['kecamatan_pk'] = kelurahan.kecamatan.pk
            a['city'] = kelurahan.kecamatan.kota.name
            a['city_pk'] = kelurahan.kecamatan.kota.pk
            a['province'] = kelurahan.kecamatan.kota.provinsi.name
            a['province_pk'] = kelurahan.kecamatan.kota.provinsi.pk
            results.append(a)
            return JsonResponse({'results':list(results)})
        else:
            response = HttpResponse("NOT FOUND", status=404)
            return response

def get_postal_code(request, kelurahan_code):
    if request.method == "GET":
        kelurahan = Kelurahan.objects.get(pk=kelurahan_code)
        if kelurahan:
            results = []
            a = {}
            a['postal_code'] = kelurahan.postal_code
            results.append(a)
            return JsonResponse({'results':list(results)})
        else:
            response = HttpResponse("NOT FOUND", status=404)
            return response