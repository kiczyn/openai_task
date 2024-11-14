import os
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
import requests

response = requests.get("https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt")


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI()

ai=client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "bazując na tresc artykulu, napraw kodowanie znaków w tresci, utwórz odpowiednie tagi html do strukturyzacji tresci artykułu wyróżniając tytuły i akapity. Dodaj odpowiednie klasy i id. Zasugeruj w jakich miejscach artykułu warto umieścić grafiki używając w tym celu tagu <img> z atrybutem src='image_placeholder.jpg'. Zwrócony kod powinien zawierać jedynie zawartość do wtawienia pomiędzy tagami <body> i </body>."},
        {"role": "user", "content": response.text}
    ]
)



Func =open("artykul.html", "w",encoding="utf-8")
Func.write(ai.choices[0].message.content)
Func.close()