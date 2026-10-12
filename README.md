# 📊 Alertes Macro CI

Bot qui envoie chaque matin à 07h00 (heure d'Abidjan) les annonces économiques à fort impact, sur le canal Telegram [@alertesmacroci](https://t.me/alertesmacroci).

Fait pour les traders ivoiriens : plus besoin de convertir les heures américaines à la main.

## ✨ Fonctionnalités

- Récupère le calendrier économique ForexFactory (XML)
- Garde uniquement les annonces à fort impact
- Convertit les heures en GMT (Abidjan) avec zoneinfo
- Envoie un message formaté sur Telegram
- Tourne tout seul chaque matin (cron)

## 🧱 Structure

    config.py      # paramètres (TOKEN, CHAT_ID, URL)
    fetcher.py     # récupération et filtrage XML ForexFactory
    notifier.py    # mise en forme et envoi du message Telegram
    main.py        # orchestration globale

## ⚙️ Installation

    git clone https://github.com/jauresdago3-beep/alertesmacroci.git
    cd alertesmacroci
    pip install requests
    cp config.py.example config.py
    nano config.py

## ▶️ Lancer

    python main.py

## ⏰ Automatisation (Termux)

    pkg install cronie
    termux-wake-lock
    crond
    crontab -e
    0 7 * * * cd ~/alertesmacroci && python main.py

## 🛠️ Technologies

Python, Telegram Bot API, cron, Termux (Android)

## 👤 Auteur

Kodjo, Code Z, Abidjan 🇨🇮
