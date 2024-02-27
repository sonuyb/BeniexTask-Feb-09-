class TextFileHandler:
    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode
        self.file = None
 
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except Exception as e:
            print(f"Error: {e}")
            raise
 
        return self
 
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
 
        if exc_type is not None or 'bug' in self.file.read():
            try:
                import os
                os.remove(self.filename)
                print(f"File '{self.filename}' deleted.")
            except Exception as e:
                print(f"Error deleting file: {e}")
 
if __name__ == "__main__":
    try:
        with TextFileHandler('example.txt') as handler:
            handler.file.write("This is a sample text without bug.")
            # Uncomment the line below to test deleting the file on exception or 'bug' keyword
            # raise Exception("Test Exception")
    except Exception as e:
        print(f"An exception occurred: {e}")