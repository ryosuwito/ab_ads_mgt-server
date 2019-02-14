from area_db.models import Province, City, Kecamatan, Kelurahan


with open('database_indonesia.csv') as file:
    print('begin')
    province = False
    city = False
    kecamatan = False
    plimit = 34
    klimit = 10000
    kclimit = 1000
    kllimit = 10000
    allowed_province = ['Banten', 'DKI Jakarta', 'Jawa Barat', 'Jawa Timur',
        'Jawa Tengah']
    prov, kot, kec, kel = 0, 0, 0, 0
    for index, line in enumerate(file):
        data = line.split(';')
        data.pop(0)
        if data[0] in allowed_province:

            print('{:}'.format(index, data[0]))
            if not province:
                if prov > plimit:
                    break
                prov += 1
                kot, kec, kel = 0, 0, 0
                province, cp = Province.objects.get_or_create(name=data[0])
            elif not province.name == data[0]:
                if prov > plimit:
                    break
                prov += 1
                kot, kec, kel = 0, 0, 0
                province, cp = Province.objects.get_or_create(name=data[0])

            if not city and not kot > klimit:    
                kot += 1
                kec, kel = 0, 0
                city, ck = City.objects.get_or_create(name=('%s %s'%(data[1], data[2])), provinsi=province)
            elif not city.name == '%s %s'%(data[1], data[2]) and not kot > klimit :
                kot += 1
                kec, kel = 0, 0
                city, ck = City.objects.get_or_create(name=('%s %s'%(data[1], data[2])), provinsi=province)
            
            if not kecamatan and not kec > kclimit:
                kec += 1
                kel = 0
                kecamatan, ckc = Kecamatan.objects.get_or_create(name=data[3], kota=city)
            elif not kecamatan.name == data[3] and not kec > kclimit:
                kec += 1
                kel = 0
                kecamatan, ckc = Kecamatan.objects.get_or_create(name=data[3], kota=city)
                
            if not kel > kllimit:
                kel += 1
                kelurahan= Kelurahan.objects.get_or_create(name=data[4], kecamatan=kecamatan, postal_code = data[5].strip())
            '''
            print('%s %s'%(cp, province.name))
            print('%s %s'%(ck, city.name))
            print('%s %s'%(ckc, kecamatan.name))
            print('%s %s'%(ckl, kelurahan.name))
            print(kelurahan.postal_code)
        '''
print('done')
