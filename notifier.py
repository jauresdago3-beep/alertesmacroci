import requests
from config import TOKEN, CHAT_ID

def send_telegram_alert(events):
    if not events:
        message = "📅 **ALERTES MACRO CI**\n\n🟢 Aucune annonce à fort impact (High) détectée aujourd'hui."
    else:
        message = "📅 **ALERTES MACRO CI — RAPPEL PÉRIODIQUE**\n"
        message += "📍 *Horaires convertis en GMT (Heure d'Abidjan)*\n\n"
        
        for ev in events:
            message += f"🌍 **Devise :** {ev['country']}\n"
            message += f"📌 **Événement :** {ev['title']}\n"
            message += f"⏰ **Heure GMT :** {ev['date']} à **{ev['time']}**\n"
            message += f"📊 **Prévu :** {ev['forecast']} | **Précédent :** {ev['previous']}\n"
            message += "----------------------------------------\n"
        
        message += "\n⚠️ *Information de marché uniquement — pas un conseil financier.*"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, json=payload)
    return response.json()
