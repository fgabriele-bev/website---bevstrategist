"""Builds the bilingual pages of bevstrategist.co.uk from one template per page.

Italian is the default language at the site root; English lives under /en/.
Run from the repository root:  python3 _build/build.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://bevstrategist.co.uk"

T = {
    "it": {
        "lang": "it", "home": "/", "other_home": "/en/",
        "title": "Francesco Gabriele | Beverage Strategist",
        "desc": "Strategia di ingresso nel mercato britannico per cantine italiane boutique. Un parere indipendente, dal lato di chi compra.",
        "nav_how": "Come lavoriamo", "how_url": "/come-lavoriamo.html",
        "nav_about": "Chi sono", "about_id": "chi-sono",
        "linkedin": "Il mio profilo su LinkedIn",
        "nav_contact": "Contatti", "contact_id": "contatti",
        "logo_alt": "Francesco Gabriele | Beverage Strategist, torna alla home",
        "h1": ["Il mercato britannico", "visto dal lato", "di chi compra"],
        "sub": "Per le cantine italiane boutique che cercano una presenza solida&nbsp;e&nbsp;strategica nel canale Horeca del Regno Unito.",
        "cta": "Come lavoriamo",
        "photo_alt": "Francesco Gabriele in una cantina di vini",
        "statement": ["Oltre tre decenni dal lato di chi compra.", "Oggi al fianco di chi produce."],
        "about": [
            "Ho lavorato oltre tre decenni nell’ospitalità di lusso, di cui gli ultimi 14 anni in uno dei gruppi alberghieri più iconici del Regno Unito, dove ho guidato vino e bevande per l’intero gruppo. Ho valutato produttori, scelto distributori, costruito carte dei vini e formato le squadre di sala.",
            "In quel ruolo la domanda era sempre la stessa: perché questo vino merita un posto in carta? La risposta dipendeva dalla storia del produttore, dalla fiducia con cui la sala lo avrebbe proposto e dal senso commerciale per quell’hotel in quel momento.",
            "Da lì nasce il mio metodo. So come decide un buyer britannico e dove un buon vino si ferma prima di arrivare in carta. Lo metto al servizio di poche cantine italiane, scelte con cura.",
        ],
        "contact_lead": ["Si comincia con una conversazione gratuita", "per capire la tua situazione e se posso esserti utile."],
        "form": {"first": "Nome", "last": "Cognome", "winery": "Cantina", "email": "Email", "msg": "Messaggio",
                 "privacy": "Ho letto la", "send": "Invia messaggio", "or": "Oppure scrivimi o chiamami",
                 "lang_name": "Italiano", "subject": "Nuovo messaggio dal sito",
                 "ok": "Grazie, il tuo messaggio è arrivato. Ti rispondo di persona.",
                 "fail": "L’invio non è riuscito. Scrivimi a fgabriele@bevstrategist.co.uk."},
        "rec_label": "Ti riconosci?",
        "rec": [
            "Hai scritto a importatori britannici e le risposte sono rimaste in sospeso.",
            "In fiera l’interesse c’era, poi è mancato il seguito.",
            "Hai incontrato distributori senza arrivare a una presenza continuativa.",
            "Ti è difficile spiegare perché il tuo vino dovrebbe entrare in un portafoglio britannico.",
        ],
        "privacy": "Privacy Policy", "privacy_url": "/privacy-policy.html",
    },
    "en": {
        "lang": "en", "home": "/en/", "other_home": "/",
        "title": "Francesco Gabriele | Beverage Strategist",
        "desc": "UK market entry strategy for Italian boutique wine producers. Independent advice from the buyer’s side of the table.",
        "nav_how": "How we work", "how_url": "/en/how-we-work.html",
        "nav_about": "About", "about_id": "about",
        "linkedin": "My profile on LinkedIn",
        "nav_contact": "Contact", "contact_id": "contact",
        "logo_alt": "Francesco Gabriele | Beverage Strategist, back to home",
        "h1": ["Beverage strategy built", "from the inside out"],
        "sub": "For Italian boutique wine producers seeking a solid, strategic presence in the UK on-trade.",
        "cta": "How we work",
        "photo_alt": "Francesco Gabriele in a wine cellar",
        "statement": ["Over three decades on the buyer’s side.", "Now working alongside producers."],
        "about": [
            "I spent over three decades in luxury hospitality, the last 14 years with one of the UK’s most iconic hotel groups, where I led wine and beverages across the group. I assessed producers, chose distributors, built wine lists and trained the floor teams.",
            "In that role the question was always the same: why does this wine deserve a place on the list? The answer depended on the producer’s story, on how confidently the team would recommend it and on the commercial sense for that hotel at that moment.",
            "That is where my method comes from. I know how a UK buyer decides and where a good wine stops before it reaches the list. I put that to work for a small number of Italian wineries, chosen with care.",
        ],
        "contact_lead": ["It starts with a conversation, free of charge,", "to understand your situation and whether I can be useful."],
        "form": {"first": "First name", "last": "Last name", "winery": "Winery", "email": "Email", "msg": "Message",
                 "privacy": "I have read the", "send": "Send message", "or": "Or email or call me",
                 "lang_name": "English", "subject": "New message from the website",
                 "ok": "Thank you, your message has arrived. I will reply personally.",
                 "fail": "The message could not be sent. Please email fgabriele@bevstrategist.co.uk."},
        "rec_label": "Does this sound familiar?",
        "rec": [
            "You wrote to UK importers and the replies are still pending.",
            "At the fair the interest was there, then the follow-up went missing.",
            "You met distributors without reaching a lasting presence.",
            "You find it hard to explain why your wine belongs in a UK portfolio.",
        ],
        "privacy": "Privacy Policy", "privacy_url": "/en/privacy-policy.html",
    },
}

FORM_ENDPOINT = "https://formspree.io/f/xrpeqwgr"

LINKEDIN = "https://www.linkedin.com/in/francesco-gabriele-b3495321"
LEGAL = ("FG Beverage Strategy Ltd · Registered in England and Wales No. 17307517<br>"
         "Registered Office: 27 Charles Knott Gardens, Southampton, England, SO15 2TF")


def head(t, path_it, path_en, title=None, desc=None):
    title = title or t["title"]
    desc = desc or t["desc"]
    self_url = SITE + (path_it if t["lang"] == "it" else path_en)
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{self_url}">
<link rel="alternate" hreflang="it" href="{SITE}{path_it}">
<link rel="alternate" hreflang="en" href="{SITE}{path_en}">
<link rel="alternate" hreflang="x-default" href="{SITE}{path_it}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Francesco Gabriele | Beverage Strategist">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{self_url}">
<meta property="og:locale" content="{'it_IT' if t['lang'] == 'it' else 'en_GB'}">
<meta property="og:locale:alternate" content="{'en_GB' if t['lang'] == 'it' else 'it_IT'}">
<meta property="og:image" content="{SITE}/assets/img/anteprima-social.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Francesco Gabriele | Beverage Strategist">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="96x96" href="/assets/img/favicon-96.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/cormorant-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/lato-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
"""


