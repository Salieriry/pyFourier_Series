import fourier_series as fs
import plotter as pl
import numpy as np

if __name__ == "__main__":    

    t =  np.linspace(0, 1, 1000)
    A = 1.0
    f0 = 1.0
    w0 = 2 * np.pi * f0

    wave_list = fs.fourier_series(t, A, w0, 250, 'triangular')
    wave_sum = fs.sum_waves(wave_list)

    pl.plot_fourier_series(t, wave_list, fs.n_indexes)
    pl.plot_fourier_series(t, wave_list, fs.n_indexes, True)
    pl.plot_waves_on_same_graph(t, wave_list, fs.n_indexes)
    pl.plot_wave_sum(t, wave_sum) 
    pl.plot_amplitude_spectrum(fs.n_indexes, fs.amplitude_spectrum)