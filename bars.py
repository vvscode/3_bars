import requests

default_bars_url = 'https://devman.org/fshare/1503831681/4/'

def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']

def get_bar_seatscount(bar):
    return  bar['properties']['Attributes']['SeatsCount']

def get_bar_coordinates(bar):
    return  bar['geometry']['coordinates']

def get_default_latlng():
    r = requests.get('https://api.userinfo.io/userinfos')
    user_data = r.json()
    position = user_data['position']
    return [position['latitude'], position['longitude']]

def get_distance(coordinates1, coordinates2):
    [lat1, lng1] = coordinates1
    [lat2, lng2] = coordinates2
    lat_distance = abs(lat1 - lat2)
    lng_distance = abs(lng1 - lng2)
    return (lat_distance**2 + lng_distance**2)**0.5

def load_data(filepath):
    r = requests.get(filepath)
    return r.json()['features'];

def coordinates_to_str(coordinates):
    return ','.join(map(str, coordinates))


def get_biggest_bar(data):
    data.sort(key=get_bar_seatscount, reverse=True)
    return data[0]


def get_smallest_bar(data):
    data.sort(key=get_bar_seatscount)
    return data[0]


def get_closest_bar(data, longitude, latitude):
    data.sort(key=lambda x: get_distance(get_bar_coordinates(x), [latitude, longitude]))
    return data[0]

def main():
    file_url = input('Which url should we use to load data? (or just enter to use {}) - '.format(default_bars_url)) or  default_bars_url

    default_latlng_str =coordinates_to_str(get_default_latlng())
    latlng_str = input('Please enter your coordinates in format `lat, lng` (like `{}`) or just press enter - '.format(default_latlng_str)) or default_latlng_str

    [s_lat, s_lng] = latlng_str.split(',')
    lat = float(s_lat.strip())
    lng = float(s_lng.strip())

    bars_data = load_data(file_url)

    biggest_bar = get_biggest_bar(bars_data)
    smallest_bar = get_smallest_bar(bars_data)
    closest_bar = get_closest_bar(bars_data, lat, lng)

    print('Biggest bar is `{}` with {} seats'.format(get_bar_name(biggest_bar), get_bar_seatscount(biggest_bar)))
    print('Smallest bar is `{}` with {} seats'.format(get_bar_name(smallest_bar), get_bar_seatscount(smallest_bar)))

    closest_bar_coordinates = coordinates_to_str(get_bar_coordinates(closest_bar))
    print('Closest bar is `{}` with  coordinates {}'.format(get_bar_name(closest_bar), closest_bar_coordinates))



if __name__ == '__main__':
    main()
