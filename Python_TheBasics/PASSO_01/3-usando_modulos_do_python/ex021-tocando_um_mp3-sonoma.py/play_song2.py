import pygame
# for audio playback on Sonoma 14.4

# Specify the downloaded audio file path
audio_file = "helloworld.mp3"  # Replace with your actual file

# Initialize Pygame
pygame.init()

# Load the audio file
sound = pygame.mixer.Sound(audio_file)

# Play the audio
sound.play()

# Wait for the audio to finish playing (optional)
while pygame.mixer.get_busy():
    pygame.time.wait(100)  # Adjust wait time as needed

# Quit Pygame
pygame.quit()

print("Audio playback complete.")