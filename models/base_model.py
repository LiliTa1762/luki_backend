class Basejson:
    """ Class to have data in json without a specific parameter """
    def to_dict(self):
        """ Method to convert into dictionary """
        dictionary: dict = self.__dict__
        dictionary.pop('_sa_instance_state')
        return dictionary
