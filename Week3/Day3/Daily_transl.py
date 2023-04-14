from deep_translator import GoogleTranslator
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
translation=[]
for i in french_words:
    translated_word = GoogleTranslator(source='fr', target='en').translate(i)
    translation.append(translated_word)
print(translation)