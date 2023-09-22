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
            csv_list.append(list((genre, artist, album, name)))
    return csv_list

def generate_tree(data_list, tree):
    # Collection of data!
    genres = []

    # Gathering genres.
    for song in data_list:
        # genre = song[3]
        # artist = song[2]
        # album = song[1]
        # name = song[0]
        # tree_genre = TreeNode(genre)
        # if genre not in genres:
        #     genres.append(genre)
        #     tree.add_child(tree_genre)
        for item in song:
            if item not in genres:
                genres.append(item)
                tree.add_child(TreeNode(item))
        


        

my_tree = TreeNode('Library')
tree_genre = TreeNode('Genres')
my_tree.add_child(tree_genre)
generate_tree(get_dict('songs_database.csv'), tree_genre)
print(my_tree)