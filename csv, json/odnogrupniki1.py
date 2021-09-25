import csv
#data = [('Югансон', 'Наташа', 'ж', 15, 'mango'),('Кулешова', 'Вита', 'ж', 17, 'apple'),('Зуев', 'Гордей', 'м', 17, 'kiwi'),('Смирнов', 'Арсений', 'м', 16, 'mango'),('Харченко', 'Вера', 'ж', 16, 'apple'),('Хазова', 'Настя', 'ж', 27, 'orange'),('Смиронов', 'Саша', 'м', 17, 'mandarin'),('Смирнов', 'Артем', 'м', 17, 'apple'),('Рапота', 'Маша', 'ж', 17, 'orange'),('Свиридов', 'Илья', 'м', 17, 'apple')]

#with open('odnogroupniki1.csv', 'w') as fp:
    #writer=csv.writer(fp, delimiter=',')
    #writer.writerows(data)
    
#with open('odnogroupniki1.csv', 'r') as fp:
    #reader=csv.reader(fp, delimiter=',')
    #data_read=[row for row in reader]

with open('moma.csv', newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row['DisplayName'], row['Gender'],row['ArtistBio'], sep=';')

#print(data_read)
