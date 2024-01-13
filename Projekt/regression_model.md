```python
import statsmodels.formula.api as smf
import pandas as pd
```


```python
data = pd.read_csv('prepared_data.csv')
```


```python
data.columns
```




    Index(['carat', 'clarity', 'color', 'cut', 'x dimension', 'y dimension',
           'z dimension', 'depth', 'table', 'price'],
          dtype='object')



# Hipoteza zerowa

- H0: $\beta_1 = 0$. Nie ma dowodów na wzrost ceny
- Ha: $\beta_1 \neq 0$. Istnieją dowody na wzrost cen


```python
model = smf.ols("price ~ carat + clarity + color + cut + depth + table", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.977
    Model:                            OLS   Adj. R-squared:                  0.969
    Method:                 Least Squares   F-statistic:                     127.3
    Date:                Sat, 13 Jan 2024   Prob (F-statistic):           1.22e-39
    Time:                        19:27:55   Log-Likelihood:                -590.64
    No. Observations:                  77   AIC:                             1221.
    Df Residuals:                      57   BIC:                             1268.
    Df Model:                          19                                         
    Covariance Type:            nonrobust                                         
    ====================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------------
    Intercept        -2.057e+04   1.78e+04     -1.158      0.252   -5.61e+04     1.5e+04
    clarity[T.IF]     1354.5084    411.172      3.294      0.002     531.150    2177.867
    clarity[T.SI2]     476.9858    294.259      1.621      0.111    -112.258    1066.230
    clarity[T.Si1]     802.3826    297.566      2.696      0.009     206.518    1398.248
    clarity[T.VVS1]   1004.0284    326.613      3.074      0.003     349.998    1658.059
    clarity[T.VVS2]   1027.1969    324.878      3.162      0.003     376.639    1677.755
    color[T.D]         317.2362    438.730      0.723      0.473    -561.305    1195.778
    color[T.E]         402.9128    408.577      0.986      0.328    -415.249    1221.075
    color[T.F]         308.5999    374.103      0.825      0.413    -440.528    1057.728
    color[T.G]         135.8373    383.634      0.354      0.725    -632.376     904.051
    color[T.H]         255.1629    383.669      0.665      0.509    -513.121    1023.447
    color[T.I]         217.5268    369.985      0.588      0.559    -523.354     958.408
    color[T.J]        -588.1625    756.610     -0.777      0.440   -2103.249     926.924
    cut[T.Good]       -640.8511    247.017     -2.594      0.012   -1135.495    -146.207
    cut[T.Ideal]       -23.9625    285.055     -0.084      0.933    -594.775     546.850
    cut[T.Premium]     108.3973    259.467      0.418      0.678    -411.177     627.971
    cut[T.Very Good]   -57.3889    256.673     -0.224      0.824    -571.368     456.590
    carat             9474.3198    268.053     35.345      0.000    8937.552       1e+04
    depth              247.0485    280.926      0.879      0.383    -315.496     809.593
    table               38.4212     57.414      0.669      0.506     -76.549     153.392
    ==============================================================================
    Omnibus:                        0.971   Durbin-Watson:                   1.663
    Prob(Omnibus):                  0.615   Jarque-Bera (JB):                0.433
    Skew:                           0.073   Prob(JB):                        0.806
    Kurtosis:                       3.337   Cond. No.                     2.18e+04
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 2.18e+04. This might indicate that there are
    strong multicollinearity or other numerical problems.
    

# Usuńmy kolumny table oraz depth ze współczynników (0.402 oraz 0.541)


```python
model = smf.ols("price ~ carat + clarity + color + cut", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.972
    Model:                            OLS   Adj. R-squared:                  0.968
    Method:                 Least Squares   F-statistic:                     265.9
    Date:                Sat, 13 Jan 2024   Prob (F-statistic):           1.09e-92
    Time:                        19:27:55   Log-Likelihood:                -1148.7
    No. Observations:                 149   AIC:                             2333.
    Df Residuals:                     131   BIC:                             2387.
    Df Model:                          17                                         
    Covariance Type:            nonrobust                                         
    ====================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------------
    Intercept        -3505.2750    332.989    -10.527      0.000   -4164.007   -2846.543
    clarity[T.IF]     1144.9904    227.446      5.034      0.000     695.048    1594.933
    clarity[T.SI2]     422.8493    185.657      2.278      0.024      55.576     790.122
    clarity[T.Si1]     671.7661    192.023      3.498      0.001     291.899    1051.633
    clarity[T.VVS1]    896.1456    202.002      4.436      0.000     496.538    1295.753
    clarity[T.VVS2]    894.7953    199.175      4.493      0.000     500.779    1288.811
    color[T.D]         558.8829    307.152      1.820      0.071     -48.737    1166.503
    color[T.E]         516.1640    301.650      1.711      0.089     -80.572    1112.900
    color[T.F]         611.5971    275.899      2.217      0.028      65.804    1157.390
    color[T.G]         410.6657    270.262      1.520      0.131    -123.977     945.309
    color[T.H]         375.6453    282.350      1.330      0.186    -182.910     934.200
    color[T.I]         308.7077    274.895      1.123      0.263    -235.101     852.517
    color[T.J]         352.5322    337.434      1.045      0.298    -314.993    1020.057
    cut[T.Good]       -336.3771    160.306     -2.098      0.038    -653.500     -19.254
    cut[T.Ideal]        -1.4922    177.258     -0.008      0.993    -352.151     349.167
    cut[T.Premium]     378.5691    164.824      2.297      0.023      52.507     704.631
    cut[T.Very Good]    56.6331    165.596      0.342      0.733    -270.956     384.222
    carat             9904.1840    154.834     63.967      0.000    9597.886    1.02e+04
    ==============================================================================
    Omnibus:                        3.130   Durbin-Watson:                   1.554
    Prob(Omnibus):                  0.209   Jarque-Bera (JB):                3.418
    Skew:                          -0.023   Prob(JB):                        0.181
    Kurtosis:                       3.741   Cond. No.                         22.9
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    

# Usuńmy kolumnę color (> 0.066)


```python
model = smf.ols("price ~ carat + clarity + cut", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.970
    Model:                            OLS   Adj. R-squared:                  0.968
    Method:                 Least Squares   F-statistic:                     450.9
    Date:                Sat, 13 Jan 2024   Prob (F-statistic):          4.01e-100
    Time:                        19:27:55   Log-Likelihood:                -1152.6
    No. Observations:                 149   AIC:                             2327.
    Df Residuals:                     138   BIC:                             2360.
    Df Model:                          10                                         
    Covariance Type:            nonrobust                                         
    ====================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------------
    Intercept        -3169.9458    199.840    -15.862      0.000   -3565.091   -2774.801
    clarity[T.IF]     1274.6768    210.288      6.062      0.000     858.875    1690.479
    clarity[T.SI2]     499.2032    171.496      2.911      0.004     160.104     838.302
    clarity[T.Si1]     676.2813    185.518      3.645      0.000     309.455    1043.107
    clarity[T.VVS1]    989.6259    183.947      5.380      0.000     625.906    1353.345
    clarity[T.VVS2]   1012.2759    184.183      5.496      0.000     648.090    1376.462
    cut[T.Good]       -306.5000    157.160     -1.950      0.053    -617.253       4.253
    cut[T.Ideal]        12.1677    171.926      0.071      0.944    -327.783     352.118
    cut[T.Premium]     395.2751    155.140      2.548      0.012      88.517     702.033
    cut[T.Very Good]    54.3510    160.630      0.338      0.736    -263.263     371.965
    carat             9915.4917    151.693     65.365      0.000    9615.548    1.02e+04
    ==============================================================================
    Omnibus:                        2.416   Durbin-Watson:                   1.528
    Prob(Omnibus):                  0.299   Jarque-Bera (JB):                2.287
    Skew:                           0.044   Prob(JB):                        0.319
    Kurtosis:                       3.600   Cond. No.                         11.1
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    

# Usuńmy kolumnę cut


```python
model = smf.ols("price ~ carat + clarity", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.965
    Model:                            OLS   Adj. R-squared:                  0.964
    Method:                 Least Squares   F-statistic:                     659.5
    Date:                Sat, 13 Jan 2024   Prob (F-statistic):          5.04e-101
    Time:                        19:27:55   Log-Likelihood:                -1164.1
    No. Observations:                 149   AIC:                             2342.
    Df Residuals:                     142   BIC:                             2363.
    Df Model:                           6                                         
    Covariance Type:            nonrobust                                         
    ===================================================================================
                          coef    std err          t      P>|t|      [0.025      0.975]
    -----------------------------------------------------------------------------------
    Intercept       -3083.4759    194.947    -15.817      0.000   -3468.849   -2698.102
    clarity[T.IF]    1152.7102    210.241      5.483      0.000     737.103    1568.317
    clarity[T.SI2]    366.6467    178.800      2.051      0.042      13.193     720.101
    clarity[T.Si1]    720.3231    192.770      3.737      0.000     339.254    1101.392
    clarity[T.VVS1]   902.3433    191.161      4.720      0.000     524.455    1280.232
    clarity[T.VVS2]   881.0768    191.456      4.602      0.000     502.605    1259.548
    carat            9944.5012    160.685     61.888      0.000    9626.858    1.03e+04
    ==============================================================================
    Omnibus:                        3.463   Durbin-Watson:                   1.241
    Prob(Omnibus):                  0.177   Jarque-Bera (JB):                3.395
    Skew:                          -0.178   Prob(JB):                        0.183
    Kurtosis:                       3.648   Cond. No.                         10.4
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    

# Hipoteza

Możemy odrzucić hipotezę zerową. 
Czynniki takie jak carat oraz clarity mają znaczący wpływ na wzrost ceny wyrobu.


```python
data['residuals'] = model.resid
outliers = data[abs(data['residuals']) > 3 * data['residuals'].std()]
outliers
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
      <th>residuals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>1.50</td>
      <td>VVS2</td>
      <td>F</td>
      <td>Good</td>
      <td>7.2</td>
      <td>7.18</td>
      <td>NaN</td>
      <td>62.7</td>
      <td>59.0</td>
      <td>10800</td>
      <td>-1914.352698</td>
    </tr>
    <tr>
      <th>33</th>
      <td>0.95</td>
      <td>IF</td>
      <td>D</td>
      <td>Ideal</td>
      <td>6.3</td>
      <td>NaN</td>
      <td>3.9</td>
      <td>62.6</td>
      <td>58.0</td>
      <td>9400</td>
      <td>1883.489553</td>
    </tr>
  </tbody>
</table>
</div>


