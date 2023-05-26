import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

# Ruta al archivo .wav
archivo_wav = 'C:\\Users\\akhat\\Desktop\\lab3_señales\\acoustic.wav'

# Leer el archivo de audio
fs, y = wavfile.read(archivo_wav)

# Cálculo de la Transformada de Fourier
fft_result = np.fft.fft(y)
amplitudes = np.abs(fft_result)

# Gráfico de la Transformada de Fourier
frequencies = np.fft.fftfreq(len(y), 1 / fs)
plt.plot(frequencies, amplitudes)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title('Transformada de Fourier')
plt.grid(True)
plt.show()

# Cálculo del espectrograma
frequencies, times, spectrogram = signal.spectrogram(y, fs)

# Gráfico del espectrograma
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram))
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.title('Espectrograma')
plt.colorbar(label='dB')
plt.show()