def header(t, path_it, path_en):
    it_cur = ' aria-current="true"' if t["lang"] == "it" else ""
    en_cur = ' aria-current="true"' if t["lang"] == "en" else ""
    return f"""<header class="site-header">
  <a class="site-logo" href="{t['home']}"><img src="/assets/img/logo-francesco-gabriele.png" width="990" height="255" alt="{t['logo_alt']}"></a>
  <nav aria-label="{'Menu principale' if t['lang'] == 'it' else 'Main menu'}">
    <ul class="site-nav">
      <li><a href="{t['how_url']}">{t['nav_how']}</a></li>
      <li><a href="{t['home']}#{t['about_id']}">{t['nav_about']}</a></li>
      <li><a class="nav-contact" href="{t['home']}#{t['contact_id']}"><img src="/assets/img/francesco-gabriele-ritratto.jpg" width="192" height="192" alt=""><span>{t['nav_contact']}</span></a></li>
      <li class="lang"><a href="{path_it}" lang="it" hreflang="it"{it_cur}>IT</a><span aria-hidden="true">|</span><a href="{path_en}" lang="en" hreflang="en"{en_cur}>EN</a></li>
    </ul>
  </nav>
</header>
"""


def footer(t):
    return f"""<footer class="site-footer">
  <p class="legal">{LEGAL}</p>
  <p><a href="{t['privacy_url']}">{t['privacy']}</a> <span class="sep">·</span> <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></p>
</footer>
<script src="/assets/js/form.js" defer></script>
</body>
</html>
"""


def lines(parts):
    return " ".join(f'<span class="line">{p}</span>' for p in parts)


