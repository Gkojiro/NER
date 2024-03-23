import spacy

# SpaCy modelini yükle
nlp = spacy.load("en_core_web_sm")

# Metni işleme
def process_text(text):
    # Metni analiz et
    doc = nlp(text)
    
    # Named Entity Recognition (NER)
    entities = {"ORG": [], "DATE": [], "PERSON": [], "NORP": [], "GPE": []}
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    
    return entities

# Örnek metin
text = "Jonathan live in istanbul and he is born 1994"

# Metni işle
result = process_text(text)

# Sonuçları yazdır
print("Organizasyonlar:", result["ORG"])
print("Tarihler:", result["DATE"])
print("Kişiler:", result["PERSON"])
print("Ülkeler/Nesneler:", result["NORP"])
print("Şehirler:", result["GPE"])
