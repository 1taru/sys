import numpy as np
import matplotlib.pyplot as plt
from scipy import fft, signal

# Parámetros de la señal
amplitud = 1.0
frecuencia = 200  # Hz
duracion = 1  # segundos
num_puntos = 1000  # Número de puntos en la señal

# Generar la señal sinusoidal
t = np.linspace(0, duracion, num_puntos)  # Tiempo
x = amplitud * np.sin(2 * np.pi * frecuencia * t)  # Señal

# Cálculo de la Transformada de Fourier
fft_result = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(x), t[1] - t[0])

# Gráfico de la Transformada de Fourier
plt.figure()
plt.plot(frequencies, np.abs(fft_result))
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title('Transformada de Fourier')
plt.grid(True)
plt.show()

# Cálculo del espectrograma
frequencies, times, spectrogram = signal.spectrogram(x, fs=1/(t[1]-t[0]))

# Gráfico del espectrograma
plt.figure()
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram))
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.title('Espectrograma')
plt.colorbar(label='dB')
plt.show()
