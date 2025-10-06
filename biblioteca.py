def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    biblioteca={}
    try:

        with open(file_path,'r',encoding='utf-8') as openfile:
            maxsezione = int(openfile.readline().rstrip())
            for line in openfile:
                riga=line.rstrip().split(',')
                titolo=riga[0]
                autore=riga[1]
                anno=int(riga[2])
                pagina=int(riga[3])
                sezione=int(riga[4])
                biblioteca[titolo]={'author':autore,'year':anno,'pages':pagina,'section':sezione}

        return biblioteca, maxsezione

    except FileNotFoundError:
        return None









def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path, maxsezione):
    """Aggiunge un libro nella biblioteca"""
    # TODO



    if titolo in biblioteca or sezione>maxsezione:
        return None

    else:
        biblioteca[titolo]={[autore,anno,pagine,sezione]}
        with open(file_path, 'a') as outfile:
            outfile.write(f'{titolo},{autore},{anno},{pagine},{sezione}\n')
            return biblioteca


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    risultato = ''
    title=titolo
    for key, dati in biblioteca.items():
        if key == title:
            autore = dati['author']
            anno=dati['year']
            pagine = dati['pages']
            sezione = dati['section']
            risultato = titolo+ ', '+autore+', '+ ', '+str(anno)+', '+str(pagine)+', '+str(sezione)
            return risultato

    return None




def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO

    libri_sezione=[]

    for key,dati in biblioteca.items():
        numero=dati['section']
        if numero==sezione:
            libri_sezione.append(key)

        libri_sezione.sort()

    if len(libri_sezione)==0:
        return None
    else:
        return libri_sezione





def main():
    biblioteca ={}
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca,maxsezione= carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            biblioteca = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione,file_path,maxsezione)
            if biblioteca:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

