# Часть 1 Подключение датасета
import matplotlib.pyplot as pltimport pandas as pdimport numpy as np
# Загрузка датасета
df = pd.read_csv('21 fridges.csv')
# Информация о датасете
print("Размер датасета:", df.shape)
print("\nСтолбцы:", df.columns)
print("\nПервые строки:")print(df.head())
# Часть 2 Визуализация данных# ===== ЛИНЕЙНЫЙ ГРАФИК (Price) =====
plt.figure()plt.title('Цена холодильников', fontsize=15)plt.ylabel('Цена')plt.xlabel('Номер записи')plt.plot(np.sort(df['Price']))plt.show()
# ===== ГИСТОГРАММА (Brand) =====
plt.figure()plt.title('Распределение по брендам', fontsize=15)plt.xlabel('Бренд')plt.ylabel('Количество')brand_counts = df['Brand'].value_counts()plt.bar(brand_counts.index, brand_counts.values)plt.xticks(rotation=45)plt.show()
# ===== КРУГОВАЯ ДИАГРАММА =====
plt.figure()plt.title('Доли брендов')plt.pie(brand_counts.values, labels=brand_counts.index, autopct='%1.1f%%')plt.show()
# ===== ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ (scatter) =====
print("\nБренды:", df['Brand'].unique())
# выбираем числовые столбцы
numeric_cols = df.select_dtypes(include=np.number).columns
# убираем 
Pricenumeric_cols = [col for col in numeric_cols if col != 'Price']
# берем первые 5 столбцов
cols_to_plot = numeric_cols[:5]brands = df['Brand'].unique()for col in cols_to_plot:    plt.figure()    plt.title(f'{col} по брендам')    for brand in brands:        subset = df[df['Brand'] == brand]        plt.scatter(subset.index, subset[col], label=brand)    plt.xlabel('Индекс')    plt.ylabel(col)    plt.legend()    plt.show()
