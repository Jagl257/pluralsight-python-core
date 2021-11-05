class ShippingContainer:

    container_serial = 0

    @classmethod
    def create_from_dict(cls, dictionary):
        return cls(**dictionary) 
        


    @staticmethod
    def _generate_serial():
        result = ShippingContainer.container_serial
        ShippingContainer.container_serial += 1
        return result
    
    def __init__(self, code, contents):
        self.code = code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()
