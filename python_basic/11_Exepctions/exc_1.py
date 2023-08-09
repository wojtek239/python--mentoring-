class InvalidDataError(Exception):
    pass


class FileHandler:
    def __init__(self, file_path, no_connectors, max_file_size):
        self.set_file_path(file_path)
        self.set_no_connectors(no_connectors)
        self.set_max_file_size(max_file_size)

    def set_file_path(self, file_path):
        if not file_path:
            raise InvalidDataError("'file_path' cannot be empty.")
        self.file_path = file_path

    def set_no_connectors(self, no_connectors):
        if not isinstance(no_connectors, int) or no_connectors <= 0\
                or no_connectors > 10:
            raise InvalidDataError("'no_connectors' must be from 1 to 10")
        self.no_connectors = no_connectors

    def set_max_file_size(self, max_file_size):
        if not isinstance(max_file_size, int) or max_file_size < 1000\
                or max_file_size > 9999:
            raise InvalidDataError("'max_file_size' must be 4-digit number")
        self.max_file_size = max_file_size

    def read_content(self):
        print("Reading file content.")

    def save_to_file(self):
        print("Saving to file.")

# example use
try:
    handler = FileHandler("", 5, 2000)
except InvalidDataError as e:
    print(f"Validation error: {e}")

try:
    handler = FileHandler("/path/to/file.txt", 12, 5000)
except InvalidDataError as e:
    print(f"Validation error: {e}")

try:
    handler = FileHandler("/path/to/file.txt", 8, 12345)
except InvalidDataError as e:
    print(f"Validation error: {e}")

# Proper use
try:
    handler = FileHandler("/path/to/file.txt", 5, 2000)
    handler.read_content()
    handler.save_to_file()
except InvalidDataError as e:
    print(f"Validation error: {e}")
