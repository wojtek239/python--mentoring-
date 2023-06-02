bird_names = {
    "kos": "Turdus merula",
    "wilga": "Oriolus oriolus",
    "rudzik": "Erithacus rubecula",
    "kukulka": "Cuculus canorus",
    "pleszka": "Phoenicurus phoenicurus",
    "bogatka": "Parus major",
    "drozd": "Turdus philomelos",
    "zieba": "Fringilla coelebs",
    "dzwoniec": "Chloris chloris",
    "szczygiel": "Carduelis carduelis",
    "szpak": "Sturnus vulgaris",
    "kopciuszek": "Phoenicurus ochruros"
}

text = (
    "W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, "
    "po nim rudzik,a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. "
    "Zaraz po niej budzi sie bogatka.Wraz ze wschodem slonca, o czwartej godzinie, "
    "swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga"
    "akcentuje swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze"
    " dodaje szpak, a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie "
    "okazuj sie byc dzwoniec i szczygiel."
)

for pl_name, latin_name in bird_names.items():
    text = text.replace(pl_name, f"{pl_name},({latin_name})")

print(text)


