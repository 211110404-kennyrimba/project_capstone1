from fastapi import FastAPI
from pydantic import BaseModel
from api.db import *



app = FastAPI(title="Mie Ayam bang Willi - API Services", version="1.0.0")

def convert_timedelta(waktu):
    detik = waktu.seconds
    jam = detik // 3600
    menit = (detik % 3600) // 60
    detik = detik % 60
    return "{0}:{1}:{2}".format(jam, menit, detik)


# BASE MODELS
class Reservasi(BaseModel):
    id_pemesanan: int
    nama: str
    email: str
    telp: str
    jum_tamu: int
    tanggal: str
    jam: str
    tambahan: str
    id_user: int
    meja_no: int
    ket_meja: str
    status: str

class Promo(BaseModel):
    usersession: int
    menu: str
    harga_awal: int
    harga_promo: int
    tanggal: str

class Meja(BaseModel):
    no_meja: int
    keterangan: str
    status_meja: str

class User(BaseModel):
    id_user: int
    username: str
    password: str

class DaftarMenu(BaseModel):
    id_menu: int
    menu: str
    harga: int
    path: str

class Update(BaseModel):
    tabel: str
    fieldStatus: str
    status: str
    fieldKondisi: str
    kondisi: str

# INDEX API
@app.get("/api/")
def index():
    return {
        "description": "API status 200"
    }

# API RESERVASI
@app.get("/api/getReservasi")
def getReservasi():
    content = {}
    content["data_reservasi"] = []
    data = getData("SELECT * FROM reservasi")

    for i in data:
        jam = convert_timedelta(i[6])

        content["data_reservasi"].append(
            {
                "id_pemesanan": i[0],
                "nama": i[1],
                "email": i[2],
                "telepon": i[3],
                "jumlah_tamu": i[4],
                "tanggal": i[5],
                "jam": jam,
                "tambahan": i[7],
                "id_user": i[8],
                "no_meja": i[9],
                "ket_meja": i[10],
                "status": i[11],
            }
        )

    return content


@app.get("/api/getReservasiById/{id_pemesanan}")
def getReservasiById(id_pemesanan: int):
    content = {}
    content["data_reservasi"] = []
    data = getOneData(
        "SELECT * FROM reservasi WHERE id_pemesanan='{}'".format(id_pemesanan)
    )

    jam = convert_timedelta(data[6])

    content["data_reservasi"].append(
        {
            "nama": data[1],
            "id_pemesanan": data[0],
            "email": data[2],
            "telepon": data[3],
            "jumlah_tamu": data[4],
            "tanggal": data[5],
            "jam": jam,
            "tambahan": data[7],
            "id_user": data[8],
            "no_meja": data[9],
            "ket_meja": data[10],
            "status": data[11],
        }
    )

    return content

@app.get("/api/getReservasiByIdUser/{id_user}")
def getReservasiById(id_user: int):
    content = {}
    content["data_reservasi"] = []
    data = getData(
        "SELECT * FROM reservasi WHERE id_user='{}'".format(id_user)
    )

    for i in data:
        jam = convert_timedelta(i[6])

        content["data_reservasi"].append(
            {
                "id_pemesanan": i[0],
                "nama": i[1],
                "email": i[2],
                "telepon": i[3],
                "jumlah_tamu": i[4],
                "tanggal": i[5],
                "jam": jam,
                "tambahan": i[7],
                "id_user": i[8],
                "no_meja": i[9],
                "ket_meja": i[10],
                "status": i[11],
            }
        )

    return content

@app.get("/api/getUserByIdReservasi/{id_pemesanan}")
def getUserByIdReservasi(id_pemesanan: int):
    content = {}
    content["data_reservasi"] = []
    data = getOneData(
        "SELECT id_user FROM reservasi WHERE id_pemesanan='{}'".format(id_pemesanan)
    )


    content["data_reservasi"].append(
        {
            "id_user": data[0],
        }
    )

    return content

