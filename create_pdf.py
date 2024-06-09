import os
import openai
import PyPDF2
import random
import pinecone


from openai import OpenAI

api_key = 'sk-proj-BCtNALBJdUhNjwA2XKPoT3BlbkFJ14y9f2uLvjfWYGvLCL2r'
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()


def load_pdf(file_name):
    # Read the PDF file
    pdf_file = open(file_name, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text_content = ""
    # Extract text from each page
    for page in range(len(pdf_reader.pages)):
        text_content += pdf_reader.pages[page].extractText()

    pdf_file.close()
 
    return text_content


# Function to chunk text by number of words or characters with a given size and overlap

def chunk_text(text, chunk_size=300, chunk_overlap=100, by='word'):
    if by not in ['word', 'char']:
        raise ValueError("Invalid value for 'by'. Use 'word' or 'char'.")

    chunks = []
    if by == 'word':
        text = text.split()
    elif by == 'char':
        text = text

    current_chunk_start = 0
    while current_chunk_start < len(text):
        current_chunk_end = current_chunk_start + chunk_size
        if by == 'word':
            chunk = " ".join(text[current_chunk_start:current_chunk_end])
        else:
            chunk = text[current_chunk_start:current_chunk_end]

        chunks.append(chunk)
        current_chunk_start += (chunk_size - chunk_overlap)
    print(len(chunks))
    print(chunks[0])
    return chunks
text=load_pdf('state_of_ai_docs.pdf')
chunks=chunk_text(text, by='word')
from pinecone import Pinecone
import pinecone
pc = Pinecone(api_key="7c0c8ae3-71d7-435b-9132-8ed9c7dfb3ff")
index = pc.Index("test")

'''for i in range(len(chunks)):
    vector = client.embeddings.create(
        model="text-embedding-ada-002",
        input=chunks[i])
    vector = vector.data[0].embedding

    upsert_response = index.upsert(
    vectors=[
        (
         str(i),
         vector,
         {"chunk_content": chunks[i]}
        )
    ])'''

user_request = input("Ask some question regarding the document: ")

user_vector = client.embeddings.create(
    model="text-embedding-ada-002",
    input=user_request)

user_vector = user_vector.data[0].embedding

matches = index.query(
    vector=user_vector,
    top_k=19,
    include_metadata=True,
  
  )

#who is Alex Singla
print(matches['matches'][0]['metadata'])
messages = [{"role": "system", "content": """I want you to act as a support agent. Your name is "My Super Assistant". You will provide me with answers from the given info . If the answer is not included, say exactly "Ooops! I don't know that." and stop after that. Refuse to answer any question not about the info. Never break character and always answer on the given text translated to french."""}]
messages.append({"role": "user", "content": matches['matches'][0]['metadata']['chunk_content']})
messages.append({"role": "user", "content": user_request})
print(messages)
chat_response = client.chat.completions.create(
	model="gpt-3.5-turbo",
	messages=messages,
	temperature=0,
	max_tokens=100,
)

messages.append({"role": "assistant", "content": chat_response.choices[0].message.content})
print("Assistant:", chat_response.choices[0].message.content)
print()
#print("Context: ", matches['matches'][0]['metadata']['chunk_content'])
print("$$$$$")