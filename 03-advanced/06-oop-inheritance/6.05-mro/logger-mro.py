class LoggerFactory:
    def configure(self, *args, **kwargs):
        print(f'{self.__class__.__name__}:configure')

class SpecificLogger(LoggerFactory):
    def configure(self, *args, **kwargs):
        super().configure(*args, **kwargs)
        print(f'{self.__class__.__name__}:configure extended')

class BaseClassWithLoggingCapabilities(LoggerFactory):
    def __init__(self):
        super().configure()

class SpecificClass(BaseClassWithLoggingCapabilities, SpecificLogger):
    pass

if __name__ == '__main__':
    v = SpecificClass()