@app.get("/api/getReservasiByStatus/{status}")
def getReservasiById(status: str):
    content = {}
    content["data_reservasi"] = []
    data = getData(
        "SELECT * FROM reservasi WHERE status='{}'".format(status)
    )

    for i in data:
        jam = convert_timedelta(i[6])

        content["data_reservasi"].append(
            {
                "id_pemesanan": i[0],
                "nama": i[1],
                "email": i[2],
                "telepon": i[3],
                "jumlah_tamu": i[4],
                "tanggal": i[5],
                "jam": jam,
                "tambahan": i[7],
                "id_user": i[8],
                "no_meja": i[9],
                "ket_meja": i[10],
                "status": i[11]
            }
        )

    return content


@app.post("/api/createReservasi/")
def createReservasi(reservasi: Reservasi):
    insertQuery = """
    INSERT INTO reservasi(id_pemesanan, nama, email, telp, jum_tamu, tanggal, jam, tambahan, id_user, meja_no, ket_meja, status) 
    VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')
    """
    execute(
        insertQuery.format(
            reservasi.id_pemesanan,
            reservasi.nama,
            reservasi.email,
            reservasi.telp,
            reservasi.jum_tamu,
            reservasi.tanggal,
            reservasi.jam,
            reservasi.tambahan,
            reservasi.id_user,
            reservasi.meja_no,
            reservasi.ket_meja,
            reservasi.status,
        )
    )

    return {"message": "success"}


@app.post("/api/updateReservasi/{id}")
def updateReservasi(id: int, reservasi: Reservasi):
    updateQuery = """
    UPDATE reservasi SET 
    id_pemesanan = '{0}', nama = '{1}', email = '{2}', telp = '{3}', jum_tamu = '{4}', 
    tanggal = '{5}', jam = '{6}', tambahan = '{7}', id_user = '{8}', meja_no = '{9}', 
    ket_meja = '{10}', status = '{11}' WHERE reservasi.id_pemesanan = {12}
    """
    execute(
        updateQuery.format(
            reservasi.id_pemesanan,
            reservasi.nama,
            reservasi.email,
            reservasi.telp,
            reservasi.jum_tamu,
            reservasi.tanggal,
            reservasi.jam,
            reservasi.tambahan,
            reservasi.id_user,
            reservasi.meja_no,
            reservasi.ket_meja,
            reservasi.status,
            id,
        )
    )

    return {"message": "success"}


@app.delete("/api/deleteReservasi/{id}")
def deleteReservasi(id):
    execute("DELETE FROM reservasi WHERE id_pemesanan='{}'".format(id))

    return {"message": "success"}


# API PROMO
@app.get("/api/getPromo")
def getPromo():
    content = {}
    content["data_promo"] = []
    data = getData("SELECT * FROM promo")

    for i in data:

        content["data_promo"].append(
            {
                "id_promo": i[0],
                "menu": i[1],
                "harga_awal": i[2],
                "harga_promo": i[3],
                "tanggal": i[4]
            }
        )

    return content

@app.get("/api/getCurrentPromo")
def getCurrentPromo():
    content = {}
    content["data_promo"] = []
    data = getData("SELECT * FROM promo WHERE tanggal >= CURDATE()")

    for i in data:

        content["data_promo"].append(
            {
                "id_promo": i[0],
                "menu": i[1],
                "harga_awal": i[2],
                "harga_promo": i[3],
                "tanggal": i[4]
            }
        )

    return content


@app.get("/api/getPromoById/{id_promo}")
def getPromoById(id_promo: int):
    content = {}
    content["data_promo"] = []
    data = getOneData(
        "SELECT * FROM promo WHERE id_promo='{}'".format(id_promo)
    )


    content["data_promo"].append(
        {
            "id_promo": data[0],
            "menu": data[1],
            "harga_awal": data[2],
            "harga_promo": data[3],
            "tanggal": data[4]
        }
    )

    return content


@app.post("/api/createPromo/")
def createPromo(promo: Promo):
    insertQuery = """
    INSERT INTO promo(id_promo, menu, harga_awal, harga_promo, tanggal) VALUES ('','{0}','{1}','{2}','{3}')
    """
    if promo.usersession == 1:
        execute(
            insertQuery.format(
                promo.menu,
                promo.harga_awal,
                promo.harga_promo,
                promo.tanggal
            )
        )
        return {"message": "success"}
    else:
        return{"message":"failed"}




