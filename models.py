#Zweck: Enthält die Datenstruktur und Hilfsfunktionen für Aufgaben und Deadlines.
# Importieren der notwendigen Module
from datetime import datetime, timedelta

#Funktion zum Parsen von Datum- und Zeitstrings in ein datetime-Objekt
def parse_deadline_string(date_str, time_str):
    try:
        #Kombinieren von Datum- und Zeitstrings und Parsen in datetime-Objekt
        comb_str = date_str + " " + time_str
        #Konvertieren des kombinierten Strings in ein datetime-Objekt
        deadline_obj = datetime.strptime(comb_str, "%Y-%m-%d %H:%M")
        return deadline_obj
    except ValueError:
        #Gibt None zurück, wenn das Format ungültig ist
        return None
    
# Definieren der Task-Klasse zur Darstellung einer Aufgabe mit Titel und Deadline
class Task: 
    def __init__(self, title, deadline):
        #Titel der Aufgabe(String) und Deadline (datetime-Objekt)
        self.title = title
        self.deadline = deadline
        #Status der Aufgabe (abgeschlossen oder nicht)
        self.completed = False
        
   

    
    # Funktion zur Berechnung der verbleibenden Zeit bis zur Deadline    
    def get_time_remaining(deadline: datetime) -> timedelta: 
        now = datetime.now()
        
        #Prüfen, ob die Deadline bereits vergangen ist
        if deadline < now:
            return timedelta(seconds=0)
        
        #Gibt die verbleibende Zeit als timedelta-Objekt zurück
        return deadline - now 
    
    
    # Funktion zur Formatierung eines timedelta-Objekts in einen lesbaren String
    def format_timedealta(td: timedelta) -> str: 
        
        #Gesamtanzahl der Sekunden im timedelta berechnen
        total_seconds = int(td.total_seconds())
        
        #berechnung von Tagen, Stunden, Minuten und Sekunden
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600 
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        #Formatierung des Strings basierend auf der verbleibenden Zeit
        if days > 0: 
            return f"{days}d {hours:02}h {minutes:02}m {seconds:02}s"
        elif hours > 0:
            return f"{hours:02}h {minutes:02}m {seconds:02}s"
        else:
            return f"{minutes:02}m {seconds:02}s"
        
         
    
        
        
        