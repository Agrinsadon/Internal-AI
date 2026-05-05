# 🤖 Internal AI Assistant (LangChain + GPT + Tavily + LangSmith)

Tämä projekti on henkilökohtainen AI-agentti, joka on rakennettu LangChainin ja LangGraphin avulla. Se toimii komentorivipohjaisena assistenttina, joka pystyy käyttämään web-hakua, muistia ja GPT-mallia reaaliaikaisessa keskustelussa.

Projektissa käytetään Python 3.12 + uv dependency manager -ympäristöä.

---

## 🚀 Ominaisuudet

- 🧠 GPT-4o-mini -pohjainen AI-agentti  
- 🌐 Web-haku (Tavily Search)  
- 💬 ReAct-agentti (reasoning + työkalut)  
- 💾 Keskustelumuisti (MemorySaver)  
- 🔄 Streamattavat vastaukset terminaaliin  
- 📊 LangSmith tracing (debug & seuranta)  
- 🇫🇮 Suomi + Englanti tuki  

---

## ⚙️ Teknologiat

- Python 3.12+
- uv (package manager)
- LangChain
- LangGraph
- OpenAI API
- Tavily API
- LangSmith

---

## 📦 Asennus

Kloonaa projekti

```bash
git clone https://github.com/agrinsadon/internal-ai.git
cd internal-ai
```

---

Asenna riippuvuudet:

```bash
uv sync
```

---

## 🔑 Ympäristömuuttujat

Luo projektin juureen `.env` tiedosto:

```env
OPENAI_API_KEY=sk-proj-...

TAVILY_API_KEY=tvly-dev...

LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_...

LANGCHAIN_PROJECT=agrinin-agentti
```

---

## ▶️ Käynnistys

```bash
uv run python main.py
```

---

## 💬 Käyttö

- Kirjoita kysymys terminaaliin  
- AI vastaa reaaliajassa  
- Kirjoita `lopeta` lopettaaksesi ohjelman  

Esimerkki:

```text
Sinä: mikä on tekoäly?
AI: Tekoäly on järjestelmä, joka pystyy analysoimaan dataa ja tekemään päätöksiä sen perusteella.
```

---

## 🧠 Agentin ohjeistus

> Olet henkilökohtainen AI assistentti. Olet avulias, ytimekäs ja puhut suomea ja englantia. Ole suorapuheinen äläkä kaunistele vastauksia. Jos et tiedä jotain, sano se rehellisesti.

---

## 🏗️ Arkkitehtuuri

- ChatOpenAI → GPT-malli  
- TavilySearch → web-haku  
- create_react_agent → agenttimoottori  
- MemorySaver → keskustelumuisti  
- LangSmith → seuranta ja debug  
- CLI loop → käyttöliittymä  

---

## 📁 Projektirakenne

```text
internal-ai/
│── main.py
│── .env
│── pyproject.toml
│── README.md
```

---

## 📈 Tulevaisuuden kehitysideat

- Web UI (React / Next.js)
- Pitkäaikainen vector-muisti
- Multi-agent järjestelmä
- FastAPI backend
- Käyttäjäkohtainen personointi

---

## ⚠️ Tärkeää

Älä koskaan jaa `.env` tiedostoa tai API-avaimia julkisesti.