@app.post("/api/updatePromo/{id}")
def updatePromo(id: int, promo: Promo):
    updateQuery = """
    UPDATE promo SET menu = '{0}', harga_awal = '{1}', harga_promo = '{2}', tanggal = '{3}' WHERE promo.id_promo = {4}
    """
    execute(
        updateQuery.format(
            promo.menu,
            promo.harga_awal,
            promo.harga_promo,
            promo.tanggal,
            id
        )
    )

    return {"message": "success"}


@app.delete("/api/deletePromo/{id}")
def deletePromo(id):
    execute("DELETE FROM promo WHERE id_promo='{}'".format(id))

    return {"message": "success"}


# API MEJA
@app.get("/api/getMeja")
def getMeja():
    content = {}
    content["data_meja"] = []
    data = getData("SELECT * FROM meja")

    for i in data:

        content["data_meja"].append(
            {
                "no_meja": i[0],
                "keterangan": i[1],
                "status_meja": i[2]
            }
        )

    return content


@app.get("/api/getMejaById/{no_meja}")
def getMejaById(no_meja: int):
    content = {}
    content["data_meja"] = []
    data = getData(
        "SELECT * FROM meja WHERE no_meja='{}'".format(no_meja)
    )

    for i in data:

        content["data_meja"].append(
            {
                "no_meja": i[0],
                "keterangan": i[1],
                "status_meja": i[2]
            }
        )

    return content

@app.get("/api/getMejaNoById/{id_pemesanan}")
def getMejaNoById(id_pemesanan: int):
    content = {}
    content["data_meja"] = []
    data = getOneData("SELECT meja_no FROM reservasi WHERE id_pemesanan='{}'".format(id_pemesanan))

    content["data_meja"].append(
        {
            "no_meja": data[0]
        }
    )

    return content


@app.post("/api/createMeja/")
def createMeja(meja: Meja):
    insertQuery = """
    INSERT INTO meja(no_meja, keterangan, status_meja) VALUES ('{0}','{1}','{2}')
    """
    execute(
        insertQuery.format(
            meja.no_meja,
            meja.keterangan,
            meja.status_meja
        )
    )

    return {"message": "success"}


@app.post("/api/updateMeja/{no_meja}")
def updateMeja(no_meja: int, meja: Meja):
    updateQuery = """
    UPDATE meja SET 
    no_meja = '{0}', keterangan = '{1}', status_meja = '{2}' WHERE meja.no_meja = {3}
    """
    execute(
        updateQuery.format(
            meja.no_meja,
            meja.keterangan,
            meja.status_meja,
            no_meja
        )
    )

    return {"message": "success"}


@app.delete("/api/deleteMeja/{no_meja}")
def deleteMeja(no_meja):
    execute("DELETE FROM meja WHERE no_meja='{}'".format(no_meja))

    return {"message": "success"}


# API DAFTAR MENU
@app.get("/api/getDaftarMenu")
def getDaftarMenu():
    content = {}
    content["data_menu"] = []
    data = getData("SELECT * FROM daftar_menu")
    for i in data:

        content["data_menu"].append(
            {
                "id_menu": i[0],
                "menu": i[1],
                "harga": i[2],
                "path": i[3]
            }
        )
    print("CONTENT API DAFTAR MENU : -----------------------------------------------------------")
    return content


@app.get("/api/getIdMenu")
def getIdMenu():
    content = {}
    content["data_menu"] = []
    data = getData("SELECT id_menu FROM daftar_menu")

    for i in data:

        content["data_menu"].append(
            {
                "id_menu": i[0]
            }
        )

    return content


@app.get("/api/getDaftarMenuById/{id_menu}")
def getDaftarMenuById(id_menu: int):
    content = {}
    content["data_menu"] = []
    data = getData(
        "SELECT * FROM daftar_menu WHERE id_menu='{}'".format(id_menu)
    )

    for i in data:

        content["data_menu"].append(
            {
                "id_menu": i[0],
                "menu": i[1],
                "harga": i[2],
                "path": i[3]
            }
        )

    return content

