class ExampleObject:
    def __init__(self, name, value):
        assert isinstance(name, str)
        assert isinstance(value, str)
        
        self.name = name 
        self.value = value

