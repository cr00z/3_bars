import json
import math
import io


def load_data(filepath):
    try:
        with io.open(filepath, encoding='utf-8') as json_file_object:
            return json.load(json_file_object)
    except FileNotFoundError:
        exit('Input file not found')
    except json.decoder.JSONDecodeError:
        exit('It\'s not a JSON')


def get_bar_seats_count(bar):
    return bar['properties']['Attributes']['SeatsCount']


def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


def get_biggest_bar(bars_list):
    return max(bars_list, key=get_bar_seats_count)


def get_smallest_bar(bars_list):
    return min(bars_list, key=get_bar_seats_count)


def get_distance(bar):
    bar_coord = bar['geometry']['coordinates']
    longitude_delta = bar_coord[0] - user_longitude
    latitude_delta = bar_coord[1] - user_latitude
    return math.hypot(longitude_delta, latitude_delta)


def get_closest_bar(bars_list):
    return min(bars_list, key=get_distance)


if __name__ == '__main__':
    moscow_bars = load_data('bars.json')['features']
    print('Biggest bar: {}'.format(get_bar_name(get_biggest_bar(moscow_bars))))
    print('Smallest bar: {}'.format(get_bar_name(get_smallest_bar(moscow_bars))))
    try:
        # SIC!!! in Russia we use latitude first
        user_latitude = float(input('Input your latitude: '))
        user_longitude = float(input('Input your longitude: '))
    except ValueError:
        exit('Coordinates must be digital')
    closest_bar = get_closest_bar(moscow_bars)
    print('Closest bar: {}'.format(get_bar_name(closest_bar)))