def contact_block(t):
    f = t["form"]
    return f"""  <section class="contact" id="{t['contact_id']}">
    <div class="inner">
      <div class="contact-head">
        <img src="/assets/img/francesco-gabriele-ritratto.jpg" width="192" height="192" alt="Francesco Gabriele">
        <h2 class="label">{t['nav_contact']}</h2>
      </div>
      <span class="rule"></span>
      <p class="lead">{lines(t['contact_lead'])}</p>
      <form class="contact-form" method="post" action="{FORM_ENDPOINT}" data-ok="{f['ok']}" data-fail="{f['fail']}">
        <input type="hidden" name="_subject" value="{f['subject']}">
        <input type="hidden" name="lingua" value="{f['lang_name']}">
        <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
        <label><span>{f['first']}</span><input type="text" name="nome" autocomplete="given-name" required></label>
        <label><span>{f['last']}</span><input type="text" name="cognome" autocomplete="family-name" required></label>
        <label><span>{f['winery']}</span><input type="text" name="cantina" autocomplete="organization" required></label>
        <label><span>{f['email']}</span><input type="email" name="email" autocomplete="email" required></label>
        <label class="wide"><span>{f['msg']}</span><textarea name="messaggio" rows="5" required></textarea></label>
        <label class="check wide"><input type="checkbox" name="privacy" required><span>{f['privacy']} <a href="{t['privacy_url']}">{t['privacy']}</a></span></label>
        <div class="wide"><button class="btn" type="submit">{f['send']}</button></div>
        <p class="form-status wide" role="status" aria-live="polite"></p>
      </form>
      <p class="contact-or">{f['or']}</p>
      <div class="contact-links">
        <a href="mailto:fgabriele@bevstrategist.co.uk">fgabriele@bevstrategist.co.uk</a>
        <a href="tel:+447561514822">+44 7561 514822</a>
      </div>
    </div>
  </section>
"""


