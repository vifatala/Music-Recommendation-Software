from gathering_data import *
from tree import TreeNode
from tree_search import bfs

# This function is used to interact with the user everytime they can make a search, call the bfs,
# and decide in which category (song, album, artist, genre) the value found should be. This is done by
# seeing how far the node found parent is from the 'Genres' node.
# 
def search_area():
    # Interaction
    print('')
    print(f"{name}, search for anything in the world of Rock music!")
    print("You can either type the name of a song, album, artist, or genre")
    print("Or type \'Library\' to see all of our catalog.")
    user_search = input("> ")
    print('')
    
    user_search_lower = user_search.lower()     # make the user input lower, so we don't need to worry about captalization.
    if user_search_lower == 'library':
        print(my_tree)
        try_again()
    else:
        goal_path, goal_node, possible = bfs(my_tree, user_search_lower)
        if (len(possible) != 0) and (goal_path is None):
            print(f"Starting with \'{user_search}\' in our catalog we have:")
            for value in possible:
                print("-"+value)
        elif goal_path is not None:
            print("Term found in:")
            for node in goal_path:
                print(f"{' |'  * goal_path.index(node)}-{node.value}")
            print('')

            if goal_node.parent.value == 'Genres':
                print(f"Inside the \'{goal_node.value}\' genre, we have the following artists:\n")
                for child in goal_node.children:
                    print(f"-{child.value}")
            elif goal_node.parent.parent.value == 'Genres':
                print(f"In {goal_node.value}'s discography, some of the albums we have are:\n")
                for child in goal_node.children:
                    print(f"-{child.value}")
            elif goal_node.parent.parent.parent.value == 'Genres':
                print(f"In \'{goal_node.value}\' by {goal_node.parent.value}, some of the tracks we have are:\n")
                for child in goal_node.children:
                    print(f"-{child.value}")
            else:
                print(f"\"{goal_node.value}\" is a track of the album \'{goal_node.parent.value}\' released by {goal_node.parent.parent.value}.\nThis is considered part of the {goal_node.parent.parent.parent.value} genre.\n")
                print(f"(Try searching for \'{goal_node.parent.parent.parent.value}\' to see more songs like this!)")
        else:
            print(f"Sorry, Victor, we could't find anything that started with \"{user_search}\" in our catalog!")
            try_again()
        print('')
        try_again()
        
            
def try_again():
    user_choice = input("Would you like to search more? (y/n) ").lower()
    if user_choice == 'y':
        search_area()
    elif user_choice == 'n':
        return
    else:
        print('')
        print("Please, enter a valid option.")
        try_again()

my_tree = TreeNode('Library')
tree_genre = TreeNode('Genres')
my_tree.add_child(tree_genre)
generate_tree(get_dict('songs_database.csv'), tree_genre)

print("""
      WELCOME TO THE

$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$'`$$$$$$$$$$$$$'`$$$
$$$$$$  $$$$$$$$$$$  $$$$
$$$$$$$  '$/ `/ `$' .$$$$
$$$$$$$$. i  i  /! .$$$$$
$$$$$$$$$.--'--'   $$$$$$
$$^^$$$$$'        J$$$$$$
$$$   ~""   `.   .$$$$$$$
$$$$$e,      ;  .$$$$$$$$
$$$$$$$$$$$.'   $$$$$$$$$
$$$$$$$$$$$$.    $$$$$$$$
$$$$$$$$$$$$$     $by&TL$
      
Rock Music Recommendation Software!
      """)
name = input("What is your name? ")
search_area()
print('')
print(f"Thank you for using our program, {name}!")

