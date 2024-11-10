
def if_alive(method):
    def wrapper(self, *args, **kwargs):
        if self.current_health <= 0:
            raise RuntimeError('Hero is dead and cannot make damage')
        return method(self, *args, **kwargs)

    return wrapper