HOW = {
    "it": {
        "path": "/come-lavoriamo.html", "other": "/en/how-we-work.html",
        "title": "Come lavoriamo | Francesco Gabriele | Beverage Strategist",
        "desc": "Il percorso di FG Beverage Strategy con le cantine italiane boutique: dal primo contatto alla firma, poi 90 giorni di progetto e supporto continuativo.",
        "h1": ["Un percorso", "passo per passo"],
        "sub": "A costo zero per te fino alla firma: capisco, verifico, ti spiego, preparo un programma e tu decidi.",
        "before_label": "Prima della firma",
        "steps": [
            ("Primo contatto", "Una conversazione gratuita per capire la tua situazione e se posso esserti utile."),
            ("Questionario", "Un piccolo questionario per te mi darà i primi elementi per capire la tua azienda, i tuoi vini e i tuoi obiettivi."),
            ("Prima lettura di mercato", "Ricevi un’analisi introduttiva di circa quattro pagine, costruita sulle tue risposte: primi punti di forza e prime domande aperte."),
            ("Videochiamata", "Un incontro per ascoltarti, chiarire i punti aperti e raccogliere le informazioni mancanti."),
            ("Proposta", "Ricevi la proposta di lavoro con le tariffe e una copia del contratto, in inglese e in italiano, da leggere prima di decidere."),
            ("Firma", "Comunichi i dati societari, preparo il contratto definitivo e, una volta firmato, iniziamo a esplorare il tuo mercato britannico direttamente sul campo."),
        ],
        "after_label": "Dopo la firma",
        "phases": [
            ("Fase 1", "Progetto iniziale", "90 giorni", [
                "Il primo mese circa è dedicato all’analisi: i tuoi dati e la tua preparazione commerciale, il mercato e i concorrenti, il prezzo lungo tutta la filiera, il canale più coerente.",
                "Il risultato è il rapporto strategico, che approvi prima di qualunque contatto esterno.",
                "Nei sessanta giorni successivi ti presento a una prima lista di tre o quattro potenziali partner, quando esistono candidati adatti, e coordino incontri, degustazioni e campioni. Si chiude con una raccomandazione finale: priorità, rischi e azioni correttive.",
            ]),
            ("Fase 2", "Supporto costante e continuativo", "Conferimento di incarico per il primo anno", [
                "Mantengo il dialogo con i partner nominati, seguo l’avanzamento rispetto alla strategia, aggiorno le ricerche di mercato e ti affianco in incontri, degustazioni e visite.",
            ]),
        ],
        "for_label": "A chi mi rivolgo",
        "for": [
            "Cantine italiane boutique o a conduzione familiare, con un’identità riconoscibile e una qualità credibile.",
            "Aziende assenti dal Regno Unito, oppure presenti in modo frammentario.",
            "Produttori che vogliono capire il mercato prima di investire in fiere, campionature, trasferte o accordi distributivi.",
        ],
        "need_label": "Cosa serve da parte tua",
        "need": [
            "Dati completi e aggiornati su vini, prezzi ex-cantina, disponibilità e capacità produttiva.",
            "La disponibilità a discutere apertamente le criticità del portafoglio.",
            "Risorse minime per campioni, materiali e, quando serve, trasferte.",
            "Tempi di risposta coerenti con quelli del trade britannico.",
        ],
        "roles_label": "Chi fa cosa",
        "roles_head": ("Attività", "Io", "Tu"),
        "roles": [
            ("Analisi, posizionamento, prezzi", "Analizzo e raccomando", "Decidi"),
            ("Scelta dei partner", "Ricerco e propongo una lista ragionata", "Scegli chi incontrare"),
            ("Primo contatto con gli operatori", "Ti presento dichiarando il mio ruolo", "Autorizzi ogni contatto"),
            ("Prezzi, esclusiva, ordini, contratti", "Ti consiglio", "Negozi e firmi"),
            ("Licenze, accise, etichettatura, importazione", "Segnalo i temi e ti indirizzo agli specialisti", "A te la decisione"),
        ],
        "on_request": ("Su richiesta", "Progetto a ore", [
            "Anche per poche ore, per un mese o per un singolo progetto: decidi tu quando e quante ore vuoi che dedichi al tuo progetto nel mercato britannico.",
            "Ricevi un preventivo costruito sulle tue richieste.",
        ]),
    },
    "en": {
        "path": "/en/how-we-work.html", "other": "/come-lavoriamo.html",
        "title": "How we work | Francesco Gabriele | Beverage Strategist",
        "desc": "How FG Beverage Strategy works with Italian boutique wine producers: from first contact to signature, then a 90-day project and ongoing support.",
        "h1": ["A path", "step by step"],
        "sub": "At no cost to you until signature: I understand, I verify, I explain, I prepare a programme and you decide.",
        "before_label": "Before signature",
        "steps": [
            ("First contact", "A conversation, free of charge, to understand your situation and whether I can be useful."),
            ("Questionnaire", "A short questionnaire for you gives me the first elements to understand your business, your wines and your goals."),
            ("First market reading", "You receive an introductory analysis of about four pages, built on your answers: first strengths and first open questions."),
            ("Video call", "A meeting to listen to you, clarify the open points and gather missing information."),
            ("Proposal", "You receive the working proposal with fees and a copy of the contract, in English and Italian, to read before deciding."),
            ("Signature", "You send your company details, I prepare the final contract and, once it is signed, we start exploring your UK market directly on the ground."),
        ],
        "after_label": "After signature",
        "phases": [
            ("Phase 1", "Initial project", "90 days", [
                "Roughly the first month is given to analysis: your information and commercial readiness, the market and competitors, the price along the whole supply chain, the most coherent channel.",
                "The outcome is the strategy report, which you approve before any external contact.",
                "In the following sixty days I introduce you to a first list of three or four potential partners, where suitable candidates exist, and coordinate meetings, tastings and samples. It closes with a final recommendation: priorities, risks and corrective actions.",
            ]),
            ("Phase 2", "Ongoing support", "Engagement for the first year", [
                "I keep up the dialogue with the appointed partners, monitor progress against the strategy, refresh market research and support you at meetings, tastings and visits.",
            ]),
        ],
        "for_label": "Who I work with",
        "for": [
            "Boutique or family-run Italian producers with a recognisable identity and credible quality.",
            "Wineries absent from the UK, or present in a fragmented way.",
            "Producers who want to understand the market before investing in trade fairs, samples, travel or distribution agreements.",
        ],
        "need_label": "What is needed from you",
        "need": [
            "Complete, up-to-date information on wines, ex-cellar prices, availability and production capacity.",
            "Willingness to discuss the portfolio’s weak points openly.",
            "Basic resources for samples, materials and, when needed, travel.",
            "Response times in step with those of the UK trade.",
        ],
        "roles_label": "Who does what",
        "roles_head": ("Activity", "Me", "You"),
        "roles": [
            ("Analysis, positioning, pricing", "I analyse and recommend", "You decide"),
            ("Choice of partners", "I research and propose a reasoned list", "You choose whom to meet"),
            ("First contact with the trade", "I introduce you, stating my role", "You authorise every contact"),
            ("Prices, exclusivity, orders, contracts", "I advise you", "You negotiate and sign"),
            ("Licences, duty, labelling, importation", "I flag the issues and refer you to specialists", "The decision is yours"),
        ],
        "on_request": ("On request", "Hourly project", [
            "Even for a few hours, for one month or for a single project: you decide when and how many hours you want me to give to your project in the UK market.",
            "You receive a quote built on your requests.",
        ]),
    },
}


