```python
import pandas as pd
import numpy as np
data = pd.read_csv('C:/Users/grzeg/PycharmProjects/PAD/Projekt/messy_data.csv')
```

# Dane - pierwsze 5 wierszy


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>carat</th>
      <th>clarity</th>
      <th>color</th>
      <th>cut</th>
      <th>x dimension</th>
      <th>y dimension</th>
      <th>z dimension</th>
      <th>depth</th>
      <th>table</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.5</td>
      <td>IF</td>
      <td>D</td>
      <td>Ideal</td>
      <td>5.1</td>
      <td>5.15</td>
      <td>3.2</td>
      <td>61.5</td>
      <td></td>
      <td>3000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.7</td>
      <td>vvs2</td>
      <td>E</td>
      <td>premium</td>
      <td>5.7</td>
      <td></td>
      <td>3.52</td>
      <td>62</td>
      <td>59</td>
      <td>4500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>Si2</td>
      <td>h</td>
      <td>Good</td>
      <td>4.3</td>
      <td>4.31</td>
      <td></td>
      <td>62.3</td>
      <td>56</td>
      <td>700</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.2</td>
      <td>if</td>
      <td>d</td>
      <td>ideal</td>
      <td></td>
      <td>6.82</td>
      <td>4.2</td>
      <td>61.7</td>
      <td>58</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.9</td>
      <td>I1</td>
      <td>J</td>
      <td>Fair</td>
      <td>6</td>
      <td></td>
      <td>3.7</td>
      <td>61.7</td>
      <td></td>
      <td>2400</td>
    </tr>
  </tbody>
</table>
</div>



# Analiza danych - kolumny

- **carat**: Liczba karatów w danym wyrobie. Typ zmiennoprzecinkowy, zawiera puste wiersze
- **clarity**: Przejrzystość/czystość wyrobu - kategoria. Wymaga ujednolicenia
- **color**: Kolor - kategoria. Wymaga ujednolicenia
- **cut**: Szlif - kategoria. Wymaga ujednolicenia
- **x/y/z dimension**: Wymiary. Typ zmiennoprzecinkowy, zawiera puste wiersze
- **depth**: Głębokość. Typ zmiennoprzecinkowy, zawiera puste wiersze
- **table**: Płaska górna powierzchnia diamentu. Typ int, zawiera puste wiersze
- **price**: Cena wyrobu. Typ int, zawiera puste wiersze

# Czyszczenie i ujednolicenie danych

## Nazwy kolumn


```python
# w nazwach kolumn są białe znaki
data.columns = data.columns.str.strip()
data.columns
```




    Index(['carat', 'clarity', 'color', 'cut', 'x dimension', 'y dimension',
           'z dimension', 'depth', 'table', 'price'],
          dtype='object')



## Kolumna clarity


```python
clarity_categories = set(data['clarity'])
clarity_categories

# W nazwach są białe znaki
data['clarity'] = data['clarity'].str.strip()

clarity_categories = set(data['clarity'])
clarity_categories
```




    {'I1',
     'IF',
     'SI2',
     'Si1',
     'Si2',
     'VVS1',
     'VVS2',
     'Vvs1',
     'i1',
     'if',
     'si1',
     'si2',
     'vvs1',
     'vvs2'}




```python
# Mapowanie rodzajów i ustawienie typu na kategorie

mapping = {'i1': 'I1', 'if': 'IF', 'si1': 'Si1', 'si2': 'SI2','Si2': 'SI2' ,'vvs1': 'VVS1', 'Vvs1': 'VVS1', 'vvs2': 'VVS2'}
data['clarity'] = data['clarity'].replace(mapping)

clarity_categories = set(data['clarity'])
clarity_categories

data['clarity'] = data['clarity'].astype('category')
data.dtypes

```




    carat           float64
    clarity        category
    color            object
    cut              object
    x dimension      object
    y dimension      object
    z dimension      object
    depth            object
    table            object
    price            object
    dtype: object



