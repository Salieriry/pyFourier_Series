# Visualizador da Série de Fourier

Um script Python para calcular e visualizar a Série de Fourier de formas de onda. Este projeto demonstra como ondas quadradas ou triangulares são formadas pela soma de ondas senoidais simples (harmônicos).

## Funcionalidades

-   Calcula os harmônicos da Série de Fourier para os modos 'square' (quadrada) e 'triangular'.
    
-   Gera múltiplas visualizações dos harmônicos e da onda resultante.
    
-   Plota os 20 primeiros harmônicos em uma grade 5x4.
    
-   Plota os harmônicos ímpares sobrepostos em um único gráfico.
    
-   Exibe a soma final de todos os harmônicos (a onda reconstruída).
    
-   Mostra o espectro de amplitude dos harmônicos.
    

## Requisitos

-   Python 3.12.3
    
-   As bibliotecas listadas em `requirements.txt`, principalmente:
    
    -   `numpy`
        
    -   `matplotlib`
        

## Como Usar

1.  Clone este repositório.
    
2.  Crie e ative um ambiente virtual:
    
    Bash
    
    ```
    python -m venv venv
    source venv/bin/activate 
    # ou .\venv\Scripts\activate no Windows
    
    ```
    
3.  Instale as dependências:
    
    Bash
    
    ```
    pip install -r requirements.txt
    
    ```
    
4.  Execute o script principal:
    
    Bash
    
    ```
    python main.py
    
    ```
    

Ao executar, o script abrirá 5 janelas de gráfico sequencialmente. É preciso fechar cada janela para que a próxima apareça.

Para alterar a forma de onda, edite o `main.py` e mude `'square'` para `'triangular'` na chamada da função `fourier_series`.


