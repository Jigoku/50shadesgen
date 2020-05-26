#!/usr/bin/env python3
import random
import json
import re

with open('sentences', 'r') as rfile:
  sentences=rfile.readlines()

with open('vocabulary.json', 'r') as rfile:
  vocabulary=json.load(rfile)

def parse_sentence(sentence):
  for token in re.findall("\[(.*?)\]", sentence):
    parts = token.split("-")
    type = parts[1]

    if parts[0] == "verb":
      items = list(vocabulary["verbs"][type])

      if parts[2] == "root":
        sentence = re.sub("(\[" + token + "\])", random.choice(items)[0], sentence,1)
        continue
      elif parts[2] == "past":
        sentence = re.sub("(\[" + token + "\])", random.choice(items)[1], sentence,1)
        continue
      elif parts[2] == "present":
        sentence = re.sub("(\[" + token + "\])", random.choice(items)[2], sentence,1)
        continue

    if parts[0] == "noun":
      items = list(vocabulary["nouns"][type])

      sentence = re.sub("(\[" + token + "\])", random.choice(items), sentence,1)
      continue
    elif parts[0] == "simile":
      items = list(vocabulary["similes"][type])
      sentence = re.sub("(\[" + token + "\])", random.choice(items), sentence, 1)
      continue

  return sentence

def generate(num):
  output = ""
  for i in range(num):
    sentence = random.choice(sentences)
    output = output + " " + (parse_sentence(sentence.rstrip()))

  return output


print (generate(5))



