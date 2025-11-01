import numpy as np

amplitude_spectrum = []
n_indexes = []

def fourier_series(t, A, w0, N, mode):
    amplitude_spectrum.clear()
    n_indexes.clear()
    
    wave_list = []
    
    if mode == 'triangular':
        for n in range(1, N + 1):
            n_indexes.append(n)
            sign = (-1)**((n - 1) // 2)
            if n % 2 == 0:
                wave_list.append(np.zeros_like(t))
                An = 0.0
            else:
                An = sign * (8 * A) / (np.pi**2 * n**2)
                Sinn = np.sin(n * w0 * t)
                wave_list.append(An * Sinn)
                
            amplitude_spectrum.append(abs(An))
                
    elif mode == 'square':
        for n in range(1, N + 1):
            n_indexes.append(n)
            if n % 2 == 0:
                wave_list.append(np.zeros_like(t))
                An = 0.0
            else:
                An = (4 * A) / (np.pi * n)
                Sinn = np.sin(n * w0 * t)
                wave_list.append(An * Sinn)
                
            amplitude_spectrum.append(abs(An))
                
    return wave_list

def sum_waves(wave_list):
    x_t = np.sum(wave_list, axis=0)
    return x_t