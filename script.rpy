# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Budi", image="budi.png")
define pt = Character("Pak Taat", image="pak taat.png")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # main menu:
    # show cityscape
    # play music

    scene bg "Kota Metropolitan Intro dan Mode Hunter.JPG"

    show budi
    b "Tandai hadir!"

    show pak taat
    

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    Budi ""

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
