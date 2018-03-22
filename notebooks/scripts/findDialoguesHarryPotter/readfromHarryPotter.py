"""Books taken from https://javalibre.com.ua"""


books = ["Harri-Potter-i-Filosofskyj-Kamin-Dzhoan-Ketlin-Roling.txt",
         "Harri-Potter-i-tayemna-kimnata-Dzhoan-Ketlin-Roling.txt",
         "Harri-Potter-i-Smertelni-Relikviyi-Dzhoan-Ketlin-Roling.txt",
         "Harri-Potter-i-orden-Feniksa-Dzhoan-Ketlin-Roling.txt",
         "Harri-Potter-i-napivkrovnyj-prync-fb2-Dzhoan-Ketlin-Roling.txt",
         "Harri-Potter-i-Kelyh-Vohnyu-Dzhoan-Ketlin-Roling.txt",
         "Harri-Potter-i-vyazen-Azkabanu-Dzhoan-Ketlin-Roling.txt",
         ]

def dialogue_clean(phrase):
    dt = [phrase[i] + " " for i in range(len(phrase)) if (i % 2 == 0 and phrase[i] != ",")]
    return "".join(dt)

lst = list()
for book in books:
    with open('HarryPotterDialogues.txt', 'a') as dialogs:
        with open(book) as hp1:
            ct = 0
            for line in hp1:
                if line.startswith("     -"):
                    dt = line.strip().split("-")[1:]
                    ct += 1
                    dialogs.write(dialogue_clean(dt)+'\n')
                    print(dialogue_clean(dt))
                elif line.startswith("     —") or line.startswith("—"):
                    dt = line.strip().split("—")[1:]
                    dialogs.write(dialogue_clean(dt)+'\n')
                    print(dialogue_clean(dt))
                    ct += 1
            lst.append(ct)

print(sum(lst))