# Frage 2

1. Messen wie viel der generierten Minuten/Sekunden tatsächlich abgespielt werden. (Wie viel als "Waste" endet)

Hebel:

- Einen Cache implementieren der besonders häufige Antworten beinhaltet, sodass diese nicht öfters generiert werden müssen.
(Keine Einschränkungen des Betriebs)

- On Demand generierung -> Davon ausgehen das das Kind sehr sprunghaft mit der KI umgeht. Somit nur einen (kleinen) Teil der Antwort vorgenerieren. (Kleine Einschränkung des Betriebs möglich)

- APIs Staffeln: Günstige API für kleine Texte/Simple antworten. Teurere API für z.B. emotionale Antworten.

# Frage 3

Sehr schwierig eine klare Antwort zu definieren, sehr Situationsabhägig.

Das Gerät würde je nach System-Prompt das Thema umschreiben und keine klare Antwort liefern.
Zusätzlich dazu würde eine Benachrichtigung an die Eltern-App geschickt werden, um sie darauf aufmerksam zu machen und eventuell selbst mit dem Kind ins Gespräch zu gehen.

- Eine zweite KI als reasoning Instanz benutzen, bevor die Antwort an das Gerät gegeben wird, um mögliche Schlupflöcher zu stopfen.

# Frage 4

- Debuggen über z.B. LangSmith um Latenzen aufzudecken bzw. andere Probleme in der Pipeline zu erkennen.
- Überprüfen, ob das Problem überhaupt auf unserer Seite liegt oder z.B. durch einen instabile WLAN Verbindung auf der Nutzer seite liegt. -> Durch überprüfen der Latenz zum Gerät selber.