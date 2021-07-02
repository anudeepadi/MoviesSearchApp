import json
import requests


def imbdGetId():
    # Example of two words movie
    #  url: 'https://data-imdb1.p.rapidapi.com/series/idbyTitle/The%20Avengers/',

    moviename = input('Please enter a Movie name\n')
    url = "https://data-imdb1.p.rapidapi.com/movie/imdb_id/byTitle/{}/".format(moviename)
    headers = {
        'x-rapidapi-key': "Enter Your Rapid Api Key Here",
        'x-rapidapi-host': "Enter Rapid Api Hostname"
    }
    response = requests.request("GET", url, headers=headers)
    response_string = response.text
    textfile = open("main1.json", "r+")
    textfile.write(response_string)
    textfile.close()
    # Opening JSON file
    with open('main1.json', 'r+') as json_file:
        data = json.load(json_file)
        this_data = data['Result'][0]['imdb_id']
    return this_data


def getMovieShow():
    url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{}".format(imbdGetId())

    headers = {
        'x-rapidapi-key': "Enter Your Rapid Api Key Here",
        'x-rapidapi-host': "Enter Rapid Api Hostname"
    }

    response = requests.request("GET", url, headers=headers)
    this_again = response.text
    textfile1 = open("main2.json", "r+")
    textfile1.write(this_again)
    textfile1.close()

    with open('main2.json', 'r+') as json_file:
        data = json.load(json_file)
        print("The Movies Application By Anudeep Adiraju")
        print("All Rights Reserved")
        print("Movie Details: ")
        print("ID: ", data['id'])
        print("Title: ", data['title'])
        print("Year: ", data['year'])
        print("Length: ", data['length'])
        print("Rating: ", data['rating'])
        print("Poster:\n", data['poster'])
        print("Trailer: ", data['trailer']['link'])
        print("Plot: ", data['plot'])
        print("Cast:-")
        print("1:", data['cast'][0]['actor'] + " as " + data['cast'][0]['character'])
        print("2:", data['cast'][1]['actor'] + " as " + data['cast'][1]['character'])
        print("3:", data['cast'][2]['actor'] + " as " + data['cast'][2]['character'])
        print("4:", data['cast'][3]['actor'] + " as " + data['cast'][3]['character'])
        print("5:", data['cast'][4]['actor'] + " as " + data['cast'][4]['character'])
        json.dumps(data, indent=4)

# To Work on this
# def delete1():
#     obj = json.load(open("main1.json"))
# 
#     # Iterate through the objects in the JSON and pop (remove)
#     # the obj once we find it.
#     for i in range(len(obj)):
#         obj.pop(i)
#         break
# 
#     # Output the updated file with pretty JSON
#     open("updated-file.json", "w").write(
#         json.dumps(obj, sort_keys=True, indent=4)
#     )

# TODO add Tv Show search
# TODO add Genre,Year,Actor...Search
# TODO add option to see Trailer in Vlc
# TODO display image


if __name__ == '__main__':
 getMovieShow()
