import random

# Initial joke collection
programming_jokes = [
    "Pourquoi les développeurs préfèrent le mode sombre ? Parce que la lumière attire les bugs !",
    "Combien de développeurs faut-il pour changer une ampoule ? Aucun, c'est un problème hardware.",
    "Pourquoi les développeurs Java portent des lunettes ? Parce qu'ils ne peuvent pas C# !"
]

dad_jokes = [
    "— Papa, tu connais l’histoire du lit vertical ? — Non ? — Tant mieux, elle est un peu tirée par les draps !",
    "Pourquoi est-ce que les plongeurs plongent toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau !",
    "— Papa, j’ai faim. — Enchanté, Faim, moi c’est Papa !"
]

def print_random_joke():
    """Print a random joke from the collection."""
    joke_type = random.choice([programming_jokes, dad_jokes])
    joke = random.choice(joke_type)
    print(f"😂 {joke}")

if __name__ == "__main__":
    print("Bienvenue au Générateur de Blagues !")
    print_random_joke()