def how(t, h):
    it_path = h["path"] if t["lang"] == "it" else h["other"]
    en_path = h["other"] if t["lang"] == "it" else h["path"]
    steps = "\n".join(
        f'        <li><span class="step-n">{i}</span><div><h3>{name}</h3><p>{text}</p></div></li>'
        for i, (name, text) in enumerate(h["steps"], 1))
    def card(k, name, dur, paras):
        d = f'<p class="phase-d">{dur}</p>' if dur else ""
        return (f'<article class="phase"><p class="phase-k">{k}</p><h3>{name}</h3>{d}'
                + "".join(f"<p>{p}</p>" for p in paras) + "</article>")
    cards = [card(*ph) for ph in h["phases"]]
    if h.get("on_request"):
        k, name, paras = h["on_request"]
        cards[-1] = '<div class="phase-stack">' + cards[-1] + card(k, name, "", paras) + "</div>"
    phases = "\n".join("        " + c for c in cards)
    li = lambda items: "\n".join(f"        <li>{x}</li>" for x in items)
    rh = h["roles_head"]
    rows = "\n".join(
        f'          <tr><th scope="row">{a}</th><td data-k="{rh[1]}">{b}</td><td data-k="{rh[2]}">{c}</td></tr>'
        for a, b, c in h["roles"])
    return head(t, it_path, en_path, h["title"], h["desc"]) + header(t, it_path, en_path) + f"""<main>
  <div class="page-hero">
    <div class="inner">
      <h1>{lines(h['h1'])}</h1>
      <span class="rule"></span>
      <p>{h['sub']}</p>
    </div>
  </div>

  <section class="for-whom">
    <div class="inner">
      <h2 class="label">{h['for_label']}</h2>
      <span class="rule"></span>
      <ul class="bullets">
{li(h['for'])}
      </ul>
    </div>
  </section>

  <section class="path">
    <div class="inner">
      <h2 class="label">{h['before_label']}</h2>
      <span class="rule"></span>
      <ol class="steps">
{steps}
      </ol>
    </div>
  </section>

  <section class="phases">
    <div class="inner-wide">
      <h2 class="label">{h['after_label']}</h2>
      <span class="rule"></span>
      <div class="phase-grid">
{phases}
      </div>
    </div>
  </section>

  <section class="needs">
    <div class="inner">
      <h2 class="label">{h['need_label']}</h2>
      <span class="rule"></span>
      <ul class="bullets">
{li(h['need'])}
      </ul>
    </div>
  </section>

  <section class="roles">
    <div class="inner-wide">
      <h2 class="label">{h['roles_label']}</h2>
      <span class="rule"></span>
      <table class="roles-table">
        <thead><tr><th scope="col">{rh[0]}</th><th scope="col">{rh[1]}</th><th scope="col">{rh[2]}</th></tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>
  </section>

{contact_block(t)}</main>
""" + footer(t)


PRIVACY = {
    "it": {"h1": "Informativa privacy", "body": "privacy_it.html",
           "title": "Privacy Policy | Francesco Gabriele | Beverage Strategist",
           "desc": "Informativa privacy di FG Beverage Strategy Ltd: quali dati personali raccogliamo, perché li usiamo, per quanto tempo li conserviamo e i tuoi diritti."},
    "en": {"h1": "Privacy Notice", "body": "privacy_en.html",
           "title": "Privacy Policy | Francesco Gabriele | Beverage Strategist",
           "desc": "Privacy Notice of FG Beverage Strategy Ltd: the personal data we collect, why we use it, how long we keep it and your rights."},
}


