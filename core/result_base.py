
class ResultBase():
    def __str__(self):
        return str(self.__dict__.items())