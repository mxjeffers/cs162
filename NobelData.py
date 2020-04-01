# Name: Malcolm Jeffers
# Date: 01/30/2020
# Description: This program searches a JSON file for Nobel Prize winners in a category and year.


import json


class NobelData:
    """Creates a class of Nobel data. Loads the nobels.json file. Has a method to search for
        a year and category"""

    def __init__(self):
        """Loads the nobels.json file as self._nobel"""
        with open('nobels.json', 'r') as infile:
            self._nobel = json.load(infile)

    def search_nobel(self, year, category):
        """ Searches the JSON file for a year and category. It then returns the list of winners surnames
            in alphabetical order."""
        win_list = []
        year_list = []

        # Gets a list of years that match the requested year.
        for i in range(len(self._nobel['prizes'])):
            if self._nobel['prizes'][i]['year'] == year:
                year_list.append(i)

        # Searches through the list of years to find a corresponding category.
        # If the category is found, it iterates through 'laureates to add their surnames
        # to a list.

        for x in year_list:
            if self._nobel['prizes'][x]['category'] == category:
                for y in range(len(self._nobel['prizes'][x]['laureates'])):
                    win_list.append(self._nobel['prizes'][x]['laureates'][y]['surname'])
        win_list.sort()
        return win_list

