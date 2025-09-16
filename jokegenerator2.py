import random

# Blagues classées par catégorie
jokes = {
    "PROGRAMMATION": [
        "Pourquoi les développeurs préfèrent le mode sombre ? Parce que la lumière attire les bugs !",
        "Combien de développeurs faut-il pour changer une ampoule ? Aucun, c'est un problème hardware.",
        "Pourquoi les développeurs Java portent des lunettes ? Parce qu'ils ne peuvent pas C# !"
    ],
    "ANIMAUX": [
        "Pourquoi les poules traversent la route ? Pour aller de l'autre côté !",
        "Quel est le comble pour un chat ? De se faire griffer par son propre chaton."
    ]
}

def print_random_joke(category):
    """Print a random joke from the selected category."""
    if category in jokes:
        joke = random.choice(jokes[category])
        print(f"[{category}] 😂 {joke}")
    else:
        print("Catégorie non trouvée !")

if __name__ == "__main__":
    print("Bienvenue au Générateur de Blagues !")
    print_random_joke("PROGRAMMATION")
    print_random_joke("ANIMAUX")