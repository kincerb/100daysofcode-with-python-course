#!/usr/bin/env python
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    return (', ').join(cars.get('Jeep'))


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [cars.get(manufacturer)[0] for manufacturer in cars.keys()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matches = []
    for models in cars.values():
        for model in models:
            if grep.lower() in model.lower():
                matches.append(model)
    matches.sort()
    return matches


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    for manufacturer, models in cars.items():
        models.sort()
        cars[manufacturer] = models
    return cars
