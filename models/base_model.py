class Basejson:
    def to_dict(self):
        dictionary: dict = self.__dict__
        dictionary.pop('_sa_instance_state')
        return dictionary
