import json
import sys
import math


def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def get_biggest_bar(data):
    max_seats_count = 0
    biggest_bars = []
    for bar in data['features']:
        seats_count = bar['properties']['Attributes']['SeatsCount']
        if max_seats_count > seats_count:
            continue
        if max_seats_count < seats_count:
            max_seats_count = seats_count
            biggest_bars = []
        biggest_bars.append(bar)
    return biggest_bars


def get_smallest_bar(data):
    min_seats_count = sys.maxint
    smallest_bars = []
    for bar in data['features']:
        seats_count = bar['properties']['Attributes']['SeatsCount']
        # if seats_count == 0:    # incorrect seats value
        #    continue
        if min_seats_count < seats_count:
            continue
        if min_seats_count > seats_count:
            min_seats_count = seats_count
            smallest_bars = []
        smallest_bars.append(bar)
    return smallest_bars


def get_closest_bar(data, longitude, latitude):
    min_distance = float(sys.maxint)
    closest_bar = {}
    for bar in data['features']:
        longitude_delta = bar['geometry']['coordinates'][0] - longitude
        latitude_delta = bar['geometry']['coordinates'][1] - latitude
        distance = math.hypot(longitude_delta, latitude_delta)
        if min_distance > distance:
            min_distance = distance
            closest_bar = bar
    return closest_bar


def get_bar_name(data):
    return data['properties']['Attributes']['Name']


if __name__ == '__main__':
    moscow_bars = load_data('bars.json')

    print('Biggest bars:')
    for bar in get_biggest_bar(moscow_bars):
        print(get_bar_name(bar))

    print('Smallest bars:')
    for bar in get_smallest_bar(moscow_bars):
        print(get_bar_name(bar))

    user_longitude = input('Input your longitude: ')
    user_latitude = input('Input your latitude: ')
    closest_bar = get_closest_bar(moscow_bars, user_longitude, user_latitude)
    print('Closest bar: ' + get_bar_name(closest_bar))
