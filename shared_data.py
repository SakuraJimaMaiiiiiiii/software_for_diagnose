# shared_data.py
class SharedData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SharedData, cls).__new__(cls)
            cls._instance.file_path = ""
        return cls._instance

    def set_file_path(self, path):
        self.file_path = path

    def get_file_path(self):
        return self.file_path
