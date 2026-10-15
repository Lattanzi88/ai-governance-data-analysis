import pandas as pd

import matplotlib.pyplot as plt

# ==========================================
# 1. CREAZIONE DEL DATASET
# ==========================================

dati = {
    "candidato": ["Anna", "Marco", "Sara", "Luca", "Giulia", "Paolo"],
    "esperienza": [3, 5, 2, 7, 4, 6],
    "selezionato": [1, 0, 1, 1, 1, 0],
    "genere": ["F","M","F","M","F","M"],
    "titolo_studio": ["laurea","diploma","diploma","laurea","laurea","laurea"],
}

df = pd.DataFrame(dati)

numero_candidati = len(df)

if numero_candidati < 30:
    print("ATTENZIONE: dataset molto piccolo.")
    print("I risultati sono soltanto esplorativi.")
else:
    print("Dataset sufficientemente ampio per proseguire l'analisi.")

conteggio_genere = df["genere"].value_counts()

print("\n--- CANDIDATI PER GENERE ---")
print(conteggio_genere)


selezionati_per_genere = (df[df["selezionato"] == 1]["genere"].value_counts())

print("\n--- SELEZIONATI PER GENERE ---")
print(selezionati_per_genere)


# ==========================================
# 2. PREPARAZIONE E ANALISI DEI DATI
# ==========================================

candidati_selezionati = df[df["selezionato"] == 1]

candidati_non_selezionati = df[df["selezionato"] == 0]

# --- Analisi per esperienza ---

meno_esperienza = df[df["esperienza"] <= 4]

esperti = df[df["esperienza"] > 4]

meno_esperienza_selezionati = meno_esperienza[meno_esperienza["selezionato"] == 1]

esperti_selezionati = esperti[esperti["selezionato"] == 1]

# --- Analisi per genere ---

genere_femmine = df[df["genere"] == "F"]

genere_femmine_selezionate = df[(df["genere"] == "F") & (df["selezionato"] == 1)]

genere_maschio = df[df["genere"] == "M"]

genere_maschio_selezionati = df[(df["genere"] == "M") & (df["selezionato"] == 1)]

# --- Analisi per titolo di studio ---

laureati = df[df["titolo_studio"] == "laurea"]

laureati_selezionati = df[(df["titolo_studio"] == "laurea") & (df["selezionato"] == 1)]

diplomati = df[df["titolo_studio"] == "diploma"]

diplomati_selezionati = df[(df["titolo_studio"] == "diploma") & (df["selezionato"] == 1)]


# --- Selezione complessiva ---

percentuale_candidati_selezionati = (df["selezionato"].sum()/len(df["candidato"]))*100

percentuale_candidati_non_selezionati = (len(candidati_non_selezionati)/len(df["candidato"]))*100


# --- Tassi per esperienza ---

percentuale_esperti_selezionati = (len(esperti_selezionati)/len(esperti))*100

percentuale_meno_esperienza_selezionati = (len(meno_esperienza_selezionati)/len(meno_esperienza))*100


# --- Tassi per genere ---

percentuale_selezione_femmine = (len(genere_femmine_selezionate)/ len(genere_femmine))*100

percentuale_selezione_maschi = (len(genere_maschio_selezionati)/ len(genere_maschio))*100

differenza_selezione_genere = abs(percentuale_selezione_femmine - percentuale_selezione_maschi)

tasso_minimo = min(percentuale_selezione_femmine,percentuale_selezione_maschi)

tasso_massimo = max(percentuale_selezione_femmine,percentuale_selezione_maschi)

if tasso_massimo == 0:
    selection_rate_ratio_genere = None
else:
    selection_rate_ratio_genere = tasso_minimo / tasso_massimo


if selection_rate_ratio_genere is None:
    interpretazione_ratio = "Rapporto non definibile"
elif selection_rate_ratio_genere < 0.8:
    interpretazione_ratio = "Differenza da approfondire"
else:
    interpretazione_ratio = "Rapporto pari o superiore a 0.8"

