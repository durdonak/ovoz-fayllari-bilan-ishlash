# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EVeRp2O-5WKeO_pQhZMiFYWcVvr6xbFE
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = 'music.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = 'music2.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = 'music3.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

!pip install gTTS

from gtts import gTTS
from IPython.display import Audio

text = "Good morning here, how can i help you?"
language = 'en'

tts = gTTS(text=text, lang=language, slow=False)

audio_file = "output.mp3"
tts.save(audio_file)

Audio(audio_file)