## Kolumna **color**


```python
colors = set(data['color'])
colors

# W nazwach kolorów są białe znaki
data['color'] = data['color'].str.strip()

colors = set(data['color'])
colors
```




    {'Colorless',
     'D',
     'E',
     'F',
     'G',
     'H',
     'I',
     'J',
     'colorless',
     'd',
     'e',
     'f',
     'g',
     'h',
     'j'}




```python
# Mapowanie kolorów i ustawienie typu na kategorie

mapping = {'colorless': 'Colorless', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'j': 'J'}
data['color'] = data['color'].replace(mapping)

colors = set(data['color'])
colors

data['color'] = data['color'].astype('category')
data.dtypes
```




    carat           float64
    clarity        category
    color          category
    cut              object
    x dimension      object
    y dimension      object
    z dimension      object
    depth            object
    table            object
    price            object
    dtype: object



## Kolumna cut


```python
cut_categories = set(data['cut'])

# W nazwach są białe znaki
data['cut'] = data['cut'].str.strip()

cut_categories = set(data['cut'])
cut_categories
```




    {'Fair',
     'Good',
     'Ideal',
     'Premium',
     'Very Good',
     'Very good',
     'fair',
     'good',
     'ideal',
     'premium',
     'very Good',
     'very good'}




```python
# Mapowanie szlifów i ustawienie typu na kategorie

mapping = {'fair': 'Fair', 'good': 'Good', 'ideal': 'Ideal', 'premium': 'Premium', 'very good': 'Very Good', 'Very good': 'Very Good', 'very Good': 'Very Good'}
data['cut'] = data['cut'].replace(mapping)

cut_categories = set(data['cut'])
cut_categories

data['cut'] = data['cut'].astype('category')
data.dtypes
```




    carat           float64
    clarity        category
    color          category
    cut            category
    x dimension      object
    y dimension      object
    z dimension      object
    depth            object
    table            object
    price            object
    dtype: object




```python
#Ustawienie typu danych dla reszty kolumn

cols_with_empty_strings = data.columns[data.apply(lambda col: col == ' ').any()]
data[cols_with_empty_strings] = data[cols_with_empty_strings].replace(' ', np.nan)

data['x dimension'] = data['x dimension'].astype(float)
data['y dimension'] = data['y dimension'].astype(float)
data['z dimension'] = data['z dimension'].astype(float)
data['depth'] = data['depth'].astype(float)
data['table'] = data['table'].astype('Int32')
data['price'] = data['price'].astype('Int32')

data.dtypes

```




    carat           float64
    clarity        category
    color          category
    cut            category
    x dimension     float64
    y dimension     float64
    z dimension     float64
    depth           float64
    table             Int32
    price             Int32
    dtype: object




