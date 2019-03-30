import json
import math


def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def get_biggest_bar(data):
    seats_count = lambda x: x['properties']['Attributes']['SeatsCount']
    return max(data['features'], key=seats_count)


def get_smallest_bar(data):
    seats_count = lambda x: x['properties']['Attributes']['SeatsCount']
    return min(data['features'], key=seats_count)


def get_closest_bar(data, longitude, latitude):

    def get_distance(bar):
        longitude_delta = bar['geometry']['coordinates'][0] - longitude
        latitude_delta = bar['geometry']['coordinates'][1] - latitude
        return math.hypot(longitude_delta, latitude_delta)

    return min(data['features'], key=get_distance)


def get_bar_name(data):
    return data['properties']['Attributes']['Name']


if __name__ == '__main__':
    moscow_bars = load_data('bars.json')

    print('Biggest bar: ' + get_bar_name(get_biggest_bar(moscow_bars)))

    print('Smallest bar: ' + get_bar_name(get_smallest_bar(moscow_bars)))

    user_longitude = input('Input your longitude: ')
    user_latitude = input('Input your latitude: ')
    closest_bar = get_closest_bar(moscow_bars, user_longitude, user_latitude)
    print('Closest bar: ' + get_bar_name(closest_bar))
