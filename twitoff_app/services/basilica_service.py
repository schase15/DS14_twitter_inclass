# Interacting with basilica

from basilica import Connection
import os 
from dotenv import load_dotenv

load_dotenv()



# TODO save key in .env file
BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default='OOPS')

connection = Connection(BASILICA_API_KEY)
print(type(connection))

# List of sentences to convert to numeric values
sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]

# Call Basilica to embed the sentences into numeric values
embeddings = list(connection.embed_sentences(sentences))

# Print the enbedded sentances above
for embedding in embeddings:
    print('------')
    print(embedding)

embedding = connection.embed_sentence('Hello World')

