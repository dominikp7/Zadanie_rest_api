from flask import Flask, render_template

lista = []


plik_lista = open('lista.txt', "r")
for linia in plik_lista:
    lista.append(linia.strip())
plik_lista.close()


app = Flask(__name__)


@app.route('/')
def main():
    return render_template("menu.html")

@app.route('/dodaj/<slowo>')
def dodaj(slowo):
    lista.append(slowo)
    plik_lista = open('lista.txt', "a")
    plik_lista.write("\n"+slowo)
    plik_lista.close()
    return f"Dodano podane slowo, lista: {lista}"

@app.route('/usun/<slowo>')
def usun(slowo):
    if slowo in lista:
        lista.remove(slowo)
        ilosc = len(lista)
        plik_lista = open('lista.txt', "w")
        for i in range(ilosc):
            plik_lista.write(lista[i-1]+"\n")
        plik_lista.close()
        return f"Usunieto podane slowo, lista: {lista}"
    else:
        return "Nie znaleziono podanego slowa"

@app.route('/sprawdz_ilosc/<slowo>')
def sprawdz_ilosc(slowo):
    if slowo in lista:
        ilosc = lista.count(slowo)
        return f"Ilosc powtorzen slowa \"{slowo}\" wynosi: {ilosc}"
    else:
        return "Nie znaleziono podanego slowa"

@app.route('/unikalne')
def unikalne():
    ilosc = len(lista)
    if ilosc == 0:
        return "Lista jest pusta"
    else:
        uni = []
        for i in range(ilosc):
            if lista.count(lista[i-1]) == 1:
                uni.append(lista[i-1])
        return f"Unikalne słowa to: {uni}"



if __name__ == '__main__':
   app.run(debug=True)

