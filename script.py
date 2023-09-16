import csv

def get_dict(file):
    # Importing data from the CSV file.
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_list = []
        for row in csv_reader:
            name = row['Song Name']
            album = row['Album']
            artist = row['Band Name']
            genre = row['Genre']
            csv_list.append(list((name, album, artist, genre)))
            #print(f"\tThe song {row['Song Name']} is a {row['Genre']} track from the album \'{row['Album']}\' by {row['Band Name']}.") # First test handling data from CSV
    print(csv_list)
get_dict('songs_database.csv')
