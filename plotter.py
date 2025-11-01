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

