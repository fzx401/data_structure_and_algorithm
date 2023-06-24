class Test:
    def __init__(self) -> None:
        pass
    @classmethod
    def create_instance(cls, value):
        if cls!= Test:
            raise TypeError('error')
        return cls()
t = Test()
t.create_instance(2)