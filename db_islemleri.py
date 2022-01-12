import sqlite3
conn = sqlite3.connect("yenidb.db")
c = conn.cursor()


class db_islemleri:

    def db_ekle(ad, fiyat, url,hedef):
        c.execute("INSERT INTO yenidb (ad,fiyat,url,hedef) VALUES (?,?,?,?)",
                  (ad, fiyat, url,hedef))
        conn.commit()

    def get_id(x):
        c.execute("SELECT * FROM yenidb WHERE id=:id", {"id": x})
        return c.fetchone()[0]

    def ad_yazdir(x):
        c.execute("SELECT * FROM yenidb WHERE id=:id", {"id": x})
        return c.fetchone()[1]

    def fiyat_yazdir(x):
        c.execute("SELECT * FROM yenidb WHERE id=:id", {"id": x})
        return c.fetchone()[2]
    
    def hedef_fiyat_yazdir(x):
        c.execute("SELECT * FROM yenidb WHERE id=:id", {"id": x})
        return c.fetchone()[4]

    def urun_sayisi():
        c.execute("SELECT * FROM yenidb")
        return len(c.fetchall())

    def update(fiyat, x):
        c.execute("UPDATE yenidb SET fiyat=:fiyat WHERE id=:id",
                  {"fiyat": fiyat, "id": x})
        conn.commit()

    def get_url(x):
        c.execute("SELECT * FROM yenidb WHERE id=:id", {"id": x})
        return c.fetchone()[3]
