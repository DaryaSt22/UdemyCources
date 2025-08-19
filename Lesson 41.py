class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


custom_list = ExtendedList([3, 5, 2, 9425])
custom_list.print_list_info()

custom_list.append(456)
custom_list.print_list_info()
print(custom_list.__dict__)
print(ExtendedList.__dict__)
print(object.__dict__)
print(list.__subclasses__())
print(object.__subclasses__())
