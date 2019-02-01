import requests
import json
from datetime import datetime, timedelta

base_url="http://api.gps.id/"
class GPSHandler():
    address = ''
    apikey = ''
    birthday = ''
    coname = ''
    createdate = ''
    domain = ''
    email = ''
    fullname = ''
    id = ''
    password = 'superspring'
    phone = ''
    privilege = ''
    remark = ''
    sessionKey = ''
    username = 'super'
    
    profile = {}
    vehicles = {}

    def get_data(self,url, data):
        #print(url)
        response = requests.post(url, data=data).text
        #print(response)
        data = json.loads(response)['data']
        print(json.dumps(data, indent=4, sort_keys=True))
        return data

    def login(self):
        path = 'login'
        url = base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'password': self.password,
            }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                self.sessionKey = data['sessionKey']
                self.apikey = data['apikey']
                return {'response':'OK'}
        except Exception as e:
            print(e)
        return {'response':'NO'}

    def get_profile_user(self):
        path = 'profile'
        url = base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'sessionkey': self.sessionKey,
            'apikey': self.apikey
        }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                self.profile = data['profile']
                self.id = self.profile['id']
                self.apikey = self.profile['apikey']
                self.privilege = self.profile['privilege']
                self.fullname = self.profile['fullname']
                self.conama = self.profile['coname']
                self.phone = self.profile['phone']
                self.email = self.profile['email']
                self.address = self.profile['address']
                self.remark = self.profile['remark']
                self.createdate = self.profile['createdate']
                self.birthday = self.profile['birthday']
                return {'response':'OK'}
        except Exception as e:
            print(e)
        return {'response':'NO'}

    def get_all_vehicle(self):
        path = 'getvehicle'
        url = base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'sessionkey': self.sessionKey,
            'apikey': self.apikey
        }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                self.vehicles = data['vehicle']
                return {'response':'OK'}
        except Exception as e:
            print(e)
        return {'response':'NO'}

    def get_locate_vehicle(self, terminal):
        path = 'locatevehicle'
        url = base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'sessionkey': self.sessionKey,
            'apikey': self.apikey,
            'terminal': terminal
        }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                vehicle = data['vehicle']
                return {'response':'OK', 'vehicle': vehicle}
        except Exception as e:
            print(e)
        return {'response':'NO'}

    def get_history_vehicle(self, terminal, date_start, date_end):
        path = 'track'
        url = base_url + path
        data= {
            'domain': self.domain,
            'username': self.username,
            'sessionkey': self.sessionKey,
            'apikey': self.apikey,
            'terminal': terminal,
            'gpsstart': date_start,
            'gpsend': date_end
        }
        data = self.get_data(url, data)
        try:
            if data['response'] == 'OK':
                track = data['track']
                return {'response':'OK', 'track': track}
        except Exception as e:
            print(e)
        return {'response':'NO'}

gps_handler = GPSHandler()
res = gps_handler.login()
if res['response'] == 'OK':
    print("Login as {} Success".format(gps_handler.username))
    print("Session Key : {}".format(gps_handler.sessionKey))
    print("Api Key : {}".format(gps_handler.apikey))
else:
    print("Login Failed")
    exit()
res = gps_handler.get_profile_user()
if res['response'] == 'OK':
    print("Get Profile of {} Success".format(gps_handler.username))
else:
    print("Get Profile User Failed")
    exit()
res = gps_handler.get_all_vehicle()
if res['response'] == 'OK':
    print("Get all vehicles of {} Success".format(gps_handler.username))
else:
    print("Get Profile User Failed")
    exit()

now = datetime.now()
date_start = now - timedelta(hours = 1)
date_start = date_start.strftime('%Y-%m-%d %H:%M:%S')
date_end = now.strftime('%Y-%m-%d %H:%M:%S')

for vehicle in gps_handler.vehicles:
    print('Get location of {}'.format(vehicle['license']))
    print(gps_handler.get_locate_vehicle(vehicle['terminal']))

    print('Get history of {}'.format(vehicle['license']))
    print(gps_handler.get_history_vehicle(vehicle['terminal'], date_start, date_end))

