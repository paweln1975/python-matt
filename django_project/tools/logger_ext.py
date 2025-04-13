class LoggerFactory:
    def configure(self, **kwargs):
        print(f'LoggerFactory:configure')

class SpecificLogger(LoggerFactory):
    def configure(self, **kwargs):
        print(f'SpecificLogger:configure extended')
        super().configure(**kwargs)

class BasicLogger(LoggerFactory):
    def __init__(self):
        print(f'BasicLogger:__init__')
        super().configure()

class DjangoLogger(BasicLogger, SpecificLogger):
    def __init__(self):
        print(f'DjangoLogger:__init__')

    def __init__(self, **kwargs):
        print(f'DjangoLogger:__init__with_kwargs')

    def log_something(self, msg: str):
        print(f'{msg}:log_something')

class ModuleClass:
    pass

class SpecifiModuleClass(ModuleClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MySpecificModuleClass(SpecifiModuleClass, DjangoLogger):
    pass


if __name__ == '__main__':
    v = MySpecificModuleClass(a='test')

