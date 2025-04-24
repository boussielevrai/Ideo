import requests
import json
import tkinter as tk
import webbrowser
import os
from tkinter import messagebox
from tkinter import StringVar

def phi4():
    model1 = "phi4"


def llama():
    model1 = "llama3.2"
def deepseek():
    model1 = "deepseekR1"    

def on():
    file_path = os.path.abspath('/home/v/Bureau/pong.html')
    webbrowser.open('file://' + file_path)

def nouvelle_fonction1():
    print("Bouton Nouvelle fonction 1 cliqué")

def nouvelle_fonction2():
    print("Bouton Nouvelle fonction 2 cliqué")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Ideo_0.96")
fenetre.geometry("400x300")  # Définir la taille de la fenêtre
fenetre.resizable(True, True)  # Permettre le redimensionnement
fenetre.configure(bg="#f0f0f0")  # Fond gris clair

# Style pour les widgets
style = {
    "button": {
        "bg": "blue",  # Couleur verte
        "fg": "white",
        "font": ("Arial", 12),
        "padx": 10,
        "pady": 5,
        "relief": tk.RAISED,  # Donner un effet de relief au bouton
        "borderwidth": 2,
    },
    "label": {
        "bg": "#f0f0f0",  # Fond gris clair
        "fg": "black",
        "font": ("Arial", 12),
        "padx": 20,
        "pady": 10,
    }
}

# Créer un bouton stylisé
button1 = tk.Button(
    fenetre,
    text="Jouer à pong pour patienter",
    command=on,
    **style["button"]
)
button1.pack(pady=10)

# Créer un autre bouton stylisé
button2 = tk.Button(
    fenetre,
    text="Haute qualité d'information",
    command=phi4,
    **style["button"]
)
button2.pack(pady=10)

# Créer deux boutons supplémentaires
button3 = tk.Button(
    fenetre,
    text="qualité d'information moyenne",
    command=nouvelle_fonction1,
    **style["button"]
)
button3.pack(pady=10)

button4 = tk.Button(
    fenetre,
    text="qualité d'information basse",
    command=nouvelle_fonction2,
    **style["button"]
)
button4.pack(pady=10)

# Créer un label stylisé
label = tk.Label(
    fenetre,
    text="fermez cette fenétre pour commencer",
    justify=tk.CENTER,  # Centrer le texte
    **style["label"]
)
label.pack(pady=20)

# Centrer les widgets verticalement et horizontalement
fenetre.update()
fenetre.geometry(f"{fenetre.winfo_width()}x{fenetre.winfo_height()}")

# Lancer la boucle principale de l'application
fenetre.mainloop()



def on_select(value):
    print(f"Option sélectionnée : {value}")



def on_select(value):
    global model  # Indique que nous utilisons la variable globale `model`
    model = value  # Stocke la valeur sélectionnée dans la variable `model`
    print(f"Option sélectionnée : {model}")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("choix du llm pour la recherche locale")
fenetre.geometry("300x200")
fenetre.configure(bg="#f0f0f0")

# Liste des options
options = ["mistral", "phi4", "llama3.1", "DeepseekR1"]

# Variable pour stocker l'option sélectionnée
selected_option = StringVar(fenetre)
selected_option.set(options[0])  # Définir une option par défaut

# Créer le menu déroulant
menu_deroulant = tk.OptionMenu(fenetre, selected_option, *options, command=on_select)
menu_deroulant.pack(pady=20)

# Créer un label pour afficher l'option sélectionnée
label = tk.Label(fenetre, text="Llm choisi :", bg="#f0f0f0", font=("Arial", 12))
label.pack(pady=10)

# Créer un label pour afficher la valeur de l'option sélectionnée
label_valeur = tk.Label(fenetre, textvariable=selected_option, bg="#f0f0f0", font=("Arial", 12))
label_valeur.pack(pady=10)

# Variable pour stocker le nom de l'option sélectionnée
model = selected_option.get()  # Initialise `model` avec l'option par défaut

# Fonction pour afficher le choix de l'utilisateur
def afficher_choix():
    global model  # Indique que nous utilisons la variable globale `model`
    print(f"Choix de l'utilisateur : {model}")

# Créer un bouton pour afficher le choix de l'utilisateur
bouton_afficher = tk.Button(fenetre, text="Afficher le choix", command=afficher_choix)
bouton_afficher.pack(pady=20)

# Lancer la boucle principale de l'application
fenetre.mainloop()
 
print(model)

def soumettre_reponse():
    global reponse
    reponse = entry.get()  # Récupérer la réponse de l'utilisateur
    if reponse:
        messagebox.showinfo("Réponse", f"recherhe locale sur : {reponse}")
        root.destroy()  # Fermer la fenêtre après avoir soumis la réponse
    else:
        messagebox.showwarning("Attention", "Sujet a étudier")

# Créer la fenêtre principale
root = tk.Tk()
root.title("sujet à etudier")

# Créer un label pour poser la question
label = tk.Label(root, text="Entrer le sujet à rechercher")
label.pack(pady=10)

# Créer un champ de saisie pour la réponse
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Créer un bouton pour soumettre la réponse
button = tk.Button(root, text="lancer la recherche locale", command=soumettre_reponse)
button.pack(pady=10)

# Variable pour stocker la réponse
reponse = ""

# Lancer la boucle principale de l'application
root.mainloop()

# Afficher la réponse après la fermeture de la fenêtre
print(f"Réponse de l'utilisateur : {reponse}")



url = "http://localhost:11434/api/generate"
payload = {
    "model": model,
    "prompt": "collecte le maximum d'information sur :" + reponse,
    "stream": False
}


file_path = os.path.abspath('/home/v/Bureau/jeu.html')

webbrowser.open('file://' + file_path)


response = requests.post(url, data=json.dumps(payload))

response_data = response.json()

generated_text = response_data.get("response", "")
print("reponse du llm reçue")


print("génération de la fenètre tkinter")
def create_window_with_text(text):
    root = tk.Tk()
    root.title("All Humanity Knowledge")
    root.geometry("1800x500")
    root.configure(bg="#f0f0f0")  # Couleur de fond
    root.attributes('-fullscreen', True)
    frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.SUNKEN)
    frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    label = tk.Label(frame, text=text, font=("Arial", 12), bg="#ffffff", fg="#333333", wraplength=1750, justify=tk.LEFT)
    label.pack(pady=20, padx=20)

    close_button = tk.Button(root, text="Fermer", command=root.destroy, font=("Arial", 10), bg="#ff4c4c", fg="#ffffff")
    close_button.pack(pady=10)

    root.mainloop()

# Exemple de texte généré
custom_text = generated_text
create_window_with_text(custom_text)