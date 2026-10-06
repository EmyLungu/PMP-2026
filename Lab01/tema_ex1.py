import csv
import random

def selecteaza_studenti(cale_fisier, k):
    studenti = []
    
    with open(cale_fisier, mode='r', encoding='utf-8') as f:
        cititor = csv.reader(f)
        for linie in cititor:
            if linie:
                studenti.append(linie[0].strip())
    
    if k > len(studenti):
        raise ValueError(f"Nr cerut ({k}) este mai mare decat nr de studenti disponibili ({len(studenti)}).")
    
    selectati = random.sample(studenti, k)
    return selectati

