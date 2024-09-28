from gtts import gTTS
import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.core.clipboard import Clipboard

# Function to generate Bangla speech from text
def generate_speech(text, voice_type='female', pitch='normal', filename="output.mp3"):
    # Generate speech using gTTS
    tts = gTTS(text=text, lang='bn')  # 'bn' for Bangla
    tts.save(filename)
    os.system(f"mpv {filename}")  # Play the audio

# Kivy App for the TTS generator
class BanglaTTSApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # App Title
        title_label = Label(text='Bangla Text-to-Speech', font_size=32, color=(0, 0.4, 1, 1), size_hint=(1, 0.1))

        # Text Input for pasting or entering Bangla text
        self.text_input = TextInput(hint_text='Enter your Bangla text here', multiline=True, font_size=24, size_hint=(1, 0.5))

        # Dropdown for selecting voice types (Male, Female, Kid)
        self.voice_dropdown = DropDown()
        self.voice_button = Button(text='Select Voice Type', size_hint=(1, 0.1), background_color=(0, 0.5, 0.8, 1))
        for voice_type in ['Male', 'Female', 'Kid']:
            btn = Button(text=voice_type, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.voice_dropdown.select(btn.text))
            self.voice_dropdown.add_widget(btn)
        self.voice_button.bind(on_release=self.voice_dropdown.open)
        self.voice_dropdown.bind(on_select=lambda instance, x: setattr(self.voice_button, 'text', x))

        # Dropdown for selecting pitch (Deep, Low, Normal)
        self.pitch_dropdown = DropDown()
        self.pitch_button = Button(text='Select Pitch', size_hint=(1, 0.1), background_color=(0.2, 0.6, 1, 1))
        for pitch_type in ['Deep', 'Low', 'Normal']:
            btn = Button(text=pitch_type, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.pitch_dropdown.select(btn.text))
            self.pitch_dropdown.add_widget(btn)
        self.pitch_button.bind(on_release=self.pitch_dropdown.open)
        self.pitch_dropdown.bind(on_select=lambda instance, x: setattr(self.pitch_button, 'text', x))

        # Progress Bar
        self.progress_bar = ProgressBar(max=100, value=0, size_hint=(1, 0.1))

        # Buttons for Play, Paste, and Download
        self.play_button = Button(text='Play Speech', size_hint=(1, 0.1), background_color=(0, 0.5, 0.9, 1))
        self.play_button.bind(on_press=self.play_speech)
        self.paste_button = Button(text='Paste Text', size_hint=(1, 0.1), background_color=(0, 0.6, 0.7, 1))
        self.paste_button.bind(on_press=self.paste_text)
        self.download_button = Button(text='Download Speech', size_hint=(1, 0.1), background_color=(0.2, 0.8, 1, 1))
        self.download_button.bind(on_press=self.download_speech)

        # Premium Voice Option
        self.premium_button = Button(text='Premium Voice Options', size_hint=(1, 0.1), background_color=(1, 0.8, 0, 1))
        self.premium_button.bind(on_press=self.show_premium_info)

        # Adding widgets to the layout
        layout.add_widget(title_label)
        layout.add_widget(self.text_input)
        layout.add_widget(self.voice_button)
        layout.add_widget(self.pitch_button)
        layout.add_widget(self.progress_bar)
        layout.add_widget(self.play_button)
        layout.add_widget(self.paste_button)
        layout.add_widget(self.download_button)
        layout.add_widget(self.premium_button)

        return layout

    # Function to paste text from clipboard
    def paste_text(self, instance):
        self.text_input.text = Clipboard.paste()

    # Function to play the generated speech
    def play_speech(self, instance):
        text = self.text_input.text
        if text:
            self.progress_bar.value = 50  # Simulate progress
            generate_speech(text, voice_type=self.voice_button.text.lower(), pitch=self.pitch_button.text.lower())
            self.progress_bar.value = 100  # Mark completion

    # Function to download the generated speech
    def download_speech(self, instance):
        text = self.text_input.text
        if text:
            generate_speech(text, voice_type=self.voice_button.text.lower(), pitch=self.pitch_button.text.lower(), filename="bangla_speech.mp3")
            print("Speech downloaded as bangla_speech.mp3")  # Notify user

    # Function to show premium information
    def show_premium_info(self, instance):
        print("Upgrade to premium for neural and natural voices!")

# Run the app
if __name__ == '__main__':
    BanglaTTSApp().run()