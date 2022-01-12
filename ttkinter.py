from tkinter import *
from beatifulSoup import *
import smtplib


def kaydet():
    url = link.get(1.0, "end-1c")
    girilen_fiyat0 = hedef_fiyat.get("1.0", "end-1c")
    girilen_fiyat = float(girilen_fiyat0)
    get_product(url,girilen_fiyat)
    link.delete(1.0, "end")
    hedef_fiyat.delete(1.0, "end")


def email():

    FROM = 'pythonproje9@gmail.com'
    TO = 'yscmsen@gmail.com'
    SUBJECT = "Python Proje"
    TEXT = "İlgilendiğiniz ürünün fiyatı düştü"

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (
        FROM, ", ".join(TO), SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(FROM, "marmara1883")
    server.sendmail(FROM, TO, message)


def getir():
    bosluk = Label(frame, text="Ürün adı").grid(column=0, row=0)
    bosluk2 = Label(frame, text="Fiyat").grid(column=1, row=0)
    bosluk2 = Label(frame, text="Değişim").grid(column=2, row=0)
    for x in range(1, db_islemleri.urun_sayisi()+1):
        plabel1 = Label(frame, text=db_islemleri.ad_yazdir(x))
        plabel1.grid(column=0, row=x)
        plabel2 = Label(frame, text=db_islemleri.fiyat_yazdir(x))
        plabel2.grid(column=1, row=x)


def kontrolEt():
    for x in range(1, db_islemleri.urun_sayisi()+1):
        eski_fiyat = db_islemleri.fiyat_yazdir(x)
        db_islemleri.update(get_price_for_update(db_islemleri.get_url(x)), x)
        yeni_fiyat = db_islemleri.fiyat_yazdir(x)
        degisim = yeni_fiyat-eski_fiyat
        if (yeni_fiyat <=db_islemleri.hedef_fiyat_yazdir(x) ):
            email()
            messagebox.showinfo("Bigilendirme","Emailiniz Gönderildi")
        plabel1 = Label(frame, text=degisim)
        plabel1.grid(column=2, row=x)


master = Tk()
master.title("Fiyat Takibi")
master.geometry("600x750")
master.resizable(False, False)
frame = Frame(master, height=550, width=500)
frame0 = Frame(master, height=200, width=600, bg="gray")
frame0.grid(row=0, column=0)
frame.grid(row=1, column=0, sticky="nsew")

link = Text(master, height=1, width=50)
link.place(relx=0.16, rely=0.08)
lbl2 = Label(master, text="Link").place(relx=0.08, rely=0.08)
hedef_fiyat = Text(master, height=1, width=7)
hedef_fiyat.place(relx=0.3, rely=0.15)
lbl1 = Label(master, text="Hedef Fiyat").place(relx=0.08, rely=0.15)


buton = Button(master, text="Kaydet", command=kaydet).place(
    relx=0.8, rely=0.19)

button = Button(master, text="getir", command=getir).place(
    relx=0.31, rely=0.48)
button = Button(master, text="kontrol et", command=kontrolEt).place(
    x=500, y=500)


master.mainloop()
