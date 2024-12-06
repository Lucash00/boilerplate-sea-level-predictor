import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Leer datos desde el archivo
    data = pd.read_csv('epa-sea-level.csv')
    
    # Crear gráfico de dispersión
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', s=10, label='Data')
    
    # Primera línea de mejor ajuste
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels = intercept + slope * years_extended
    plt.plot(years_extended, sea_levels, color='red', label='Best fit line (1880-2050)')
    
    # Segunda línea de mejor ajuste
    data_2000 = data[data['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(data_2000['Year'], data_2000['CSIRO Adjusted Sea Level'])
    years_extended_2000 = pd.Series(range(2000, 2051))
    sea_levels_2000 = intercept_2000 + slope_2000 * years_extended_2000
    plt.plot(years_extended_2000, sea_levels_2000, color='green', label='Best fit line (2000-2050)')
    
    # Añadir etiquetas y título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Guardar y retornar el gráfico
    plt.savefig('sea_level_plot.png')
    return plt.gca()
