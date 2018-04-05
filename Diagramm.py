import dateparser as dateparser
import matplotlib.pyplot as plt
from load import load_csv, filterandsort


dataset= load_csv("C:\\Users\\Markus\\Downloads\\JIRA_Rohdaten.csv")
dataset= filterandsort(dataset=dataset[1:], sortindex=0,  columnfilter=[3, 41])

Storypoint = []
Datum = []


for row in dataset:
    try:
        float(row[0])
        if float(row[0])<20:
            Storypoint.append(float(row[0]))
            Datum.append(dateparser.parse(row[1]))
    except:
        continue


# Label für die y-Achse vergeben:
plt.xlabel('Datum')
plt.ylabel('Storypoints')

# Einen x-y-Plot erstellen:
plt.plot(Datum, Storypoint, 'g^')


# Ein gepunktetes Diagramm-Gitter einblenden:
plt.grid(True)

# Diagramm anzeigen:
plt.show()