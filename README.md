
# 📘 **Trading Journal**

Een geavanceerd Python-gebaseerd trading journal ontworpen om handelsgegevens te analyseren en te visualiseren met concepten geïnspireerd door de **Wyckoff-methode** en **Volume Spread Analysis (VSA)**. Deze applicatie helpt traders hun trades te volgen, marktfases te detecteren en waardevolle inzichten te verkrijgen in hun prestaties.

---

## 🚀 **Features**

✅ **Data Management**  
- Laad handelsgegevens uit CSV-bestanden.  
- Sla bijgewerkte handelsgegevens op met foutafhandeling en logging.  
- Haal historische gegevens op via de Yahoo Finance API (*yfinance*).  

✅ **Wyckoff Phase Detection**  
- Herken handelsfases zoals:  
  - *Accumulation*  
  - *Distribution*  
  - *Markup*  
  - *Markdown*  
- Gebruik van voortschrijdende gemiddelden en prijsactie.

✅ **Volume Spread Analysis (VSA)**  
- Bereken prijsspreads voor elke trade.  
- Detecteer belangrijke VSA-signalen zoals:  
  - "High Volume Wide Spread"  
  - "Low Volume Narrow Spread"  

✅ **Visualisatie**  
- Plot instap- en uitstapprijzen met:  
  - Annotaties voor Wyckoff-fases.  
  - VSA-signalen direct zichtbaar op de grafiek.  
  - Dynamische en interactieve visualisaties.  

✅ **Modulair Ontwerp**  
- Gestructureerde en overzichtelijke codebase:  
  - **`app.py`**: Hoofdapplicatie.  
  - **`data_manager.py`**: Data-inladen, opslaan en ophalen.  
  - **`phases.py`**: Wyckoff-fase detectie.  
  - **`vsa.py`**: Volume Spread Analysis-logica.  
  - **`visualizations.py`**: Plotten en visualiseren.

---

## 🗂 **Folder Structure**

```plaintext
trading-journal/
├── README.md                # Projectdocumentatie
├── app.py                   # Hoofdapplicatie
├── data/                    # Lokale opslag van data
│   └── example_trades.csv   # Voorbeeld-handelsbestand
├── tools/                   # Kernlogica en utilities
│   ├── __init__.py          # Initieert de module
│   ├── data_manager.py      # Data management
│   ├── phases.py            # Wyckoff-fase detectie
│   ├── vsa.py               # VSA-logica
│   └── visualizations.py    # Visualisaties
├── tests/                   # Unit tests
│   ├── test_data_manager.py
│   ├── test_phases.py
│   ├── test_vsa.py
│   └── test_visualizations.py
├── notebooks/               # Optionele Jupyter-notebooks
└── docs/                    # Documentatie en gidsen
```

---

## 🛠 **Installatie**

1. **Clone de repository**  
   ```bash
   git clone https://github.com/YourUsername/trading-journal.git
   cd trading-journal
   ```

2. **Installeer vereisten**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests**  
   ```bash
   pytest ./tests/
   ```

---

## ⚙️ **Hoe te gebruiken**

1. **Omgeving instellen**  
   Installeer de vereisten zoals hierboven beschreven.

2. **Applicatie uitvoeren**  
   Start de app met:  
   ```bash
   python app.py
   ```

3. **Data aanleveren**  
   Plaats je handelsdata-CSV in de `/data` map.  
   Zorg ervoor dat deze het juiste formaat heeft (zie voorbeeld hieronder).

4. **Resultaten bekijken**  
   Verwerkte data en visualisaties worden opgeslagen in de outputmap.

---

## 📊 **Sample CSV Structure**

| Date       | Asset   | High  | Low   | Entry Price | Exit Price | Volume  | Phase     |
|------------|---------|-------|-------|-------------|------------|---------|-----------|
| 2023-01-01 | EUR/USD | 1.25  | 1.20  | 1.2000      | 1.2500     | 100000  | Undefined |
| 2023-01-02 | EUR/USD | 1.26  | 1.25  | 1.2500      | 1.2600     | 120000  | Undefined |
| 2023-01-03 | EUR/USD | 1.24  | 1.23  | 1.2400      | 1.2300     | 130000  | Undefined |

---

## 📈 **Voorbeeld Workflow**

1. **Data laden**  
   Laadt handelsdata vanuit `/data/example_trades.csv`.

2. **Data analyseren**  
   - Detecteert Wyckoff-fases (bijvoorbeeld *Accumulation*, *Markup*).  
   - Herkent VSA-signalen (bijvoorbeeld *High Volume Wide Spread*).

3. **Data visualiseren**  
   Genereert een grafiek met:  
   - Instap- en uitstapprijzen.  
   - Annotaties van fases.  
   - VSA-signalen.

---

## 🛣️ **Roadmap**

### **Fase 1: Fundament**  
✅ CSV-data laden en beheren  
✅ Wyckoff-analyse uitvoeren  
✅ Resultaten visualiseren  

### **Fase 2: Geavanceerde Analyse**  
⬜ Volume Spread Analysis (VSA) uitbreiden  
⬜ Interactiviteit in visualisaties verbeteren  

### **Fase 3: Real-Time Data**  
⬜ API-integratie voor live marktdata  
⬜ AI-gestuurde handel inzichten bieden  

---

## 📸 **Screenshots**

Binnenkort beschikbaar! Houd deze sectie in de gaten voor visuele voorbeelden van de mogelijkheden.

---

## 🤝 **Bijdragen**

Wij verwelkomen bijdragen!  

1. Fork de repository.  
2. Maak een nieuwe branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Commit je wijzigingen:  
   ```bash
   git commit -m "Nieuwe functie toegevoegd"
   ```
4. Push naar de branch:  
   ```bash
   git push origin feature-name
   ```
5. Open een Pull Request.

---

## 📝 **Licentie**

Dit project is gelicentieerd onder de MIT License. Gebruik en wijzig het zoals je wilt!

---

📬 **Contact**

Heb je vragen of suggesties? Neem gerust contact op via **goliathnm@gmail.com**.

---

Veel succes met het verkennen en verbeteren van het Trading Journal! 🚀