```python
data.head(15)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>carat</th>
      <th>clarity</th>
      <th>color</th>
      <th>cut</th>
      <th>x dimension</th>
      <th>y dimension</th>
      <th>z dimension</th>
      <th>depth</th>
      <th>table</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.50</td>
      <td>IF</td>
      <td>D</td>
      <td>Ideal</td>
      <td>5.1</td>
      <td>5.15</td>
      <td>3.20</td>
      <td>61.5</td>
      <td>&lt;NA&gt;</td>
      <td>3000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.70</td>
      <td>VVS2</td>
      <td>E</td>
      <td>Premium</td>
      <td>5.7</td>
      <td>NaN</td>
      <td>3.52</td>
      <td>62.0</td>
      <td>59</td>
      <td>4500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>SI2</td>
      <td>H</td>
      <td>Good</td>
      <td>4.3</td>
      <td>4.31</td>
      <td>NaN</td>
      <td>62.3</td>
      <td>56</td>
      <td>700</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.20</td>
      <td>IF</td>
      <td>D</td>
      <td>Ideal</td>
      <td>NaN</td>
      <td>6.82</td>
      <td>4.20</td>
      <td>61.7</td>
      <td>58</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.90</td>
      <td>I1</td>
      <td>J</td>
      <td>Fair</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>3.70</td>
      <td>61.7</td>
      <td>&lt;NA&gt;</td>
      <td>2400</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>Si1</td>
      <td>G</td>
      <td>Very Good</td>
      <td>5.9</td>
      <td>5.92</td>
      <td>3.63</td>
      <td>NaN</td>
      <td>57</td>
      <td>4200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.50</td>
      <td>IF</td>
      <td>D</td>
      <td>Ideal</td>
      <td>5.1</td>
      <td>NaN</td>
      <td>3.20</td>
      <td>61.5</td>
      <td>57</td>
      <td>3100</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.40</td>
      <td>VVS1</td>
      <td>F</td>
      <td>Good</td>
      <td>4.8</td>
      <td>4.79</td>
      <td>2.95</td>
      <td>NaN</td>
      <td>&lt;NA&gt;</td>
      <td>1500</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>SI2</td>
      <td>I</td>
      <td>Good</td>
      <td>4.3</td>
      <td>4.32</td>
      <td>NaN</td>
      <td>62.3</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.00</td>
      <td>VVS1</td>
      <td>F</td>
      <td>Ideal</td>
      <td>6.4</td>
      <td>NaN</td>
      <td>4.00</td>
      <td>NaN</td>
      <td>58</td>
      <td>7500</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.50</td>
      <td>Si1</td>
      <td>Colorless</td>
      <td>Premium</td>
      <td>NaN</td>
      <td>5.21</td>
      <td>3.21</td>
      <td>61.6</td>
      <td>58</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.40</td>
      <td>VVS2</td>
      <td>G</td>
      <td>Very Good</td>
      <td>4.9</td>
      <td>4.88</td>
      <td>NaN</td>
      <td>61.2</td>
      <td>56</td>
      <td>1400</td>
    </tr>
    <tr>
      <th>12</th>
      <td>NaN</td>
      <td>SI2</td>
      <td>J</td>
      <td>Fair</td>
      <td>5.7</td>
      <td>5.71</td>
      <td>3.54</td>
      <td>NaN</td>
      <td>54</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.10</td>
      <td>VVS1</td>
      <td>E</td>
      <td>Premium</td>
      <td>6.6</td>
      <td>NaN</td>
      <td>4.08</td>
      <td>NaN</td>
      <td>57</td>
      <td>9200</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.55</td>
      <td>SI2</td>
      <td>H</td>
      <td>Good</td>
      <td>5.3</td>
      <td>5.29</td>
      <td>NaN</td>
      <td>62.0</td>
      <td>&lt;NA&gt;</td>
      <td>1800</td>
    </tr>
  </tbody>
</table>
</div>



# Usuwanie wierszy z brakującymi danymi


```python
# Postanowiłem usunąć wiersze gdzie carat jest nan. 
# Myślę, że jest to największy czynnik który ma wpływ na cene wyrobu
# Zmniejszy to rozmiar danych o 50 wierszy ale dane będą dokładniejsze
count = data['carat'].isna().sum()
data = data.dropna(subset=['carat'])

