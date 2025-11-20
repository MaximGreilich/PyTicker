#grma1075 94731
from util_module import compute_area as f
import util_module as mod

ergebnis = f(15,8)
print(ergebnis)
settings = mod.Configuration.get_default_settings()
print(settings)

#h) Das würde nicht funktionieren, da der Import mit den Aliasen f und mod gemacht wurde, d.h. in dieser Datei ist der Namensraum des Moduls nicht bekannt
