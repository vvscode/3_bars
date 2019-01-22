import requests
import json
import sys


def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


def get_bar_seatscount(bar):
    return bar['properties']['Attributes']['SeatsCount']


def get_bar_coordinates(bar):
    return bar['geometry']['coordinates']


def get_default_latlng():
    moscow_coordinates = [55.7558, 37.6173]
    try:
        response = requests.get('https://api.userinfo.io/userinfos')
        user_data = response.json()
        position = user_data['position']
        if position['latitude'] is None or position['longitude'] is None:
            raise ValueError("Error on detecting positon")
        return [position['latitude'], position['longitude']]
    except requests.exceptions.RequestException as e:
        return moscow_coordinates
    except ValueError:
        return moscow_coordinates


def get_distance(coordinates1, coordinates2):
    [lat1, lng1] = coordinates1
    [lat2, lng2] = coordinates2
    lat_distance = abs(lat1 - lat2)
    lng_distance = abs(lng1 - lng2)
    return (lat_distance ** 2 + lng_distance ** 2) ** 0.5


def load_data(filepath):
    with open(filepath) as filepointer:
        return json.load(filepointer)['features']


def coordinates_to_str(coordinates):
    return ','.join(map(str, coordinates))


def get_biggest_bar(bars_data):
    return max(bars_data, key=get_bar_seatscount)


def get_smallest_bar(bars_data):
    return min(bars_data, key=get_bar_seatscount)


def get_closest_bar(bars_data, longitude, latitude):
    return min(
        bars_data,
        key=lambda x: get_distance(
            get_bar_coordinates(x), [latitude, longitude])
    )


def print_bar(bar):
    return "`{}` (seat(s) - {}, coordinates - {})".format(
        get_bar_name(bar),
        get_bar_seatscount(bar),
        coordinates_to_str(get_bar_coordinates(bar))
    )


def request_user_coordinates():
    default_latlng_str = coordinates_to_str(get_default_latlng())
    latlng_str = input('''
    Your coordinates in format `lat, lng` or just press enter
    We detected your  coordinates as `{}` - '''.strip().format(
        default_latlng_str)) or default_latlng_str

    try:
        return map(lambda x: float(x.strip()), latlng_str.split(','))
    except ValueError:
        sys.exit("Please enter coordinates in correct format")


def load_bars_data(filename):
    try:
        return load_data(filename)
    except FileNotFoundError:
        sys.exit("Please pass correct file name")
    except json.decoder.JSONDecodeError:
        sys.exit("Provided file does not contains correct json data")


def main():
    if (len(sys.argv) < 2):
        return sys.exit("Please pass filename as param")

    filename = sys.argv[1]

    bars_data = load_bars_data(filename)
    [lat, lng] = request_user_coordinates()

    biggest_bar = get_biggest_bar(bars_data)
    smallest_bar = get_smallest_bar(bars_data)
    closest_bar = get_closest_bar(bars_data, lat, lng)

    print('Biggest bar is `{}`'.format(print_bar(biggest_bar)))
    print('Smallest bar is `{}`'.format(print_bar(smallest_bar)))
    print('Closest bar is `{}`'.format(print_bar(closest_bar)))


if __name__ == '__main__':
    main()
