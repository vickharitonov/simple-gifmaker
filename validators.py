class ExtensionValidator:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, name):
        start = name.rfind(".")  # index after which we getting file extension
        ext = (
            "" if start == -1 else name[start + 1 :].lower()
        )  # getting extension string after last '.'
        return (
            ext in self.extensions
        )  # returns True if fileextension in extensions list
