import psycopg2
from datetime import datetime
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from classes import Photo, Album

class Model(object):
    def __init__(self):
        engine = create_engine('postgresql://postgres:postgrepass@localhost:5432/MyDB')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        print("фільтрація Photo.name == smthreallynew")
        start_time = datetime.now()
        answr = self.session.query(Photo).filter(Photo.name == "smthreallynew").all()
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        for it in answr:
            print(it.name)
        print("агрегатні функції, count")
        start_time = datetime.now()
        answr = self.session.query(Photo).filter(Photo.name == "smthreallynew").count()
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        print(answr)
        print("groups by album")
        start_time = datetime.now()
        answr = self.session.query(func.count(Photo.name)).group_by(Photo.albumid).all()
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        print(answr)
        print("albums by time")
        start_time = datetime.now()
        answr = self.session.query(Album).order_by(Album.date).all()
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        for it in answr:
            print(it.name)

    def getPhotos(self):
        answ = self.session.query(Photo).all()
        return answ

    def getAlbums(self):
        answ = self.session.query(Album).all()
        return answ

    def insertPhoto(self, name, description, albumID):
        photo = Photo(name, description, int(albumID))
        self.session.add(photo)
        self.session.commit()

    def insertAlbum(self, name, description, owner):
        album = Album(name, description, owner)
        self.session.add(album)
        self.session.commit()

    def updatePhoto(self, oldname, newname, description, albumID):
        self.session.query(Photo).filter(Photo.name == oldname).update({
            "name": newname,
            "description": description,
            "albumid": albumID})
        self.session.commit()

    def updateAlbum(self, id, name, description, owner):
        self.session.query(Album).filter(Album.id == id).update({
            "name": name,
            "description": description,
            "owner": owner})
        self.session.commit()

    def deletePhoto(self, name):
        self.session.query(Album).filter(Photo.name == name).delete()
        self.session.commit()

    def deleteAlbum(self, id):
        self.session.query(Album).filter(Album.id == id).delete()
        self.session.commit()

    # def getRandomInts(self, max, number):
    #     self.cur.execute("SELECT trunc(random()*%s)::int FROM generate_series(1, %s)", (max, number))
    #     answ = self.cur.fetchall()
    #     return answ
    #
    # def getRandomTexts(self, number , length):
    #     self.cur.execute("select randomText(%s) from generate_series(1,%s)", (length, number))
    #     answ = self.cur.fetchall()
    #     return answ
    #
    # def getPhotosByAttribute(self, attr, val):
    #     if attr == "albumid":
    #         print("hi")
    #         self.cur.execute("select * FROM public.\"Photos\" WHERE albumid = "+val)
    #         return self.cur.fetchall()
    #     self.cur.execute("select * FROM public.\"Photos\" WHERE %s LIKE %s", (attr, val))
    #     return self.cur.fetchall()
    #
    # def getAlbumsByAttribute(self, attr, val):
    #     if attr == "id":
    #         self.cur.execute("select * FROM public.\"Albums\" WHERE id = "+val)
    #         return self.cur.fetchall()
    #     self.cur.execute("select * FROM public.\"Albums\" WHERE %s LIKE %s", (attr, val))
    #     return self.cur.fetchall()
    #