def privacy(t):
    """Body text comes from the approved Word file; see extract_privacy.py."""
    v = PRIVACY[t["lang"]]
    with open(os.path.join(ROOT, "_build", v["body"]), encoding="utf8") as f:
        body = f.read()
    paths = ("/privacy-policy.html", "/en/privacy-policy.html")
    return head(t, *paths, v["title"], v["desc"]) + header(t, *paths) + f"""<main>
  <div class="page-hero">
    <div class="inner">
      <h1>{v['h1']}</h1>
      <span class="rule"></span>
    </div>
  </div>

  <section class="legal-text">
    <div class="inner">
{body}    </div>
  </section>
</main>
""" + footer(t)


PAGES = [("/", "/en/"), ("/come-lavoriamo.html", "/en/how-we-work.html"),
         ("/privacy-policy.html", "/en/privacy-policy.html")]


def sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for it, en in PAGES:
        for own in (it, en):
            out += ["  <url>", f"    <loc>{SITE}{own}</loc>",
                    f'    <xhtml:link rel="alternate" hreflang="it" href="{SITE}{it}"/>',
                    f'    <xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/>',
                    f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{it}"/>',
                    "  </url>"]
    return "\n".join(out + ["</urlset>", ""])


def redirect(target, label):
    """Old address kept alive: sends visitors and search engines to the new page."""
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{label}</title>
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{SITE}{target}">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
<main><section><div class="inner"><p><a href="{target}">{label}</a></p></div></section></main>
</body>
</html>
"""


def not_found():
    t = T["it"]
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pagina non trovata | Francesco Gabriele | Beverage Strategist</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
""" + header(t, "/", "/en/") + """<main>
  <div class="page-hero">
    <div class="inner">
      <h1>Pagina non trovata</h1>
      <span class="rule"></span>
      <p>Questo indirizzo non porta a una pagina del sito. <span lang="en">This address leads to no page on the site.</span></p>
    </div>
  </div>
  <section class="legal-text">
    <div class="inner">
      <p><a href="/">Torna alla home</a> <span class="sep">·</span> <a href="/en/" lang="en">Back to home</a></p>
    </div>
  </section>
</main>
""" + footer(t)


def home(t):
    paras = "\n".join(f"      <p>{p}</p>" for p in t["about"])
    rec = "\n".join(f"        <li>{r}</li>" for r in t["rec"])
    return head(t, "/", "/en/") + header(t, "/", "/en/") + f"""<main>
  <div class="hero">
    <div class="hero-photo" aria-hidden="true" style="background-image:url('/assets/img/hero-orologio.jpg')"></div>
    <div class="hero-copy">
      <h1>{lines(t['h1'])}</h1>
      <span class="rule"></span>
      <p>{t['sub']}</p>
      <a class="btn" href="{t['how_url']}">{t['cta']}</a>
    </div>
  </div>

  <section class="statement">
    <p>{lines(t['statement'])}</p>
  </section>

  <section class="recognise">
    <div class="inner-wide">
      <h2 class="label">{t['rec_label']}</h2>
      <span class="rule"></span>
      <ul class="rec-grid">
{rec}
      </ul>
    </div>
  </section>

  <section class="about" id="{t['about_id']}">
    <div class="about-grid">
      <img class="about-photo" src="/assets/img/francesco-gabriele-cantina.jpg" width="1000" height="1163" alt="{t['photo_alt']}" loading="lazy">
      <div class="about-copy">
        <h2 class="label">{t['nav_about']}</h2>
        <span class="rule"></span>
{paras}
        <p class="more"><a href="{LINKEDIN}" target="_blank" rel="noopener">{t['linkedin']}</a></p>
      </div>
    </div>
  </section>

{contact_block(t)}</main>
""" + footer(t)


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf8") as f:
        f.write(text)
    print("wrote", rel, len(text))


if __name__ == "__main__":
    write("index.html", home(T["it"]))
    write("en/index.html", home(T["en"]))
    write("come-lavoriamo.html", how(T["it"], HOW["it"]))
    write("en/how-we-work.html", how(T["en"], HOW["en"]))
    write("privacy-policy.html", privacy(T["it"]))
    write("en/privacy-policy.html", privacy(T["en"]))
    write("producers.html", redirect("/come-lavoriamo.html", "Come lavoriamo"))
    write("404.html", not_found())
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
