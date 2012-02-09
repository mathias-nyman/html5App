class ExampleObject:
    def __init__(self, name, pic):
        assert isinstance(name, str)
        assert isinstance(pic, str)
        
        self.name = name 
        self.pic = pic

