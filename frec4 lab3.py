import numpy as np
import matplotlib.pyplot as plt
from scipy import fft, signal

# Parámetros de la señal 1
amplitud1 = 1.0
frecuencia1 = 200  # Hz
duracion = 1  # segundos
num_puntos = 1000  # Número de puntos en la señal

# Parámetros de la señal 2
amplitud2 = 10.0
frecuencia2 = 500  # Hz

# Generar las señales sinusoidales
t = np.linspace(0, duracion, num_puntos)  # Tiempo
x1 = amplitud1 * np.sin(2 * np.pi * frecuencia1 * t)  # Señal 1
x2 = amplitud2 * np.sin(2 * np.pi * frecuencia2 * t)  # Señal 2

# Sumar las señales
x_suma = x1 + x2

# Agregar ruido blanco de distribución normal
ruido = np.random.randn(len(x_suma))
x_suma_con_ruido = x_suma + ruido

# Cálculo de la Transformada de Fourier
fft_result = np.fft.fft(x_suma_con_ruido)
frequencies = np.fft.fftfreq(len(x_suma_con_ruido), t[1] - t[0])

# Gráfico de la Transformada de Fourier
plt.figure()
plt.plot(frequencies, np.abs(fft_result))
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title('Transformada de Fourier')
plt.grid(True)
plt.show()

# Cálculo del espectrograma
frequencies, times, spectrogram = signal.spectrogram(x_suma_con_ruido, fs=1/(t[1]-t[0]))

# Gráfico del espectrograma
plt.figure()
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram))
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.title('Espectrograma')
plt.colorbar(label='dB')
plt.show()
