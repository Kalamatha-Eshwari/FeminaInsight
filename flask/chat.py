"""import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "I do not understand..."


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)"""

"""import random
import json

# Load intents from the JSON file
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

def get_response(msg):
    # Tokenize the input message
    sentence = msg.lower().strip()
    
    # Initialize response to an empty string
    response = ""
    
    # Loop through intents to find a matching pattern
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in sentence:
                # Randomly select a response from the matched intent
                response = random.choice(intent['responses'])
                break
        if response:
            break
    
    # If no matching pattern found, set a default response
    if not response:
        response = "I'm sorry, I don't understand that."

    return response

if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)"""
import random
import json

# Load intents from the JSON file
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

def get_response(msg):
    # Tokenize the input message
    sentence = msg.lower().strip()
    
    # Initialize response to an empty string
    response = ""
    
    # Set the threshold for the number of matching words
    threshold = 2
    
    # Loop through intents to find a matching pattern
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # Count the number of matching words between user input and pattern
            match_count = sum(1 for word in pattern.split() if word.lower() in sentence.split())
            if intent['tag'] in sentence :  # Check if tag name is present
                # Randomly select a response from the matched intent
                response = random.choice(intent['responses'])
                break
        if response:
            break
    
    # If no matching pattern found, set a default response
    if not response:
        response = "I'm sorry, I don't understand that."

    return response

if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp) 

