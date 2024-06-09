import openai
import requests
import time
import os
import openai

from openai import OpenAI

dataset="""

segement1: 'C'est quelque chose de bête tabarnac, je m'en fiche, je vais faire ce que je veux tabarnac.'
segment2: 'Je ne sais pas comment je dois faire dans cette vie tabarnac, c'est une perte de temps tabarnac.'
segment3: 'Je suis dégoûté et je ne veux pas faire cette mission tabarnac.'

"""

api_key = 'sk-proj-BCtNALBJdUhNjwA2XKPoT3BlbkFJ14y9f2uLvjfWYGvLCL2r'
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()

messages = [{"role": "system", "content": """Je veux créer un roman dans le style d'un écrivain. Je fournirai le style de l'écrivain dans le dataset avec quelques segments. La création du roman se fera partie par partie, donc je vous donnerai une idée et vous enrichirez le texte selon le style des segments
si je commence l'ecriture avec @enr-"text" donc il faux enrichire le text si je ecris @idee donc il faux vous proposer des idee et scenario selon les action precedent
si je ecris @cont-1 donc il faux continuer le histoire selon votre idee 1 et lorsque je dicouvrire un faute on supprime les message precedent et le remplace avec le message
@sup-"text" dans toute vous expression assayer de utiliser le style des segement1 et segement2 et segement3 le resume de remon c est sami trouver un telephone de le president de grande pouvoir au monde ce president vivre une vie simple il a cacher derire sa pauvrité """}]
messages.append({"role": "assistant", "content": dataset})
while True:
    user_input = input("You: ")
    if user_input == "quit":
        break

    messages.append({"role": "user", "content": user_input})
    chat_response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        temperature=0.0,
        max_tokens=300,
    )
    messages.append({"role": "assistant", "content": chat_response.choices[0].message.content})
    print("Assistant:", chat_response.choices[0].message.content)