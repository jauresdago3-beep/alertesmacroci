import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import zoneinfo
from config import XML_URL

def convert_to_gmt(date_str, time_str):
    """Convertit l'heure US/Eastern de ForexFactory en GMT (Heure d'Abidjan)"""
    try:
        full_date_str = f"{date_str} {time_str}"
        dt_us = datetime.strptime(full_date_str, "%m-%d-%Y %I:%M%p")
        
        # Fuseau source ForexFactory (US/Eastern)
        us_tz = zoneinfo.ZoneInfo("America/New_York")
        dt_us = dt_us.replace(tzinfo=us_tz)
        
        # Fuseau cible (GMT / UTC)
        gmt_tz = zoneinfo.ZoneInfo("UTC")
        dt_gmt = dt_us.astimezone(gmt_tz)
        
        return dt_gmt.strftime("%d/%m/%Y"), dt_gmt.strftime("%H:%M GMT")
    except Exception:
        return date_str, time_str

def get_high_impact_events():
    try:
        response = requests.get(XML_URL, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Erreur lors de la récupération du flux : {e}")
        return []

    root = ET.fromstring(response.content)
    events = []

    for event in root.findall('event'):
        impact = event.find('impact').text
        if impact and impact.lower() == 'high':
            title = event.find('title').text
            country = event.find('country').text
            date_raw = event.find('date').text
            time_raw = event.find('time').text
            forecast = event.find('forecast').text
            previous = event.find('previous').text

            date_gmt, time_gmt = convert_to_gmt(date_raw, time_raw)

            events.append({
                'title': title,
                'country': country,
                'date': date_gmt,
                'time': time_gmt,
                'forecast': forecast if forecast else 'N/A',
                'previous': previous if previous else 'N/A'
            })

    return events
