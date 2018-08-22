class Vehicle:
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        # The double underscore here tells python that the variable should be private. 
        self.__warnings = []

    def __repr__(self):
        print('Printing...')
        return 'Top speed: {}, __warnings: {}'.format(self.top_speed, self.__warnings)

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)

    def get_warnings(self):
        return self.__warnings

    def drive(self):
        print('I am driving, but not faster than {}'.format(self.top_speed))