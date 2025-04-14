from textblob import TextBlob

# Abre o arquivo com as sentenças
with open('inputs/frases.txt', 'r', encoding='utf-8') as file:
    frases = file.readlines()

# Analisa cada frase
for frase in frases:
    analise = TextBlob(frase)
    print(f'Frase: {frase.strip()}')
    print(f'Sentimento (polaridade): {analise.sentiment.polarity}')
    print('-' * 50)
