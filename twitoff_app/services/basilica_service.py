# Interacting with basilica

# Imports
from basilica import Connection
import os 
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default='OOPS')

# Establish connection
connection = Connection(BASILICA_API_KEY)
print(type(connection))

# Simple embed to test
embedding = connection.embed_sentance('HELLO WORLD!')
print(embedding)

# List of sentences to convert to numeric values
sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]

# Call Basilica to embed the sentences into numeric values
embeddings = list(connection.embed_sentences(sentences))

# Print the enbedded sentences above
for embed in embeddings:
    print('------')
    print(embed)