# Brakujące dane w kolumnie price postanowiłem zamienić średnią z wierszy o podobnych wartościach (carat i cut jest taki sam)
# Zobaczmy ile jest wierszy gdzie carat i cut jest taki sam - 82
size = len(data.groupby(['carat', 'cut'], observed=True))
size
```




    82




```python
# Ilosc wierszy bez ceny
price_na_data = data[data['price'].isna()]
print(len(price_na_data)) 
```

    2
    




```python
# Wyswietlmy wiersze gdzie price jest nan oraz wiersze z takim samym carat i cut
matched_data = pd.merge(data,price_na_data[['carat', 'cut']], on=['carat', 'cut'])
matched_data 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>carat</th>
      <th>clarity</th>
      <th>color</th>
      <th>cut</th>
      <th>x dimension</th>
      <th>y dimension</th>
      <th>z dimension</th>
      <th>depth</th>
      <th>table</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>VVS1</td>
      <td>F</td>
      <td>Ideal</td>
      <td>6.4</td>
      <td>NaN</td>
      <td>4.00</td>
      <td>NaN</td>
      <td>58</td>
      <td>7500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.5</td>
      <td>Si1</td>
      <td>Colorless</td>
      <td>Premium</td>
      <td>NaN</td>
      <td>5.21</td>
      <td>3.21</td>
      <td>61.6</td>
      <td>58</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>IF</td>
      <td>D</td>
      <td>Ideal</td>
      <td>6.5</td>
      <td>6.49</td>
      <td>NaN</td>
      <td>61.7</td>
      <td>58</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.5</td>
      <td>VVS1</td>
      <td>E</td>
      <td>Premium</td>
      <td>5.2</td>
      <td>5.22</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>58</td>
      <td>2900</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.5</td>
      <td>VVS2</td>
      <td>F</td>
      <td>Premium</td>
      <td>5.2</td>
      <td>5.23</td>
      <td>NaN</td>
      <td>62.1</td>
      <td>58</td>
      <td>3200</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.5</td>
      <td>Si1</td>
      <td>H</td>
      <td>Premium</td>
      <td>5.1</td>
      <td>NaN</td>
      <td>3.16</td>
      <td>62.3</td>
      <td>57</td>
      <td>3000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.5</td>
      <td>SI2</td>
      <td>E</td>
      <td>Premium</td>
      <td>5.1</td>
      <td>5.11</td>
      <td>NaN</td>
      <td>62.5</td>
      <td>55</td>
      <td>2900</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Liczba wierszy z cena oraz z takim samym cut i caratem
print(len(matched_data[~matched_data['price'].isna()])) # 5
```

    5
    


```python
mean_prices = data.groupby(['carat', 'cut'], observed=True)['price'].mean().reset_index(name='mean_price')
merged_data = pd.merge(data, mean_prices, on=['carat', 'cut'], how='left')
merged_data['mean_price'] = merged_data['mean_price'].astype('Int32')
price_nan_mask_merged = merged_data['price'].isna()
merged_data['price'] = merged_data['price'].fillna(merged_data['mean_price']) # inplace=true dawalo warning 
merged_data[price_nan_mask_merged]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>carat</th>
      <th>clarity</th>
      <th>color</th>
      <th>cut</th>
      <th>x dimension</th>
      <th>y dimension</th>
      <th>z dimension</th>
      <th>depth</th>
      <th>table</th>
      <th>price</th>
      <th>mean_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>0.5</td>
      <td>Si1</td>
      <td>Colorless</td>
      <td>Premium</td>
      <td>NaN</td>
      <td>5.21</td>
      <td>3.21</td>
      <td>61.6</td>
      <td>58</td>
      <td>3000</td>
      <td>3000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1.0</td>
      <td>IF</td>
      <td>D</td>
      <td>Ideal</td>
      <td>6.5</td>
      <td>6.49</td>
      <td>NaN</td>
      <td>61.7</td>
      <td>58</td>
      <td>7500</td>
      <td>7500</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = merged_data.drop(columns=['mean_price'])
data[price_nan_mask_merged]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>carat</th>
      <th>clarity</th>
      <th>color</th>
      <th>cut</th>
      <th>x dimension</th>
      <th>y dimension</th>
      <th>z dimension</th>
      <th>depth</th>
      <th>table</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>0.5</td>
      <td>Si1</td>
      <td>Colorless</td>
      <td>Premium</td>
      <td>NaN</td>
      <td>5.21</td>
      <td>3.21</td>
      <td>61.6</td>
      <td>58</td>
      <td>3000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1.0</td>
      <td>IF</td>
      <td>D</td>
      <td>Ideal</td>
      <td>6.5</td>
      <td>6.49</td>
      <td>NaN</td>
      <td>61.7</td>
      <td>58</td>
      <td>7500</td>
    </tr>
  </tbody>
</table>
</div>



