# Pearl Hacks 2019

import boto3
import json
# Imports the Google Cloud client library
from google.cloud import translate

langs = {1:"en", 2:"es", 3:"fr", 4:"tl"}

# Instantiates a client
#translate_client = translate.Client()

#"""Lists all available languages."""
translate_client = translate.Client()

#results = translate_client.get_languages()

#for language in results:
#    print(u'{name} ({language})'.format(**language))

#print(u'Text: {}'.format(text))
#print(u'Translation: {}'.format(translation['translatedText']))

print("Select language:")
print("1) English")
print("2) Spanish")
print("3) French")
print("4) Tagalog")

lang = int(raw_input("Input number of language: "))

# The text to translate
#text = u'Hello, world!'
# The target language
target = langs[lang]

# Translates some text into Russian
#translation = translate_client.translate(
#    text,
#    target_language=target)

name = "Petey"

client = boto3.client('lex-runtime', region_name='us-east-1')

while True:
    input = raw_input(translate_client.translate("Type your message: ", target_language=target)['translatedText'])
    if input == "end":
        break
    input = translate_client.translate(input, target_language="en")['translatedText']
    response = client.post_content(
        botName='HealthHelp',
        botAlias='tiffkwin',
        userId=name,
        #sessionAttributes={...}|[...]|123|123.4|'string'|True|None,
        #requestAttributes={...}|[...]|123|123.4|'string'|True|None,
        contentType='text/plain; charset=utf-8',
        accept='text/plain; charset=utf-8',
        inputStream=str(input)
    )
    #print(response)
    
    if '{' in response['message']:
        divided = (response['message']).split('value')
        divided = divided[1::]
        for msg in divided:
            x = msg.split('"')
            print(translate_client.translate(x[2], target_language=target)['translatedText'])
    else:
        print(response['message'])