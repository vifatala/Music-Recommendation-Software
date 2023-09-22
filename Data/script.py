import csv
from tree import TreeNode

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
    return csv_list

def generate_tree(data_list, tree):
    # Collection of data!
    names = []
    albums = []
    artists = []
    genres = []

    # Gathering genres.
    for song in data_list:
        genre = song[3]
        artist = song[2]
        album = song[1]
        name = song[0]
        tree_genre = TreeNode(genre)
        tree_artist = TreeNode(artist)
        tree_album = TreeNode(album)
        tree_name = TreeNode(name)
        if genre not in genres:
            genres.append(genre)
            tree.add_child(tree_genre)
        tree_genre.add_child(tree_artist)
        tree_artist.add_child(tree_album)
        tree_album.add_child(tree_name)

        

my_tree = TreeNode('Library')
tree_genre = TreeNode('Genres')
my_tree.add_child(tree_genre)
generate_tree(get_dict('songs_database.csv'), tree_genre)
print(my_tree)