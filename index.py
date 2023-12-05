from tkinter import *
from tkinter import messagebox, ttk
import tempfile
import random
from time import strftime
from PIL import ImageTk, Image
import os

class Super_marche:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Marché")
        self.root.geometry("1920x1040+0+0")

        title = Label(self.root, text="Super Marché Jessy Vettard", font=("Algerian", 23), bg="cyan", fg="black")
        title.pack(side=TOP, fill=X)

        def heure():
            heur = strftime("%H:%M:%S")
            lblheure.config(text=heur)
            lblheure.after(1000,heure)

        lblheure = Label(self.root, text="HH:MM:SS", font=("times new roman", 11, "bold"), bg="cyan", fg="black")
        lblheure.place(x=0, y=5, width=80, height=30)    

        heure()
        #Nos variables
        self.c_nom = StringVar()
        self.c_phon = StringVar()

        self.n_factu = StringVar()
        z = random.randint(1000,9999)
        self.n_factu.set(z)

        self.c_email = StringVar()
        self.rech_factu = StringVar()
        self.produit = StringVar()
        self.prix = IntVar()
        self.qte = IntVar()
        self.totalbrute = StringVar()
        self.taxe = StringVar()
        self.totalnet = StringVar()


        ##Liste categorie
        self.list_categorie = ["Selection", "Vêtement", "Style de vie", "Téléphone"]

        #Sous categorie vetement
        self.list_souscategorieVetement = ["Pantalon", "T-Shirt","Shirt"]

        self.pantalon = ["Levis","Mufti","Skykar"]
        self.price_levis = 5000
        self.price_mufti = 1000
        self.price_skykar = 3000

        self.t_shirt = ["Polo", "Roadister", "Jack&Jones"]
        self.price_polo = 1500
        self.price_roadister = 2550
        self.price_jack_jones = 3600

        self.shirt =  ["Peter England", "Louis Philipe","Park Avenue"]
        self.price_peter_england = 5000
        self.price_louis_philipe = 6000
        self.price_park_avenue = 9000

        #Sous categorie style de vie
        self.list_souscategorieStyle = ["Bath Soap", "Crème","Huile de cheuveux"]

        self.bath_soap = ["LifeBuy","Lux","Santoor","Pearl"]
        self.price_lifebuy = 500
        self.price_lux = 2400
        self.price_santoor = 1450
        self.price_pearl = 2100

        self.creme = ["Fair&Lovely", "Ponds", "Olay","Garnier"]
        self.price_fair = 1560
        self.price_pond = 2550
        self.price_olay = 4530
        self.price_garnier = 1250

        self.huile_cheveux =  ["Parachute", "Jashmin","Bajaj"]
        self.price_parachute = 1450
        self.price_jashmin = 2300
        self.price_bajaj = 1500

        #Sous categorie téléphone
        self.list_souscategorieTel = ["Iphone", "Samsung","Huawei","Techno"]

        self.iphone = ["Iphone X","Iphone 11","Iphone 12"]
        self.price_ix = 45000
        self.price_i11 = 65000
        self.price_i12 = 93000

        self.samsung = ["Samsung M16", "Samsung M12","Samsung M21"]
        self.price_sm16 = 15600
        self.price_sm12 = 25600
        self.price_sm21 = 30600

        self.huawei =  ["Huawei y9S", "Huawei P8","Huawei Mate"]
        self.price_y9S = 1450
        self.price_p8 = 20000
        self.price_mate = 29600

        self.techno =  ["Techno Com 11", "Techno Com 12","Techno Com 13"]
        self.price_com11 = 23600
        self.price_com12 = 29200
        self.price_com13 = 35600

        Main_Frame = Frame(self.root, bd=2, relief=GROOVE, bg='white')
        Main_Frame.place(x=0, y=40, width=1890, height=920)

        #client---------------------------------------------
        client_frame = LabelFrame(Main_Frame, text="Client", font=("times new roman", 9), bg="white")
        client_frame.place(x=0, y=0, width=237, height=100)

        self.lbl_contact = Label(client_frame, text='Contact', font=("times new roman", 11, "bold"), bg="white")
        self.lbl_contact.grid(row=0, column=0,sticky=W, padx=3, pady=1)

        self.lbl_nomclient = Label(client_frame, text='Nom client', font=("times new roman", 11, "bold"), bg="white")
        self.lbl_nomclient.grid(row=1, column=0,sticky=W, padx=3, pady=1)

        self.lbl_email = Label(client_frame, text='Email', font=("times new roman", 11, "bold"), bg="white")
        self.lbl_email.grid(row=2, column=0,sticky=W, padx=3, pady=1)

        self.txt_contact = ttk.Entry(client_frame,textvariable=self.c_phon, font=("times new roman", 11))
        self.txt_contact.grid(row=0, column=1, sticky=W, padx=3, pady=1)

        self.txt_nomclient = ttk.Entry(client_frame,textvariable=self.c_nom, font=("times new roman", 11))
        self.txt_nomclient.grid(row=1, column=1, sticky=W, padx=3, pady=1)

        self.txt_email = ttk.Entry(client_frame,textvariable=self.c_email, font=("times new roman", 11))
        self.txt_email.grid(row=2, column=1, sticky=W, padx=3, pady=1)

        #Produits

        produit_frame = LabelFrame(Main_Frame, text="Produit", font=("times new roman", 9), bg="white")
        produit_frame.place(x=240, y=0, width=600, height=100)

        self.lbl_categori = Label(produit_frame, text="Selectionner la categorie", font=("times new roman", 11, "bold"), bg="white")
        self.lbl_categori.grid(row=0, column=0, sticky=W, padx= 3, pady=1)

        self.lbl_souscategori = Label(produit_frame, text="Sous categorie", font=("times new roman", 11, "bold"), bg="white")
        self.lbl_souscategori.grid(row=1, column=0, sticky=W, padx=3, pady=1)

        self.lbl_nomproduit = Label(produit_frame, text="Nom du produit", font=("times new roman", 11, "bold"), bg="white")
        self.lbl_nomproduit.grid(row=2, column=0, sticky=W, padx=3, pady=1)

        self.lbl_prix = Label(produit_frame, text="Prix", font=("times new roman", 11, "bold"), bg="white")
        self.lbl_prix.grid(row=0, column=2, sticky=W, padx=3, pady=1)

        self.lbl_qte = Label(produit_frame, text="Quantité", font=("times new roman", 11, "bold"), bg="white")
        self.lbl_qte.grid(row=1, column=2, sticky=W, padx=3, pady=1)

        self.txt_categorie = ttk.Combobox(produit_frame, font=("times new roman", 10), values=self.list_categorie, width=24, state="readonly")
        self.txt_categorie.grid(row=0, column=1, sticky=W, padx=3, pady=1)
        self.txt_categorie.current(0)
        self.txt_categorie.bind("<<ComboboxSelected>>", self.fonctionCategorie)

        self.txt_souscategorie = ttk.Combobox(produit_frame, font=("times new roman", 10), values=[""], width=24, state="readonly")
        self.txt_souscategorie.grid(row=1, column=1, sticky=W, padx=3, pady=1)
        self.txt_souscategorie.current(0)
        self.txt_souscategorie.bind("<<ComboboxSelected>>", self.fonctionsousCategorie)

        self.txt_nomproduit = ttk.Combobox(produit_frame, font=("times new roman", 10), textvariable=self.produit, width=24, state="readonly")
        self.txt_nomproduit.grid(row=2, column=1, sticky=W, padx=3, pady=1)
        self.txt_nomproduit.bind("<<ComboboxSelected>>", self.fonctionnomproduit)

        self.txt_prix = ttk.Combobox(produit_frame, font=("times new roman", 10), textvariable=self.prix, width=24, state="readonly")
        self.txt_prix.grid(row=0, column=3, sticky=W, padx=3, pady=1)
        
        self.txt_qte = ttk.Entry(produit_frame, font=("times new roman", 10), textvariable=self.qte, width=24,)
        self.txt_qte.grid(row=1, column=3, sticky=W, padx=3, pady=1)

        #Recherche
        recher_Frame = Frame(Main_Frame, bd=2, bg="white")
        recher_Frame.place(x=850, y=0, width=400, height=70)

        self.lbl_recherche = Label(recher_Frame, text="N Facture",font=("times new roman",11,"bold"),bg="white")
        self.lbl_recherche.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_recherche = ttk.Entry(recher_Frame, textvariable=self.rech_factu, font=("times new roman", 11), width=15)
        self.txt_recherche.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.btn_recherch = Button(recher_Frame, text="Rechercher", command=self.rechercher, height=2, font=("times new roman", 11, "bold"), bg="yellow", width=9, cursor="hand2")
        self.btn_recherch.grid(row=0, column=2)

        #Espace facture

        Facture_label = LabelFrame(Main_Frame, text="Facture", font=("times new roman", 11, "bold"), bg="white")
        Facture_label.place(x=850, y=50, width=500,  height=480)
        scroll_y = Scrollbar(Facture_label, orient=VERTICAL)
        self.textarea = Text(Facture_label, yscrollcommand=scroll_y.set, font=("times new roman", 11, "bold"), bg="white", fg="black")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
    
        


        #Enbas
        enbas_frame = LabelFrame(Main_Frame, text="Boutton", font=("times new roman", 11), bg="gray")
        enbas_frame.place(x=0, y=530, width=1880, height=180)

        self.lbl_totalbrute = Label(enbas_frame, text="Total Brute", font=("times new roman ", 9,"bold"), bg="gray")
        self.lbl_totalbrute.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.lbl_taxe = Label(enbas_frame, text="Taxe", font=("times new roman ", 11,"bold"), bg="gray")
        self.lbl_taxe.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbl_totalnet = Label(enbas_frame, text="Total Net", font=("times new roman ", 11,"bold"), bg="gray")
        self.lbl_totalnet.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_totalbrute = ttk.Entry(enbas_frame, textvariable=self.totalbrute, font=("times new roman", 11), width=15, state="readonly")
        self.txt_totalbrute.grid(row=0, column=1, sticky=W, padx=5, pady=2)        
        
        self.txt_taxe = ttk.Entry(enbas_frame, textvariable=self.taxe, font=("times new roman", 11), width=15, state="readonly")
        self.txt_taxe.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.txt_totalnet = ttk.Entry(enbas_frame, textvariable=self.totalnet, font=("times new roman", 11), width=15, state="readonly")
        self.txt_totalnet.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        
        ##Image
        self.imge = ImageTk.PhotoImage(Image.open("C:/Users/TOSHIBA/Desktop/Jv/Developpement/Mini_projetTkinter/SuperMarche/image/image.jpg"))
        self.lbl_image = Label(image=self.imge)
        self.lbl_image.place(x=0, y=145, width=845, height= 430)

        #Boutton

        Btn_Frame = Frame(enbas_frame, bd=2, bg="white")
        Btn_Frame.place(x=240, y=0)

        self.ajoutPanier = Button(Btn_Frame, text = "Ajouter",command=self.ajouter, height=2, font=("times new roman", 11, "bold"),bg="cyan", width=18, cursor="hand2")
        self.ajoutPanier.grid(row=0, column=0)

        self.generer = Button(Btn_Frame, text = "Générer",command=self.genererFacture, height=2, font=("times new roman", 11, "bold"),bg="green", width=18, cursor="hand2")
        self.generer.grid(row=0, column=1)

        self.sauvFacture = Button(Btn_Frame, text = "Sauvegarde Facture",command=self.sauvegarder, height=2, font=("times new roman", 11, "bold"),bg="gray", width=18, cursor="hand2")
        self.sauvFacture.grid(row=0, column=2)

        self.imprimer = Button(Btn_Frame, text = "Imprimer",command=self.imprimer, height=2, font=("times new roman", 11, "bold"),bg="green", width=18, cursor="hand2")
        self.imprimer.grid(row=0, column=3)

        self.reinitialiser = Button(Btn_Frame, text = "Reinitialiser", height=2, font=("times new roman", 11, "bold"),bg="yellow", width=18, cursor="hand2")
        self.reinitialiser.grid(row=0, column=4)

        self.quitter = Button(Btn_Frame, text = "Quitter",command=self.quitter_app, height=2, font=("times new roman", 11, "bold"),bg="red", width=18, cursor="hand2")
        self.quitter.grid(row=0, column=5)

        self.Bienvenue()
        self.l=[]
        ##########Fonctions

    def Bienvenue(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t\tBienvenue chez Super Marché Vettard")
        self.textarea.insert(END, f"\n\nNuméro Facture : {self.n_factu.get()}")
        self.textarea.insert(END, f"\n\nNom du client : {self.c_nom.get()}")
        self.textarea.insert(END, f"\n\nTèl : {self.c_phon.get()}")
        self.textarea.insert(END, f"\n\nEmail : {self.c_email.get()}")
        self.textarea.insert(END,"\n====================================================")
        self.textarea.insert(END,f"\n\nProduits\t\tQTE\t\t")
        self.textarea.insert(END,"\n====================================================")


    def ajouter(self):
        self.n = self.prix.get()
        self.m = self.qte.get()*self.n
        self.l.append(self.m)
        if self.produit.get()=="":
            messagebox.showerror("Erreur","Selectionner un produit")
        else:
            self.textarea.insert(END, f"\n{self.produit.get()}\t\t{self.qte.get()}")
            self.donneCommande=self.textarea.get(1.0,END)
            #f0=open("/Users/TOSHIBA/Desktop/Jv/Developpement/Mini_projetTkinter/SuperMarche/Facture/commande.txt","w")
            #f0.write(self.donneCommande)
            #messagebox.showinfo("L'article a été enregistré avec succès")
            #f0.close()
            self.totalbrute.set(str("%.2f"%(sum(self.l))))
            self.taxe.set(str("%.2f"%((((sum(self.l))-(self.prix.get()))*1)/100)))
            self.totalnet.set(str("%.2f"%(((sum(self.l))+((((sum(self.l))-(self.prix.get()))*1)/100)))))
    
    # generer facture 
    def genererFacture(self):
        if self.produit.get()=="":
            messagebox.showerror("Erreur", "Ajouter d'abord un produit")
        else:
            text= self.textarea.get(10.0, (10.0+float(len(self.l))))
            self.Bienvenue()
            text = self.textarea.insert(END, text)
            self.textarea.insert(END,"\n====================================================")
            self.textarea.insert(END, f"\nProduit acheté : \t\t\t{self.produit.get()}") 
            self.textarea.insert(END, f"\nQuantité : \t\t\t{self.qte.get()}")
            self.textarea.insert(END, f"\nPrix de l'article : \t\t\t{self.prix.get()}")
            self.textarea.insert(END,"\n====================================================")
            self.textarea.insert(END, f"\nTotal Brute : \t\t\t{self.totalbrute.get()}") 
            self.textarea.insert(END, f"\nTaxe : \t\t\t{self.taxe.get()}")
            self.textarea.insert(END, f"\nTotal Net : \t\t\t{self.totalnet.get()}")

    # Sauvegarde facture 
    def sauvegarder(self):
        op=messagebox.askyesno("Sauvegarder","Voulez-vous sauvegarder la facture ?")
        if op==True:
            self.donneFacture=self.textarea.get(1.0,END)
            f1=open("/Users/TOSHIBA/Desktop/Jv/Developpement/Mini_projetTkinter/SuperMarche/Facture/"+str(self.n_factu.get())+".txt","w")
            f1.write(self.donneFacture)
            messagebox.showinfo("Sauvegarder",f"La facture numéro {self.n_factu.get()} a été enregistré avec succès")
            f1.close()
        
    def imprimer(self):
        fichier = tempfile.mktemp(".txt")
        open(fichier, "w").write(self.textarea.get("1.0",END))
        os.startfile(fichier, "print")

    def rechercher(self):
        trouver = "non"
        for i in os.listdir("/Users/TOSHIBA/Desktop/Jv/Developpement/Mini_projetTkinter/SuperMarche/Facture/"):
            if i.split(".")[0]==self.rech_factu.get():
                f1 = open(f"/Users/TOSHIBA/Desktop/Jv/Developpement/Mini_projetTkinter/SuperMarche/Facture/{i}","r")
                self.textarea.delete(1.0, END)
                for d in f1:
                    self.textarea.insert(END, d)
                    f1.close
                    trouver="oui"
        if trouver=="non":
            messagebox.showerror("Erreur", "La facture n'existe pas")


    def fonctionCategorie(self, even=""):
        # Style de vie 
        if self.txt_categorie.get()=="Vêtement":
            self.txt_souscategorie.config(values=self.list_souscategorieVetement)
            self.txt_souscategorie.current(0)

        if self.txt_categorie.get()=="Style de vie":
            self.txt_souscategorie.config(values=self.list_souscategorieStyle)
            self.txt_souscategorie.current(0)

        if self.txt_categorie.get()=="Téléphone":
            self.txt_souscategorie.config(values=self.list_souscategorieTel)
            self.txt_souscategorie.current(0)

    def fonctionsousCategorie(self, even=""):
            #Vetement
        if self.txt_souscategorie.get()=="Pantalon":
            self.txt_nomproduit.config(values=self.pantalon)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="T-Shirt":
            self.txt_nomproduit.config(values=self.t_shirt)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="Shirt":
            self.txt_nomproduit.config(values=self.shirt)
            self.txt_nomproduit.current(0)
        
        #Style de vie 
        if self.txt_souscategorie.get()=="Bath Soap":
            self.txt_nomproduit.config(values=self.bath_soap)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="Crème":
            self.txt_nomproduit.config(values=self.creme)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="Huile de cheveux":
            self.txt_nomproduit.config(values=self.huile_cheveux)
            self.txt_nomproduit.current(0)
        
        #Telephone
        if self.txt_souscategorie.get()=="Iphone":
            self.txt_nomproduit.config(values=self.iphone)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="Samsung":
            self.txt_nomproduit.config(values=self.samsung)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="Huawei":
            self.txt_nomproduit.config(values=self.huawei)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="Techno":
            self.txt_nomproduit.config(values=self.techno)
            self.txt_nomproduit.current(0)

    def fonctionnomproduit(self, event=""):
        #vetement 
        if self.txt_nomproduit.get()=="Levis":
            self.txt_prix.config(values=self.price_levis)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Mufti":
            self.txt_prix.config(values=self.price_mufti)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Skykar":
            self.txt_prix.config(values=self.price_skykar)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Polo":
            self.txt_prix.config(values=self.price_polo)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Roadister":
            self.txt_prix.config(values=self.price_roadister)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Jack&Jones":
            self.txt_prix.config(values=self.price_jack_jones)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Peter England":
            self.txt_prix.config(values=self.price_peter_england)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Louis Philip":
            self.txt_prix.config(values=self.price_louis_philipe)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Park Avenue":
            self.txt_prix.config(values=self.price_park_avenue)
            self.txt_prix.current(0)
            self.qte.set(1)

            #style life

        if self.txt_nomproduit.get()=="LifeBuy":
            self.txt_prix.config(values=self.price_lifebuy)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Lux ":
            self.txt_prix.config(values=self.price_lux)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Santoor ":
            self.txt_prix.config(values=self.price_santoor)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Pearl ":
            self.txt_prix.config(values=self.price_pearl)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Fair&Lovely ":
            self.txt_prix.config(values=self.price_fair)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Ponds":
            self.txt_prix.config(values=self.price_pond)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Olay":
            self.txt_prix.config(values=self.price_olay)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Garnier":
            self.txt_prix.config(values=self.price_garnier)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Parachute":
            self.txt_prix.config(values=self.price_parachute)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Jashmin":
            self.txt_prix.config(values=self.price_jashmin)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Bajaj":
            self.txt_prix.config(values=self.price_bajaj)
            self.txt_prix.current(0)
            self.qte.set(1)

        #######Phone

        if self.txt_nomproduit.get()=="Iphone X":
            self.txt_prix.config(values=self.price_ix)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Iphone 11":
            self.txt_prix.config(values=self.price_i11)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Iphone 12":
            self.txt_prix.config(values=self.price_i12)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Samsung M16":
            self.txt_prix.config(values=self.price_sm16)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Samsung M12":
            self.txt_prix.config(values=self.price_sm12)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Samsung M21":
            self.txt_prix.config(values=self.price_sm16)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Huawei Y9S":
            self.txt_prix.config(values=self.price_y9S)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Huawei P8":
            self.txt_prix.config(values=self.price_p8)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Huawei Mate":
            self.txt_prix.config(values=self.price_mate)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Techno Com11":
            self.txt_prix.config(values=self.price_com11)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Techno Com12":
            self.txt_prix.config(values=self.price_com12)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Techno Com13":
            self.txt_prix.config(values=self.price_com13)
            self.txt_prix.current(0)
            self.qte.set(1)

    def quitter_app(self):

        op = messagebox.askyesno("Quitter", "Voulez vous quitter")
        if op > 0:
            self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj = Super_marche(root)
    root.mainloop()
