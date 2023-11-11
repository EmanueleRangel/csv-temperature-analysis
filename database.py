import sqlalchemy

engine = sqlalchemy.create_engine("mysql://user:password@localhost/database")

class Image(sqlalchemy.Model):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(255))
    file = sqlalchemy.Column(sqlalchemy.LargeBinary)

image = Image(name="image1", file=open("image.png", "rb").read())
image.save()

