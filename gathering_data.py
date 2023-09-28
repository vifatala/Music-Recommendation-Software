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
    # Collection of data! I use this lists to track which names, albums, artists, and genres have already been added to the tree.
    # This way there are no repetitions.
    names = []
    albums = []
    artists = []
    genres = []

    # This for loop interacts over all the lists of songs in the CSV file.
    # As we keep each song in a list with their 'Name', 'Album', 'Artist', and 'Genre', we can easily organize and add children to one another.
    # In case we don't have the current tree in the previous parent tree, we add them as a child. Otherwise, we set the current tree to be the one which
    # already exists in the parent tree.
    # Kinda confusing, but it works!!! (btw I couldn't implement a helper method to do this 'if and else' blocks. Gotta try more)
    for song in data_list:
        genre = song[3]
        artist = song[2]
        album = song[1]
        name = song[0]

        tree_genre = TreeNode(genre)
        if genre not in genres:
            genres.append(genre)
            tree.add_child(tree_genre)
        else:
            for child in tree.children:
                if child.value == genre:
                    tree_genre = child

        tree_artist = TreeNode(artist)
        if artist not in artists:
            artists.append(artist)
            tree_genre.add_child(tree_artist)
        else:
            for child in tree_genre.children:
                if child.value == artist:
                    tree_artist = child

        tree_album = TreeNode(album)
        if album not in albums:
            albums.append(album)
            tree_artist.add_child(tree_album)
        else:
            for child in tree_artist.children:
                if child.value == album:
                    tree_album = child

        tree_name = TreeNode(name)
        if name not in names:
            names.append(name)
            tree_album.add_child(tree_name)
        else:
            for child in tree_album.children:
                if child.value == name:
                    tree_name = child
