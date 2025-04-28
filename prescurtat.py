"""
Cerința
Scrieți funcția cu următorul antet:

def prescurtat(text):
Funcția primește ca parametru un text, alcătuit din cuvinte separate prin câte un spațiu și formate din litere mari ale alfabetului englez, urmate eventual de caracterul . (punct), dacă sunt scrise prescurtat.
Textul reprezintă numele unei instituții de învățământ și doar cuvintele din mulțimea {COLEGIUL, LICEUL, NATIONAL, TEORETIC} pot fi prescurtate, eliminându-se ultimele lor litere.
Funcția va returna tot prin intermediul parametrului `text` numele instituției scris fără prescurtări.

Exemplu
Dacă text memorează inițial COLEG. NAT. DE INFORMATICA, atunci după apelul prescurtat(s), textul va deveni COLEGIUL NATIONAL DE INFORMATICA.

Restricții și precizări
Lungimea inițială a șirului s va fi de cel mult 50, iar la final de cel mult 100.
"""

cuvinte_neprescurtate = ["COLEGIUL", "LICEUL", "NATIONAL", "TEORETIC"]

def prescurtat(text):
    text_neprescurtat = []
    text_prescurtat = text.split(" ")  # "COLEG.", "NAT.", "DE", "INFORMATICA"
    
    for prescurtare in text_prescurtat:
        for cuvant_neprescurtat in cuvinte_neprescurtate:
            if "." in prescurtare:
                if prescurtare[:-1] in cuvant_neprescurtat:
                    text_neprescurtat.append(cuvant_neprescurtat)
            else:
                text_neprescurtat.append(prescurtare)
                break
    
    return " ".join(text_neprescurtat)


print(prescurtat("COLEG. NAT. DE INFORMATICA"))
# COLEGIUL NATIONAL DE INFORMATICA
