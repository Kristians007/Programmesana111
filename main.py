from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def te():
    return render_template("tests.html")

@app.route("/saraksts")
def saraksts() :
    saraksts = ["Anna", "Katls", "Kartupelis"]
    bildes = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcCG4898FTkK5IUBMpLleBHtjK3jUILS3YsjCFfLr56g&s", "https://arkolat.lv/storage/uploads/global/product_images/image/000/055/684/large/ef387b5ad94e9169c7f220dda11f92da.jpg", "https://rimibaltic-res.cloudinary.com/image/upload/b_white,c_fit,f_auto,h_480,q_auto,w_480/d_ecommerce:backend-fallback.png/MAT_280354_KGM_LV"]
    kopejais_saraksts = ["Anna",https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcCG4898FTkK5IUBMpLleBHtjK3jUILS3YsjCFfLr56g&s], ["Katls",https://arkolat.lv/storage/uploads/global/product_images/image/000/055/684/large/ef387b5ad94e9169c7f220dda11f92da.jpg ], ["Kartupelis",https://rimibaltic-res.cloudinary.com/image/upload/b_white,c_fit,f_auto,h_480,q_auto,w_480/d_ecommerce:backend-fallback.png/MAT_280354_KGM_LV ]
    return render_template("saraksts.html", vardi = saraksts, garums = len(saraksts))

if __name__=='__main__':
    app.run(port = 5000)

print("Sveiki!")