@app.get("/api/getHargaMenuById/{id_menu}")
def getHargaMenuById(id_menu: int):
    content = {}
    content["data_menu"] = []
    data = getOneData(
        "SELECT harga FROM daftar_menu WHERE id_menu='{}'".format(id_menu)
    )


    content["data_menu"].append(
        {
            "harga": data[0],
        }
    )

    return content

@app.get("/api/getMenuById/{id_menu}")
def getMenuById(id_menu: int):
    content = {}
    content["data_menu"] = []
    data = getOneData(
        "SELECT menu FROM daftar_menu WHERE id_menu='{}'".format(id_menu)
    )


    content["data_menu"].append(
        {
            "menu": data[0]
        }
    )

    return content



@app.post("/api/createDaftarMenu/")
def createDaftarMenu(menu: DaftarMenu):
    insertQuery = """
    INSERT INTO daftar_menu(id_menu, menu, harga, path) VALUES ('{0}','{1}','{2}','{3}')
    """
    execute(
        insertQuery.format(
            menu.id_menu,
            menu.menu,
            menu.harga,
            menu.path
        )
    )

    return {"message": "success"}


@app.post("/api/updateDaftarMenu/{id_menu}")
def updateMenu(id_menu: int, menu: DaftarMenu):
    updateQuery = """
    UPDATE daftar_menu SET 
    id_menu= '{0}', menu = '{1}', harga = '{2}', path='{3}' WHERE daftar_menu.id_menu = '{4}'
    """
    execute(
        updateQuery.format(
            menu.id_menu,
            menu.menu,
            menu.harga,
            menu.path,
            id_menu
        )
    )

    return {"message": "success"}


@app.delete("/api/deleteDaftarMenu/{id_menu}")
def deleteMeja(id_menu):
    execute("DELETE FROM daftar_menu WHERE id_menu='{}'".format(id_menu))

    return {"message": "success"}

# API USER
@app.get("/api/getUser")
def getUser():
    content = {}
    content["data_user"] = []
    data = getData("SELECT * FROM user")

    for i in data:

        content["data_user"].append(
            {
                "id_user": i[0],
                "username": i[1],
                "password": i[2]
            }
        )

    return content


@app.get("/api/getUserById/{id_user}")
def getUserById(id_user: int):
    content = {}
    content["data_user"] = []
    data = getOneData(
        "SELECT * FROM user WHERE id_user='{}'".format(id_user)
    )
        
    content["data_user"].append(
        {
                "id_user": data[0],
                "username": data[1],
                "password": data[2]
        }
    )

    return content


@app.post("/api/createUser/")
def createUser(user: User):
    insertQuery = """
    INSERT INTO user(id_user, username, password) VALUES ('{0}','{1}','{2}')
    """
    execute(
        insertQuery.format(
            user.id_user,
            user.username,
            user.password
        )
    )

    return {"message": "success"}


@app.post("/api/updateUser/{id}")
def updateUser(id: int, user: User):
    updateQuery = """
    UPDATE user SET 
    id_user= '{0}', username = '{1}', password = '{2}' WHERE user.id_user = '{3}'
    """
    execute(
        updateQuery.format(
            user.id_user,
            user.username,
            user.password,
            id
        )
    )

    return {"message": "success"}


@app.delete("/api/deleteUser/{id}")
def deleteMeja(id):
    execute("DELETE FROM user WHERE id_user='{}'".format(id))

    return {"message": "success"}


# API UPDATE ANY
@app.post("/api/updateAny/{id}")
def updateAny(update: Update):
    updateQuery = """
        UPDATE {0} SET {1}= '{2}' WHERE {3} = '{4}'
        """
    execute(
        updateQuery.format(
            update.tabel,
            update.fieldStatus,
            update.status,
            update.fieldKondisi,
            update.kondisi,
        )
    )

    return {"message": "success"}
