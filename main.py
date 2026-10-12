from fetcher import get_high_impact_events
from notifier import send_telegram_alert

def main():
    print("🔍 Récupération du calendrier macro-économique...")
    events = get_high_impact_events()
    print(f"-> {len(events)} événement(s) à fort impact trouvés.")
    
    print("📤 Envoi des alertes vers Telegram...")
    result = send_telegram_alert(events)
    print("Résultat de l'envoi :", result)

if __name__ == "__main__":
    main()
