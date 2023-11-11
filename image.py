class Image:
    def __init__(self, name, file):
        self.name = name
        self.file = file

    def __repr__(self):
        return f"Image(name={self.name}, file={self.file})"
    
    def save_image(image):
    with open(image.file, "wb") as f:
        f.write(image.data)

    db.save_image(image)

