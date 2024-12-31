from playsound import playsound
import random
import threading

# Define song paths and names
thriller = "C:\\Users\\Eric\\Downloads\\Michael Jackson - Thriller(1983) [Full Album].mp3"
september = "C:\\Users\\Eric\\Downloads\\September -Earth, Wind, and Fire.mp3"  #feel free to add more songs 

songs = [
    (thriller, "Thriller"),
    (september, "September")
]

# Randomly select a song
audio_file, song = random.choice(songs)


# Function to play the audio in a separate thread
def play_song():
    playsound(audio_file)


# Start playing the song in the background
thread = threading.Thread(target=play_song)
thread.start()


# Function to start the game
def start_game():
    lives = 3
    while lives > 0:
        guess = input("Guess the song: ")

        if guess == song:
            print(f"You guessed correctly! The song was {song}")
            break
        else:
            lives -= 1
            if lives > 0:
                print(f"Sorry, that's not correct. You have {lives} attempts left.")
            else:
                print(f"You ran out of lives. The song was {song}.")


# Start the game
start_game()
