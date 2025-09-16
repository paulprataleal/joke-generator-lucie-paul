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
    ],
    "DAD": [
      "— Papa, tu connais l’histoire du lit vertical ? — Non ? — Tant mieux, elle est un peu tirée par les draps !",
      "Pourquoi est-ce que les plongeurs plongent toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau !",
      "— Papa, j’ai faim. — Enchanté, Faim, moi c’est Papa !"
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
    print_random_joke("PROGRAMMATION")  # Affiche une blague de programmation
    print_random_joke("ANIMAUX")       # Affiche une blague d'animaux
    print_random_joke("DAD")