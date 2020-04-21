import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


letter_scores = {"A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4, "I":1, "J":8, "K":5, "L":1,"M":3, "N":1, "O":1,
                 "P":3, "Q":10, "R":1, "S":1, "T":1, "U":1, "V":4, "W":4, "X":8, "Y":4, "Z":10}

def calculate_country_scores(countries):
    scores = []
    for country in countries:
        scores.append(get_word_score(country))
    return scores
def get_letter_score(letter):
    return letter_scores[letter.upper()]

def get_word_score(word):
    sum = 0
    for letter in list(word):
        if letter.upper() in letter_scores:
            sum += get_letter_score(letter)
    return sum

country_names = pd.read_csv("Countries-Continents.csv")

country_names["scores"] = country_names["Country"].apply(get_word_score)


print("MINIMUM COUNTRY SCRABBLE SCORES")
print(country_names.head(20))
max_score = country_names["scores"].max()
print(country_names[country_names["scores"] == max_score])

country_names.sort_values(by="scores", inplace=True)



#illustrate scrabble scores
data = [country_names[country_names["Continent"] == "Africa"]["scores"],
        country_names[country_names["Continent"] == "Europe"]["scores"],
        country_names[country_names["Continent"] == "North America"]["scores"],
        country_names[country_names["Continent"] == "South America"]["scores"],
        country_names[country_names["Continent"] == "Oceania"]["scores"],
        country_names[country_names["Continent"] == "Asia"]["scores"]]
fig = plt.figure()
ax = fig.add_subplot(111)
bp = ax.boxplot(data)
#plt.boxplot(country_names[country_names["Continent"] == "Africa"]["scores"])
#plt.boxplot(country_names[country_names["Continent"] == "Europe"]["scores"])
ax.set_xticklabels(['Africa', 'Europe', 'North America',
                    'South America', 'Oceania', 'Asia'])
plt.show()



#save data
#country_names.to_excel("/Users/karlgodard/PycharmProjects/ScrabblePuzzle/CountryScrabbleScoresWithContinents.xlsx")
#print(country_names.head())


Card::Card(char suit1, int rank1) {
    suit =  suit1;
    rank = rank1;
}