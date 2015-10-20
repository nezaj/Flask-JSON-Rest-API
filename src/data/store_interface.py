"""
Interface for Store implmentations
"""
class StoreInterface:

    def create_unit(self, params):
        """ Create a new unit configuration """
        raise NotImplementedError()

    def delete_unit(self, unit_id):
        """ Deletes unit config by unit_id """
        raise NotImplementedError()

    def get_all_units(self):
        """ Get all unit configurations in the store """
        raise NotImplementedError()

    def get_unit(self, unit_id):
        """ Gets a unit configuration by a unit_id """
        raise NotImplementedError()

    def update_unit(self, unit_id, params):
        """ Updates a unit configuration with the passed in params """
        raise NotImplementedError()