# --- Tassi per titolo di studio ---

percentuale_selezione_laureati = (len(laureati_selezionati)/ len(laureati))*100

percentuale_selezione_diplomati = (len(diplomati_selezionati) / len(diplomati)) * 100

differenza_titolo_studio = abs(percentuale_selezione_laureati - percentuale_selezione_diplomati)


# ==========================================
# 3. RIEPILOGO DEGLI INDICATORI
# ==========================================

riepilogo = {
    "selezione_complessiva": {
        "tasso_selezionati": percentuale_candidati_selezionati,
        "tasso_non_selezionati": percentuale_candidati_non_selezionati,
    },

    "esperienza": {
        "tasso_selezione_esperti": percentuale_esperti_selezionati,
        "tasso_selezione_meno_esperienza": percentuale_meno_esperienza_selezionati,

    },

    "genere": {
        "tasso_maschi": percentuale_selezione_maschi,
        "tasso_femmine": percentuale_selezione_femmine,
        "differenza_genere": differenza_selezione_genere,
        "selection_rate_ratio": selection_rate_ratio_genere,
        "interpretazione_ratio": interpretazione_ratio,
    },

    "titolo_studio": {
        "tasso_laureati": percentuale_selezione_laureati,
        "tasso_diplomati": percentuale_selezione_diplomati,
        "differenza_titolo_studio": differenza_titolo_studio,
    }

}


# ==========================================
# 4. STAMPA DEI RISULTATI
# ==========================================

for categoria, indicatori in riepilogo.items():
    print(f"\n--- {categoria.upper()} ---")

    for nome, valore in indicatori.items():
        if valore is None:
            print(f"{nome}: non definito")
        elif isinstance(valore, str):
            print(f"{nome}: {valore}")
        elif "differenza" in nome:
            print(f"{nome}: {valore:.2f} punti percentuali")
        elif "ratio" in nome:
            print(f"{nome}: {valore:.2f}")
        else:
            print(f"{nome}: {valore:.2f}%")
    
print("\n--- NOTA METODOLOGICA ---")
print("Il Selection Rate Ratio è un indicatore descrittivo.")
print("Un valore basso segnala una disparità da approfondire,")
print("ma non dimostra da solo una discriminazione.")
print("I risultati dipendono dalla dimensione e dalla qualità del dataset.")

# ==========================================
# 5. VISUALIZZAZIONE DEI RISULTATI
# ==========================================

gruppi = ["Esperienza <= 4 anni", "Esperienza > 4 anni"]

percentuali = [
    percentuale_meno_esperienza_selezionati,
    percentuale_esperti_selezionati
]

barre = plt.bar(gruppi, percentuali)

plt.bar_label(barre, fmt="%.1f%%")

plt.title("Tasso di selezione per esperienza")

plt.ylabel("Tasso di selezione (%)")

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.savefig("grafici/grafico_esperienza.png")

plt.show()

gruppi_genere = ["Maschi", "Femmine"]

tassi_genere = [
    percentuale_selezione_maschi,
    percentuale_selezione_femmine
]

barre_genere = plt.bar(gruppi_genere, tassi_genere)

plt.title("Tasso di selezione per genere")

plt.xlabel("Genere")

plt.ylabel("Tasso di selezione (%)")

plt.bar_label(barre_genere, fmt="%.2f%%")

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.savefig("grafici/grafico_genere.png")

plt.show()

gruppi_studio = ["Laureati", "Diplomati"]

tassi_studio = [
    percentuale_selezione_laureati,
    percentuale_selezione_diplomati
]

barre_tassi_studio = plt.bar(gruppi_studio, tassi_studio)

plt.title("Tasso di selezione per titolo di studio")

plt.xlabel("Titolo di studio")

plt.ylabel("Tasso di selezione (%)")

plt.bar_label(barre_tassi_studio, fmt="%.2f%%")

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.savefig("grafici/grafico_titolo_studio.png")

plt.show()