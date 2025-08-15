import math
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import offsetbox
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.figure_factory as ff
#import session_info
from time import time
from plotly.subplots import make_subplots
from sklearn import set_config
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

def generate_contrast_colors(n):
    base_colors = [
        '#FF6384',  # Rosa
        '#36A2EB',  # Azul
        '#FFCE56',  # Amarillo
        '#4BC0C0',  # Turquesa
        '#9966FF',  # Violeta
        '#FF9F40',  # Naranja
        '#C9CBCF',  # Gris claro
        '#7E57C2',  # Púrpura
        '#D4E157',  # Lima
        '#66BB6A',  # Verde
    ]
    
    if n <= len(base_colors):
        return base_colors[:n]
    else:
        # Si necesitamos más colores que los base, repetimos la lista
        colors = base_colors * (n // len(base_colors)) + base_colors[:n % len(base_colors)]
        return colors

def plot_embedding(X, y, title):
    
    # Escalamiento
    X_scaled = MinMaxScaler().fit_transform(X)

    fig = go.Figure()
    unique_digits = np.unique(y)
    colors = generate_contrast_colors(len(unique_digits))

    for digit in unique_digits:
        fig.add_trace(go.Scatter(
            x=X_scaled[y == digit, 0], 
            y=X_scaled[y == digit, 1],
            mode='markers',
            marker=dict(
                size=8,
                color=colors[digit],
                opacity=0.5,
            ),
            name=f'Digit {digit}'
        ))

    fig.update_layout(
        title=title,
        xaxis_title="C1",
        yaxis_title="C2",
        legend_title="Dígito",
        showlegend=True
    )

    fig.show()
    
def score_plot(scores, range_n_clusters, operator, name_index):
    # Encontrar el número de conglomerados con la mejor puntuación
    clusters = list(range_n_clusters)

    if operator == 'max':
        operator = max(scores)
    elif operator == 'min':
        operator = min(scores)
        
    best_index = clusters[scores.index(operator)]
    best_score = max(scores)

    # Crear el gráfico de líneas para las puntuaciones
    fig = go.Figure()

    # Añadir la línea de puntuación
    fig.add_trace(go.Scatter(x=clusters, y=scores, mode='lines+markers', name=name_index))

    # Añade una línea de puntos para la mejor puntuación
    fig.add_trace(go.Scatter(x=[best_index, best_index], y=[0, best_score], mode='lines', name='Mejor Índice',
                            line=dict(color='red', width=2, dash='dot')))

    # Actualizar layout
    fig.update_layout(height=500, width=1200, title_text="",
                    xaxis_title='Número de Clusters',
                    yaxis_title=name_index,
                    showlegend=True)
    fig.show()
    
    
def calculate_elbow_point(distortions):
    n_points = len(distortions)
    all_coords = np.vstack((range(n_points), distortions)).T
    first_point = all_coords[0]
    line_vec = all_coords[-1] - all_coords[0]
    line_vec_norm = line_vec / np.sqrt(np.sum(line_vec**2))
    vec_from_first = all_coords - first_point
    scalar_product = np.sum(vec_from_first * np.tile(line_vec_norm, (n_points, 1)), axis=1)
    vec_from_first_parallel = np.outer(scalar_product, line_vec_norm)
    vec_to_line = vec_from_first - vec_from_first_parallel
    dist_to_line = np.sqrt(np.sum(vec_to_line ** 2, axis=1))
    return dist_to_line.argmax() + 1  # +1 para ajustar el índice al número real de clusters

def plot_elbow_method(no_clusters, distortions, optimal_k):
    
    # Crear el gráfico de líneas para las puntuaciones
    fig = go.Figure(data=go.Scatter(x=list(no_clusters), y=distortions, mode='lines+markers', 
                                        marker=dict(color='RoyalBlue'), name='Distorsión por K'))

    # Añade una línea de puntos para la mejor puntuación
    fig.add_trace(go.Scatter(x=[optimal_k, optimal_k], y=[0, max(distortions)], mode='lines', 
                                line=dict(color='Red', dash='dash'), name='Punto del Codo'))

    # Actualizar layout
    fig.update_layout(title='Método del Codo',
                        xaxis_title='Número de Clusters (K)',
                        yaxis_title='Distorsión', height=500, width=1200)
    fig.show()

def calculate_kn_distance(X, k=2):
    # Definimos la función para calcular la distancia al k-ésimo vecino más cercano
    neigh = NearestNeighbors(n_neighbors=k)
    nbrs = neigh.fit(X)
    distances, _ = nbrs.kneighbors(X)
    return distances[:, k-1]

def plot_kn_distance(X, k):
    # Definimos la función para trazar la curva de la distancia al k-ésimo vecino más cercano
    distances = calculate_kn_distance(X, k=k)
    distances = np.sort(distances, axis=0)
    
    # Crear el gráfico de codo
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(1, len(distances)+1)), y=distances,
                                mode='lines+markers',
                                name='Curva de distancia k'))
    fig.update_layout(title='Curva de distancia k',
                        xaxis_title='Puntos Ordenados por Distancia',
                        yaxis_title=f'Distancia al {k}-ésimo vecino más próximo',
                        showlegend=False)
    fig.show()