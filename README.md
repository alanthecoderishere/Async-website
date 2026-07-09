# ASYNC Research Institute — 1983 Intranet Portal

> *"Please be advised that all data on this server is strictly confidential."*

A lovingly crafted **1990s Web 1.0 style website** for the **ASYNC Research Institute** from the *Backrooms* series by [Kane Pixels](https://www.youtube.com/@KanePixels). Built entirely with authentic vintage HTML, CSS, and JavaScript — no frameworks, no modern patterns, just pure Geocities-era chaos.

---

## 🖥️ Features

- **Fixed 640×480 VGA viewport** — exactly like the monitors of the era
- **Authentic 1990s layout** — table-based structure, `<font>` tags, `<marquee>`, `<center>`, all the classics
- **Real ASYNC lore** sourced from the [Kane Pixels Backrooms Wiki](https://kanepixelsbackrooms.fandom.com/wiki/Async_Research_Institute):
  - About ASYNC (founded 1983 by Lawrence Altman in San Jose, CA)
  - Project KV31 & the LPMDS (gateway opened October 17, 1989)
  - Staff Directory (Ivan Beck, Peter Tench, Marvin E. Leigh, and more)
  - Safety Protocols (Class A hazmat suits, groups of 3 minimum)
  - Contact Us (spoiler: the mail server is down)
- **Simulated 1990 system clock** in the footer
- **Employee Login Portal** with an authentic Windows BSOD error
- **Spinning globe GIF** and **Under Construction badge** in the sidebar
- **Official ASYNC expanded logo** from the wiki

---

## 📁 File Structure

```
Async-Web/
├── index.html        # Home / Login page
├── about.html        # About ASYNC
├── kv31.html         # Project KV31 & The Threshold
├── staff.html        # Staff Directory
├── safety.html       # Safety Protocols
├── contact.html      # Contact Us
├── style.css         # 1990s stylesheet
├── script.js         # Vintage JavaScript
├── async_logo.png    # Official ASYNC expanded logo (from wiki)
├── globe.gif         # Spinning globe sidebar animation
├── undercon.gif      # Under Construction badge
├── portal.svg        # LPMDS gateway diagram (KV31 page)
└── gen_pages.py      # Script used to generate the inner HTML pages
```

---

## 🚀 Running Locally

No build step needed. Just serve the directory with any static file server:

```bash
# Python 3
python3 -m http.server 8080
```

Then open [http://localhost:8080](http://localhost:8080) in your browser.

> **Best viewed in Netscape Navigator 3.0 at 640×480 resolution.**

---

## 📖 Lore Context

The **Async Research Institute** (est. 1983) is a private research organization from the *Backrooms* found-footage YouTube series by Kane Parsons (Kane Pixels). Originally an MRI company, Async secretly developed the **Low-Proximity Magnetic Distortion System (LPMDS)** — a machine capable of opening a stable portal into an extradimensional space known as **The Complex**, or *The Backrooms*. The first successful gateway was opened on **October 17, 1989**.

---

*This is a fan project. All lore belongs to Kane Parsons / Kane Pixels.*