# Duplikaty


```python
 data.duplicated().sum()
# Nie ma wierszy identycznych

# Sprawdzmy duplikaty biorąc pod uwage ponizsze kolumny
duplicates = data.duplicated(subset=['carat', 'cut', 'clarity', 'x dimension', 'y dimension', 'z dimension'], keep=False)
data[duplicates]

# Znaleziono tylko 2 rekordy, cena moze sie roznic ze wzgledu na kolor

# Wyglada na to ze zbior po wstepnym oczyszczeniu nie ma duplikatow 

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>carat</th>
      <th>clarity</th>
      <th>color</th>
      <th>cut</th>
      <th>x dimension</th>
      <th>y dimension</th>
      <th>z dimension</th>
      <th>depth</th>
      <th>table</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>53</th>
      <td>1.2</td>
      <td>VVS1</td>
      <td>E</td>
      <td>Premium</td>
      <td>6.8</td>
      <td>NaN</td>
      <td>4.2</td>
      <td>62.7</td>
      <td>58</td>
      <td>10200</td>
    </tr>
    <tr>
      <th>102</th>
      <td>1.2</td>
      <td>VVS1</td>
      <td>G</td>
      <td>Premium</td>
      <td>6.8</td>
      <td>NaN</td>
      <td>4.2</td>
      <td>NaN</td>
      <td>58</td>
      <td>10100</td>
    </tr>
  </tbody>
</table>
</div>



# Błędne dane


```python
# Po obejrzeniu wykresów z rozkładem zmiennych zauważyłem, że 4 wiersze znacząco odbiegają od reszty
data = data.sort_values(by='price', ascending=False)
data.head(3)

# Tak jak wcześniej, zamienie ceny na średnią cen z podobnych rekordów (carat + cut)
# Najpierw zamienie te ceny na nan 
data.loc[data['price'] > 12000, 'price'] = np.nan

mean_prices = data.groupby(['carat', 'cut'], observed=True)['price'].mean().reset_index(name='mean_price')
merged_data = pd.merge(data, mean_prices, on=['carat', 'cut'], how='left')
merged_data['mean_price'] = merged_data['mean_price'].astype('Int32')

merged_data_na_price_mask = merged_data['price'].isna()

merged_data['price'] = merged_data['price'].fillna(merged_data['mean_price']) # inplace=true dawalo warning 

# Po ponownym obejrzeniu wykresu zauważyłem poniższy rekord, którego cena znacząco odbiega od normy
# Jako że nie ma innych wierszy z caratem równym 1.6 na razie go usune
cleaned_data = merged_data[merged_data['carat'] != 1.6]
```


```python
data = cleaned_data.drop(columns=['mean_price'])
data[merged_data_na_price_mask]
```

    C:\Users\grzeg\AppData\Local\Temp\ipykernel_26228\1991026144.py:2: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
      data[merged_data_na_price_mask]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>carat</th>
      <th>clarity</th>
      <th>color</th>
      <th>cut</th>
      <th>x dimension</th>
      <th>y dimension</th>
      <th>z dimension</th>
      <th>depth</th>
      <th>table</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.40</td>
      <td>SI2</td>
      <td>D</td>
      <td>Very Good</td>
      <td>7.3</td>
      <td>NaN</td>
      <td>4.50</td>
      <td>62.6</td>
      <td>59</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.90</td>
      <td>IF</td>
      <td>G</td>
      <td>Very Good</td>
      <td>6.3</td>
      <td>NaN</td>
      <td>3.90</td>
      <td>NaN</td>
      <td>57</td>
      <td>6700</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.55</td>
      <td>I1</td>
      <td>I</td>
      <td>Premium</td>
      <td>5.3</td>
      <td>NaN</td>
      <td>3.28</td>
      <td>62.3</td>
      <td>57</td>
      <td>2500</td>
    </tr>
  </tbody>
</table>
</div>



# Zapisanie danych


```python
data.to_csv('prepared_data.csv',index=False)
```
