import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#===============================
# CREACION DEL DATASET
#===============================
data = {
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora', 'Tablet', 'Cámara', 'Altavoz'],
    'Precio': [1200, 25, 80, 300, 150, 400, 200, 120],
    'Cantidad': [10, 50, 30, 15, 8, 20, 12, 25],
    'Ciudad': ['Lima', 'Lima', 'Bogotá', 'Lima', 'Bogotá', 'Santiago', 'Santiago', 'Lima']
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame completo
print("DataFrame original:")
print(df)

#===============================
#MANIPULACION DE DATOS CON PANDAS
#===============================
# Crear la columna 'Ventas'
df['Ventas'] = df['Precio'] * df['Cantidad']

# Mostrar el DataFrame actualizado
print("\nDataFrame con columna Ventas:")
print(df)

# Calcular estadísticas
promedio_ventas = df['Ventas'].mean()
venta_max = df['Ventas'].max()
venta_min = df['Ventas'].min()
suma_total_ventas = df['Ventas'].sum()
ventas_por_ciudad = df.groupby('Ciudad')['Ventas'].sum()

print(f"\nEstadísticas de Ventas:")
print(f"Promedio de ventas: {promedio_ventas:.2f}")
print(f"Venta máxima: {venta_max}")
print(f"Venta mínima: {venta_min}")
print(f"Suma total de ventas: {suma_total_ventas}")
print(f"\nVentas por ciudad: \n{ventas_por_ciudad}")


#===============================
# FILTRADO DE DATOS
#===============================
# Filtrar ventas en Lima
print("\nVentas en Lima:")
print(df[df['Ciudad'] == 'Lima'])

# Productos con ventas > 3000
print("\nProductos con ventas mayores a 3000:")
print(df[df['Ventas'] > 3000])

# Productos con cantidad vendida > 20
print("\nProductos con cantidad vendida mayor a 20:")
print(df[df['Cantidad'] > 20])

#===============================
#CALCULOS CON NUMPY
#===============================
# Convertir columna Ventas a array de NumPy
ventas_array = np.array(df['Ventas'])

# Cálculos con NumPy
media = np.mean(ventas_array)
desviacion = np.std(ventas_array)
maximo = np.max(ventas_array)
minimo = np.min(ventas_array)

print("\nCálculos con NumPy:")
print(f"Media: {media:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")
print(f"Valor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")

#===============================
#VISUALIZACION DE DATOS CON MATPLOTLIB
#===============================
# Gráfico de Barras: Ventas por producto
plt.figure(figsize=(10, 8))
plt.bar(df['Producto'], df['Ventas'], color='skyblue')
plt.title('Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.xticks(rotation=45)
plt.savefig('Barras.png')  # Guardar el gráfico de barras
plt.show()

# Gráfico de Línea: Cantidad vendida por producto
plt.figure(figsize=(10, 8))
plt.plot(df['Producto'], df['Cantidad'], marker='o', color='green')
plt.title('Cantidad Vendida por Producto')
plt.xlabel('Producto')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('Lineal.png')  # Guardar el gráfico de línea
plt.show()

# Gráfico de Pastel: Distribución de ventas por ciudad
ventas_por_ciudad = df.groupby('Ciudad')['Ventas'].sum()
plt.figure(figsize=(10, 8))
plt.pie(ventas_por_ciudad, labels=ventas_por_ciudad.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Ventas por Ciudad')
plt.savefig('Pastel.png')  # Guardar el gráfico de pastel
plt.show()

#===============================
#DATA SET MAS GRANDE
#===============================
np.random.seed(42)
productos = [f'Producto_{i}' for i in range(1, 11)]
ciudades = ['Lima', 'Bogotá', 'Santiago', 'Quito', 'Asunción']
regiones = [f'Región_{i}' for i in range(1, 31)]

data_grande = {
    'Producto': np.random.choice(productos, 100),
    'Precio': np.random.randint(50, 1000, 100),
    'Cantidad': np.random.randint(1, 50, 100),
    'Ciudad': np.random.choice(ciudades, 100),
    'Región': np.random.choice(regiones, 100)
}

df_grande = pd.DataFrame(data_grande)
df_grande['Ventas'] = df_grande['Precio'] * df_grande['Cantidad']

# Histograma de ventas
plt.figure(figsize=(10, 8))
plt.hist(df_grande['Ventas'], bins=20, color='purple', edgecolor='black')
plt.title('Histograma de Ventas')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')
plt.savefig('Histograma.png')  # Guardar el histograma
plt.show()

# Gráfico de dispersión: Precio vs Cantidad
plt.figure(figsize=(10, 8))
plt.scatter(df_grande['Precio'], df_grande['Cantidad'], alpha=0.6, color='red')
plt.title('Relación entre Precio y Cantidad Vendida')
plt.xlabel('Precio')
plt.ylabel('Cantidad')
plt.grid(True)
plt.savefig('Dispersion.png')  # Guardar el gráfico de dispersión
plt.show()

# Gráfico de calor: Ventas por Ciudad y Región
ventas_ciudad_region = df_grande.pivot_table(values='Ventas', index='Ciudad', columns='Región', aggfunc='sum', fill_value=0)
plt.figure(figsize=(12, 8))
plt.imshow(ventas_ciudad_region, cmap='YlOrRd', aspect='auto')
plt.xticks(range(len(ventas_ciudad_region.columns)), ventas_ciudad_region.columns, rotation=45)
plt.yticks(range(len(ventas_ciudad_region.index)), ventas_ciudad_region.index)
plt.title('Ventas por Ciudad y Región')
plt.xlabel('Región')
plt.ylabel('Ciudad')
plt.colorbar(label='Ventas Totales')
plt.savefig('Calor.png')  # Guardar el gráfico de calor
plt.show()
