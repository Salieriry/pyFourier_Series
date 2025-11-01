import matplotlib.pyplot as plt

def plot_fourier_series(t, wave_list, n_indexes, shared_ylim=False):
    
    nrows = 5
    ncols = 4
    fig, axes = plt.subplots(nrows = nrows, ncols= ncols, figsize=(15, 12), constrained_layout=True)
    
    for n, wave, ax in zip(n_indexes, wave_list, axes.flat):
      ax.plot(t, wave)
      ax.set_title(f'Harmônico N={n}')
      if shared_ylim:
          ax.set_ylim(-0.8, 0.8)
      ax.grid(True)
      
    fig.suptitle('Série de Fourier - Harmônicos Individuais', fontsize=16)
    plt.show()
    
def plot_waves_on_same_graph(t, wave_list, n_indexes):
    plt.figure(figsize=(12, 6))
    
    for n, wave in zip(n_indexes, wave_list):
        if n%2 != 0:
            plt.plot(t, wave, label=f'N={n}')
               
    plt.title('Série de Fourier - Harmônicos no Mesmo Gráfico')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()  
    
def plot_wave_sum(t, x_t):
    
    plt.figure(figsize=(12, 6))
    plt.plot(t, x_t, color='purple')
    plt.title('Série de Fourier - Soma dos Harmônicos')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

