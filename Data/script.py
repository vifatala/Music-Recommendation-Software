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
    for song in data_list:
        genre = song[3]
        tree_genre = TreeNode(genre)
        for child in tree.children:
            if tree_genre.value == child.value:
                print("achei")
        tree.add_child(tree_genre)
        

my_tree = TreeNode('Genres')
generate_tree(get_dict('songs_database.csv'), my_tree)
print(my_tree)