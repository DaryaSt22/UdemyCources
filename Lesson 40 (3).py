class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def __str__(self):
        return self.title

my_image = Image(100, "Car", 25)

print(my_image.resolution)
print(my_image.title)
print(my_image.extension)

my_image.resize('5555')
print(my_image.resolution)
print(my_image.title)
