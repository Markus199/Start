import re
import os
import webbrowser
import csv


def load_csv(frame, check=True):
    file = open(frame, "r")
    reader = csv.reader(file, delimiter=";", quotechar='"')
    dataset = []
    for list in reader:
        dataset.append(list)

    sonderzeichen = ["*", "#", "/", '"', '_', ]

    if check:
        if dataset.count('"') % 2 != 0:
            print("Bitte laden Sie die richtige CSV_Datei")
            return

        for zeichen in sonderzeichen:
            for i in range(0,len(dataset)):
                for j in range(len(dataset[i])):
                    newString = dataset[i][j].replace(zeichen, " ")
                    newString = re.sub('\s{2,}', ' ', newString)
                    dataset[i][j] = newString





    return dataset


def filterandsort(dataset, columnfilter=[], rowfilter='True', sortindex=None):

    zr = [[l[i] for i in range(len(l)) if len(columnfilter) == 0 or i in columnfilter] for l in dataset if eval(rowfilter)]

    if sortindex >= 0 and sortindex < len(dataset[0]):
        zr = zr[:1] + qs(zr[1:], sortindex)
        return zr


    return zr


def qs(ds, si):
    if ds == []: return ds
    return qs([line for line in ds[1:] if line[si] < ds[0][si]], si) + ds[0:1] + qs(
        [line for line in ds[1:] if line[si] >= ds[0][si]], si)


def data2HTML(dataset, maxcolumnsize=None):
    html = "<html><header><title>Datensatzausgabe</title>" \
           "</header>" \
           "<body><h1>Dies dient der Ausgabe eines Datensatzes im HTML-Format</h1><table>"
    for l in dataset:
        html += "<tr>"
        for e in l:
            if maxcolumnsize:
                es = e[:maxcolumnsize]
            else:
                es=str(e)
            html += "<td>" + es + "</td>"
        html += "</tr>"
    html += "</table></body></html>"

    path = os.path.abspath('data.html')
    url = 'file://' + path
    with open(path, 'w') as f:
        f.write(html)
    webbrowser.open(url)

#dokument=load_csv("C:\\Users\\Markus\\Downloads\\JIRA_Rohdaten.csv")
#data2HTML(filterandsort(dataset=dokument, sortindex=0, columnfilter=[3, 41]), 50)
#dokument=filterandsort(dataset=dokument, sortindex=0, columnfilter=[3, 41])

