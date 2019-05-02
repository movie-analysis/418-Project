# encoding=utf8
import tmdbsimple as tmdb
import sys
import csv
import time
reload(sys)
sys.setdefaultencoding('utf8')
tmdb.API_KEY = 'Get a free TMDB API key and throw it here'
Titles = []
i = 0
x = 0
search = tmdb.Search()
with open('Names.csv','r') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for column in csvReader:
        Titles.append(column[0])
with open('values.csv','a') as fd:
    writer = csv.writer(fd)
    while i < len(Titles):
        response = search.movie(query=Titles[x])
        for s in search.results:
            val = [s['title'],s['release_date'],s['vote_average'],s['genre_ids']]
            writer.writerow(val)
        x+=1
        i+=1
        print(i)
        time.sleep(0.25)