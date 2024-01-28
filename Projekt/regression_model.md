```python
import statsmodels.formula.api as smf
import statsmodels.api as sm
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




```python
data.rename(columns={"x dimension": "x_dimension", "y dimension": "y_dimension", "z dimension" : "z_dimension"}, inplace=True)
```


```python
data.columns
```




    Index(['carat', 'clarity', 'color', 'cut', 'x_dimension', 'y_dimension',
           'z_dimension', 'depth', 'table', 'price'],
          dtype='object')



# Hipoteza zerowa

- H0: $\beta_1 = 0$. Nie ma dowodów na wzrost ceny
- Ha: $\beta_1 \neq 0$. Istnieją dowody na wzrost ceny


```python
# z_dimension ma za dużo wartości nan
model = smf.ols("price ~ carat + clarity + color + cut + depth + table + x_dimension + y_dimension", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.979
    Model:                            OLS   Adj. R-squared:                  0.956
    Method:                 Least Squares   F-statistic:                     42.42
    Date:                Sun, 28 Jan 2024   Prob (F-statistic):           2.96e-11
    Time:                        12:34:59   Log-Likelihood:                -292.54
    No. Observations:                  39   AIC:                             627.1
    Df Residuals:                      18   BIC:                             662.0
    Df Model:                          20                                         
    Covariance Type:            nonrobust                                         
    ====================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------------
    Intercept        -1.957e+04   3.33e+04     -0.588      0.564   -8.95e+04    5.04e+04
    clarity[T.IF]     1441.7768    849.872      1.696      0.107    -343.737    3227.291
    clarity[T.SI2]     954.1407    535.644      1.781      0.092    -171.205    2079.486
    clarity[T.Si1]     761.0637    536.910      1.417      0.173    -366.943    1889.070
    clarity[T.VVS1]   1483.5345    575.229      2.579      0.019     275.024    2692.045
    clarity[T.VVS2]   1114.2675    576.337      1.933      0.069     -96.571    2325.106
    color[T.D]         146.1050    842.639      0.173      0.864   -1624.213    1916.423
    color[T.E]        -517.4054    761.227     -0.680      0.505   -2116.683    1081.873
    color[T.F]         -40.2904    662.483     -0.061      0.952   -1432.116    1351.535
    color[T.G]           2.7731    697.225      0.004      0.997   -1462.043    1467.589
    color[T.H]        -114.1885    689.331     -0.166      0.870   -1562.419    1334.042
    color[T.I]          28.7331    665.152      0.043      0.966   -1368.699    1426.165
    color[T.J]        4.939e-11   9.36e-11      0.528      0.604   -1.47e-10    2.46e-10
    cut[T.Good]      -1050.1645    419.190     -2.505      0.022   -1930.850    -169.479
    cut[T.Ideal]      -499.0686    470.477     -1.061      0.303   -1487.504     489.367
    cut[T.Premium]     226.1418    442.265      0.511      0.615    -703.023    1155.307
    cut[T.Very Good]    60.4024    581.787      0.104      0.918   -1161.886    1282.691
    carat             9185.5385   2223.741      4.131      0.001    4513.633    1.39e+04
    depth              250.3749    525.052      0.477      0.639    -852.718    1353.467
    table               23.0035     95.760      0.240      0.813    -178.181     224.188
    x_dimension      -4295.9110   7503.813     -0.572      0.574   -2.01e+04    1.15e+04
    y_dimension       4295.8661   7683.233      0.559      0.583   -1.18e+04    2.04e+04
    ==============================================================================
    Omnibus:                        1.579   Durbin-Watson:                   1.724
    Prob(Omnibus):                  0.454   Jarque-Bera (JB):                1.521
    Skew:                          -0.413   Prob(JB):                        0.467
    Kurtosis:                       2.497   Cond. No.                     2.34e+18
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The smallest eigenvalue is 5.11e-32. This might indicate that there are
    strong multicollinearity problems or that the design matrix is singular.
    

# Usuńmy najmniej znaczącą zmienną - color


```python
model = smf.ols("price ~ carat + clarity + cut + depth + table + x_dimension + y_dimension", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.978
    Model:                            OLS   Adj. R-squared:                  0.965
    Method:                 Least Squares   F-statistic:                     75.39
    Date:                Sun, 28 Jan 2024   Prob (F-statistic):           2.39e-16
    Time:                        12:34:59   Log-Likelihood:                -293.86
    No. Observations:                  39   AIC:                             617.7
    Df Residuals:                      24   BIC:                             642.7
    Df Model:                          14                                         
    Covariance Type:            nonrobust                                         
    ====================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------------
    Intercept         -1.57e+04   2.77e+04     -0.566      0.577   -7.29e+04    4.15e+04
    clarity[T.IF]     1468.5070    599.029      2.451      0.022     232.172    2704.842
    clarity[T.SI2]     818.9002    413.095      1.982      0.059     -33.685    1671.486
    clarity[T.Si1]     801.1688    436.879      1.834      0.079    -100.504    1702.842
    clarity[T.VVS1]   1351.9966    463.900      2.914      0.008     394.554    2309.439
    clarity[T.VVS2]   1050.3758    449.782      2.335      0.028     122.072    1978.680
    cut[T.Good]      -1007.6329    365.329     -2.758      0.011   -1761.635    -253.631
    cut[T.Ideal]      -512.4353    401.354     -1.277      0.214   -1340.789     315.919
    cut[T.Premium]      88.8894    303.821      0.293      0.772    -538.167     715.946
    cut[T.Very Good]   -33.3145    475.278     -0.070      0.945   -1014.240     947.611
    carat             9149.2623   1854.756      4.933      0.000    5321.234     1.3e+04
    depth              178.7054    434.475      0.411      0.684    -718.007    1075.417
    table               32.0723     76.520      0.419      0.679    -125.857     190.002
    x_dimension      -2820.0281   5971.409     -0.472      0.641   -1.51e+04    9504.353
    y_dimension       2846.4862   6135.787      0.464      0.647   -9817.155    1.55e+04
    ==============================================================================
    Omnibus:                        0.766   Durbin-Watson:                   1.664
    Prob(Omnibus):                  0.682   Jarque-Bera (JB):                0.848
    Skew:                          -0.244   Prob(JB):                        0.654
    Kurtosis:                       2.467   Cond. No.                     2.54e+04
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 2.54e+04. This might indicate that there are
    strong multicollinearity or other numerical problems.
    

# Usuńmy kolumnę depth


```python
model = smf.ols("price ~ carat + clarity + cut + table + x_dimension + y_dimension", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.968
    Model:                            OLS   Adj. R-squared:                  0.961
    Method:                 Least Squares   F-statistic:                     145.3
    Date:                Sun, 28 Jan 2024   Prob (F-statistic):           9.22e-42
    Time:                        12:34:59   Log-Likelihood:                -589.47
    No. Observations:                  77   AIC:                             1207.
    Df Residuals:                      63   BIC:                             1240.
    Df Model:                          13                                         
    Covariance Type:            nonrobust                                         
    ====================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------------
    Intercept        -2868.2918   3418.686     -0.839      0.405   -9699.991    3963.407
    clarity[T.IF]     1248.4493    308.454      4.047      0.000     632.054    1864.845
    clarity[T.SI2]     555.0324    239.403      2.318      0.024      76.624    1033.441
    clarity[T.Si1]     681.3451    267.232      2.550      0.013     147.325    1215.365
    clarity[T.VVS1]   1037.1353    267.505      3.877      0.000     502.570    1571.701
    clarity[T.VVS2]    905.7186    271.265      3.339      0.001     363.640    1447.798
    cut[T.Good]       -502.0799    214.514     -2.341      0.022    -930.752     -73.407
    cut[T.Ideal]      -125.5293    239.806     -0.523      0.602    -604.743     353.685
    cut[T.Premium]     444.4258    218.980      2.030      0.047       6.830     882.022
    cut[T.Very Good]   200.5720    233.895      0.858      0.394    -266.830     667.974
    carat             8816.8855   1306.527      6.748      0.000    6206.000    1.14e+04
    table              -28.3665     58.492     -0.485      0.629    -145.254      88.521
    x_dimension      -1143.5224   3840.746     -0.298      0.767   -8818.641    6531.597
    y_dimension       1509.8220   3944.757      0.383      0.703   -6373.146    9392.790
    ==============================================================================
    Omnibus:                        0.659   Durbin-Watson:                   1.718
    Prob(Omnibus):                  0.719   Jarque-Bera (JB):                0.782
    Skew:                           0.136   Prob(JB):                        0.676
    Kurtosis:                       2.588   Cond. No.                     4.94e+03
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 4.94e+03. This might indicate that there are
    strong multicollinearity or other numerical problems.
    

# Usuńmy kolumnę x_dimension


```python
model = smf.ols("price ~ carat + clarity + cut + table + y_dimension", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.969
    Model:                            OLS   Adj. R-squared:                  0.963
    Method:                 Least Squares   F-statistic:                     171.6
    Date:                Sun, 28 Jan 2024   Prob (F-statistic):           7.48e-45
    Time:                        12:34:59   Log-Likelihood:                -603.98
    No. Observations:                  79   AIC:                             1234.
    Df Residuals:                      66   BIC:                             1265.
    Df Model:                          12                                         
    Covariance Type:            nonrobust                                         
    ====================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------------
    Intercept        -3175.7543   3272.061     -0.971      0.335   -9708.634    3357.126
    clarity[T.IF]     1281.0811    295.403      4.337      0.000     691.289    1870.873
    clarity[T.SI2]     560.8059    233.530      2.401      0.019      94.548    1027.064
    clarity[T.Si1]     690.1862    258.623      2.669      0.010     173.829    1206.544
    clarity[T.VVS1]   1045.0689    260.680      4.009      0.000     524.604    1565.534
    clarity[T.VVS2]    912.7314    263.829      3.460      0.001     385.980    1439.483
    cut[T.Good]       -515.2479    207.279     -2.486      0.015    -929.094    -101.402
    cut[T.Ideal]      -111.4923    233.333     -0.478      0.634    -577.356     354.371
    cut[T.Premium]     439.5514    213.656      2.057      0.044      12.974     866.128
    cut[T.Very Good]   190.6521    228.103      0.836      0.406    -264.770     646.074
    carat             8867.9828   1260.130      7.037      0.000    6352.053    1.14e+04
    table              -22.0863     55.024     -0.401      0.689    -131.946      87.774
    y_dimension        350.7127    486.765      0.720      0.474    -621.145    1322.570
    ==============================================================================
    Omnibus:                        0.429   Durbin-Watson:                   1.718
    Prob(Omnibus):                  0.807   Jarque-Bera (JB):                0.591
    Skew:                           0.097   Prob(JB):                        0.744
    Kurtosis:                       2.624   Cond. No.                     3.06e+03
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 3.06e+03. This might indicate that there are
    strong multicollinearity or other numerical problems.
    

# # Usuńmy kolumnę table


```python
model = smf.ols("price ~ carat + clarity + cut + y_dimension", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.965
    Model:                            OLS   Adj. R-squared:                  0.961
    Method:                 Least Squares   F-statistic:                     222.9
    Date:                Sun, 28 Jan 2024   Prob (F-statistic):           2.95e-59
    Time:                        12:35:00   Log-Likelihood:                -772.75
    No. Observations:                 100   AIC:                             1570.
    Df Residuals:                      88   BIC:                             1601.
    Df Model:                          11                                         
    Covariance Type:            nonrobust                                         
    ====================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------------
    Intercept        -2116.0383   1689.154     -1.253      0.214   -5472.878    1240.801
    clarity[T.IF]     1183.0525    270.393      4.375      0.000     645.704    1720.401
    clarity[T.SI2]     610.5122    207.160      2.947      0.004     198.826    1022.199
    clarity[T.Si1]     593.9217    223.820      2.654      0.009     149.127    1038.717
    clarity[T.VVS1]   1080.8895    234.687      4.606      0.000     614.499    1547.280
    clarity[T.VVS2]   1094.5394    229.386      4.772      0.000     638.683    1550.396
    cut[T.Good]       -379.4521    188.966     -2.008      0.048    -754.981      -3.923
    cut[T.Ideal]        72.1011    212.197      0.340      0.735    -349.596     493.798
    cut[T.Premium]     575.8008    187.546      3.070      0.003     203.093     948.509
    cut[T.Very Good]   275.1723    212.064      1.298      0.198    -146.260     696.605
    carat             1.058e+04   1154.617      9.166      0.000    8288.899    1.29e+04
    y_dimension       -290.7617    437.197     -0.665      0.508   -1159.599     578.075
    ==============================================================================
    Omnibus:                        0.717   Durbin-Watson:                   1.573
    Prob(Omnibus):                  0.699   Jarque-Bera (JB):                0.450
    Skew:                          -0.159   Prob(JB):                        0.799
    Kurtosis:                       3.080   Cond. No.                         213.
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    

# Porównajmy zmienne kategorialne clarity oraz cut za pomocą metody pełna suma kwadratów


```python
difference_clarity = smf.ols("price ~ 1", data=data).fit().ssr - smf.ols("price ~ clarity", data=data).fit().ssr
difference_cut = smf.ols("price ~ 1", data=data).fit().ssr - smf.ols("price ~ cut", data=data).fit().ssr

print(difference_clarity > difference_cut)
```

    True
    

# Usuńmy kolumnę cut


```python
model = smf.ols("price ~ carat + clarity + y_dimension", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.954
    Model:                            OLS   Adj. R-squared:                  0.951
    Method:                 Least Squares   F-statistic:                     272.8
    Date:                Sun, 28 Jan 2024   Prob (F-statistic):           1.24e-58
    Time:                        12:35:00   Log-Likelihood:                -786.89
    No. Observations:                 100   AIC:                             1590.
    Df Residuals:                      92   BIC:                             1611.
    Df Model:                           7                                         
    Covariance Type:            nonrobust                                         
    ===================================================================================
                          coef    std err          t      P>|t|      [0.025      0.975]
    -----------------------------------------------------------------------------------
    Intercept       -3445.6972   1834.353     -1.878      0.063   -7088.880     197.485
    clarity[T.IF]    1157.8063    292.023      3.965      0.000     577.824    1737.789
    clarity[T.SI2]    459.2860    227.912      2.015      0.047       6.633     911.939
    clarity[T.Si1]    742.0849    244.312      3.037      0.003     256.861    1227.309
    clarity[T.VVS1]   832.0783    251.266      3.312      0.001     333.043    1331.114
    clarity[T.VVS2]   979.6204    256.358      3.821      0.000     470.472    1488.769
    carat            9529.2085   1253.518      7.602      0.000    7039.613     1.2e+04
    y_dimension       106.7095    475.058      0.225      0.823    -836.796    1050.215
    ==============================================================================
    Omnibus:                        1.357   Durbin-Watson:                   1.256
    Prob(Omnibus):                  0.507   Jarque-Bera (JB):                1.019
    Skew:                          -0.243   Prob(JB):                        0.601
    Kurtosis:                       3.093   Cond. No.                         204.
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    

# Usuńmy kolumnę y_dimension


```python
model = smf.ols("price ~ carat + clarity", data=data).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.965
    Model:                            OLS   Adj. R-squared:                  0.964
    Method:                 Least Squares   F-statistic:                     659.5
    Date:                Sun, 28 Jan 2024   Prob (F-statistic):          5.04e-101
    Time:                        12:35:00   Log-Likelihood:                -1164.1
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
