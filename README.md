# PANDAS


```python
import pandas as pd
import openpyxl
```

# Reading



```python
pd.read_excel("shiva.xlsx").head()
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_excel("shiva.xlsx").tail()
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20</th>
      <td>42</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>44</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>46</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>48</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>50</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
</div>




```python
data=pd.read_excel("shiva.xlsx")
data
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12</td>
      <td>18</td>
      <td>24</td>
      <td>30</td>
      <td>36</td>
      <td>42</td>
      <td>48</td>
      <td>54</td>
      <td>60</td>
      <td>66</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14</td>
      <td>21</td>
      <td>28</td>
      <td>35</td>
      <td>42</td>
      <td>49</td>
      <td>56</td>
      <td>63</td>
      <td>70</td>
      <td>77</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16</td>
      <td>24</td>
      <td>32</td>
      <td>40</td>
      <td>48</td>
      <td>56</td>
      <td>64</td>
      <td>72</td>
      <td>80</td>
      <td>88</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18</td>
      <td>27</td>
      <td>36</td>
      <td>45</td>
      <td>54</td>
      <td>63</td>
      <td>72</td>
      <td>81</td>
      <td>90</td>
      <td>99</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20</td>
      <td>30</td>
      <td>40</td>
      <td>50</td>
      <td>60</td>
      <td>70</td>
      <td>80</td>
      <td>90</td>
      <td>100</td>
      <td>110</td>
    </tr>
    <tr>
      <th>10</th>
      <td>22</td>
      <td>33</td>
      <td>44</td>
      <td>55</td>
      <td>66</td>
      <td>77</td>
      <td>88</td>
      <td>99</td>
      <td>110</td>
      <td>121</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24</td>
      <td>36</td>
      <td>48</td>
      <td>60</td>
      <td>72</td>
      <td>84</td>
      <td>96</td>
      <td>108</td>
      <td>120</td>
      <td>132</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26</td>
      <td>39</td>
      <td>52</td>
      <td>65</td>
      <td>78</td>
      <td>91</td>
      <td>104</td>
      <td>117</td>
      <td>130</td>
      <td>143</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28</td>
      <td>42</td>
      <td>56</td>
      <td>70</td>
      <td>84</td>
      <td>98</td>
      <td>112</td>
      <td>126</td>
      <td>140</td>
      <td>154</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30</td>
      <td>45</td>
      <td>60</td>
      <td>75</td>
      <td>90</td>
      <td>105</td>
      <td>120</td>
      <td>135</td>
      <td>150</td>
      <td>165</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32</td>
      <td>48</td>
      <td>64</td>
      <td>80</td>
      <td>96</td>
      <td>112</td>
      <td>128</td>
      <td>144</td>
      <td>160</td>
      <td>176</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34</td>
      <td>51</td>
      <td>68</td>
      <td>85</td>
      <td>102</td>
      <td>119</td>
      <td>136</td>
      <td>153</td>
      <td>170</td>
      <td>187</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36</td>
      <td>54</td>
      <td>72</td>
      <td>90</td>
      <td>108</td>
      <td>126</td>
      <td>144</td>
      <td>162</td>
      <td>180</td>
      <td>198</td>
    </tr>
    <tr>
      <th>18</th>
      <td>38</td>
      <td>57</td>
      <td>76</td>
      <td>95</td>
      <td>114</td>
      <td>133</td>
      <td>152</td>
      <td>171</td>
      <td>190</td>
      <td>209</td>
    </tr>
    <tr>
      <th>19</th>
      <td>40</td>
      <td>60</td>
      <td>80</td>
      <td>100</td>
      <td>120</td>
      <td>140</td>
      <td>160</td>
      <td>180</td>
      <td>200</td>
      <td>220</td>
    </tr>
    <tr>
      <th>20</th>
      <td>42</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>44</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>46</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>48</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>50</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.set_option('display.max_rows', 5)
```


```python
data
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>48</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>50</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.P1
```




    0      2
    1      4
          ..
    23    48
    24    50
    Name: P1, Length: 25, dtype: int64




```python
data["P1"][0]
```




    2




```python
data.iloc[0]
```




    P1      2
    P2      3
           ..
    P9     10
    P10    11
    Name: 0, Length: 10, dtype: int64




```python
data.iloc[:,0]
```




    0      2
    1      4
          ..
    23    48
    24    50
    Name: P1, Length: 25, dtype: int64




```python
data.iloc[:3,0]
```




    0    2
    1    4
    2    6
    Name: P1, dtype: int64




```python
data.iloc[1:3,0]
```




    1    4
    2    6
    Name: P1, dtype: int64




```python
data.iloc[-5:]
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20</th>
      <td>42</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>44</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>46</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>48</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>50</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.set_index("P1")
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
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
    <tr>
      <th>P1</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>48</th>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>50</th>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 9 columns</p>
</div>




```python
data.P1==4
```




    0     False
    1      True
          ...  
    23    False
    24    False
    Name: P1, Length: 25, dtype: bool




```python
data["P1"]=5
data
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>5</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.set_index("P1")
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
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
    <tr>
      <th>P1</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>5</th>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 9 columns</p>
</div>




```python
data
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>5</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data["P1"]=range(len(data),0,-1)
data.set_index("P1")
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
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
    <tr>
      <th>P1</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>25</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>24</th>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>1</th>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 9 columns</p>
</div>




```python
data.describe()
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>25.0</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>13.0</td>
      <td>39.0</td>
      <td>52.0</td>
      <td>65.0</td>
      <td>78.0</td>
      <td>91.0</td>
      <td>104.0</td>
      <td>117.0</td>
      <td>130.0</td>
      <td>143.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>19.0</td>
      <td>57.0</td>
      <td>76.0</td>
      <td>95.0</td>
      <td>114.0</td>
      <td>133.0</td>
      <td>152.0</td>
      <td>171.0</td>
      <td>190.0</td>
      <td>209.0</td>
    </tr>
    <tr>
      <th>max</th>
      <td>25.0</td>
      <td>75.0</td>
      <td>100.0</td>
      <td>125.0</td>
      <td>150.0</td>
      <td>175.0</td>
      <td>200.0</td>
      <td>225.0</td>
      <td>250.0</td>
      <td>275.0</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 10 columns</p>
</div>




```python
pd.set_option("display.max_rows",10)
```


```python
data
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.describe()
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>25.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>13.000000</td>
      <td>39.000000</td>
      <td>52.000000</td>
      <td>65.000000</td>
      <td>78.000000</td>
      <td>91.000000</td>
      <td>104.000000</td>
      <td>117.000000</td>
      <td>130.000000</td>
      <td>143.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.359801</td>
      <td>22.079402</td>
      <td>29.439203</td>
      <td>36.799004</td>
      <td>44.158804</td>
      <td>51.518605</td>
      <td>58.878406</td>
      <td>66.238206</td>
      <td>73.598007</td>
      <td>80.957808</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>5.000000</td>
      <td>6.000000</td>
      <td>7.000000</td>
      <td>8.000000</td>
      <td>9.000000</td>
      <td>10.000000</td>
      <td>11.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.000000</td>
      <td>21.000000</td>
      <td>28.000000</td>
      <td>35.000000</td>
      <td>42.000000</td>
      <td>49.000000</td>
      <td>56.000000</td>
      <td>63.000000</td>
      <td>70.000000</td>
      <td>77.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>13.000000</td>
      <td>39.000000</td>
      <td>52.000000</td>
      <td>65.000000</td>
      <td>78.000000</td>
      <td>91.000000</td>
      <td>104.000000</td>
      <td>117.000000</td>
      <td>130.000000</td>
      <td>143.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>19.000000</td>
      <td>57.000000</td>
      <td>76.000000</td>
      <td>95.000000</td>
      <td>114.000000</td>
      <td>133.000000</td>
      <td>152.000000</td>
      <td>171.000000</td>
      <td>190.000000</td>
      <td>209.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>25.000000</td>
      <td>75.000000</td>
      <td>100.000000</td>
      <td>125.000000</td>
      <td>150.000000</td>
      <td>175.000000</td>
      <td>200.000000</td>
      <td>225.000000</td>
      <td>250.000000</td>
      <td>275.000000</td>
    </tr>
  </tbody>
</table>
</div>



# data.P1.describe()


```python
data.P1.describe()
```




    count    25.000000
    mean     13.000000
    std       7.359801
    min       1.000000
    25%       7.000000
    50%      13.000000
    75%      19.000000
    max      25.000000
    Name: P1, dtype: float64




```python
data.mean()
```




    P1      13.0
    P2      39.0
    P3      52.0
    P4      65.0
    P5      78.0
    P6      91.0
    P7     104.0
    P8     117.0
    P9     130.0
    P10    143.0
    dtype: float64




```python
data.P1.unique()
```




    array([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,
            8,  7,  6,  5,  4,  3,  2,  1], dtype=int64)




```python
data.P1.value_counts()
```




    P1
    25    1
    12    1
    2     1
    3     1
    4     1
         ..
    20    1
    21    1
    22    1
    23    1
    1     1
    Name: count, Length: 25, dtype: int64



# Map



```python
data_mean=data.P2.mean()
data_mean
```




    39.0




```python
data.P2.map(lambda p: p- data_mean)
```




    0    -36.0
    1    -33.0
    2    -30.0
    3    -27.0
    4    -24.0
          ... 
    20    24.0
    21    27.0
    22    30.0
    23    33.0
    24    36.0
    Name: P2, Length: 25, dtype: float64




```python
data.P3 + data.P2
```




    0       7
    1      14
    2      21
    3      28
    4      35
         ... 
    20    147
    21    154
    22    161
    23    168
    24    175
    Length: 25, dtype: int64



# Grouping and Sorting


```python
data.groupby("P1").P1.count()
```




    P1
    1     1
    2     1
    3     1
    4     1
    5     1
         ..
    21    1
    22    1
    23    1
    24    1
    25    1
    Name: P1, Length: 25, dtype: int64




```python
data.groupby("P1").P2.min()
```




    P1
    1     75
    2     72
    3     69
    4     66
    5     63
          ..
    21    15
    22    12
    23     9
    24     6
    25     3
    Name: P2, Length: 25, dtype: int64




```python
data.groupby("P3").apply(lambda d: d.P2.iloc[0])
```




    P3
    4       3
    8       6
    12      9
    16     12
    20     15
           ..
    84     63
    88     66
    92     69
    96     72
    100    75
    Length: 25, dtype: int64




```python
data
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.groupby(["P3","P4"]).apply(lambda d: d.loc[d.P5.idxmax()])
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
      <th></th>
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
    <tr>
      <th>P3</th>
      <th>P4</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <th>5</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>8</th>
      <th>10</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>12</th>
      <th>15</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>16</th>
      <th>20</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>20</th>
      <th>25</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>84</th>
      <th>105</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>88</th>
      <th>110</th>
      <td>4</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>92</th>
      <th>115</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>96</th>
      <th>120</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>100</th>
      <th>125</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.groupby("P10").P2.agg([len,min ,max])
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
      <th>len</th>
      <th>min</th>
      <th>max</th>
    </tr>
    <tr>
      <th>P10</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>1</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>33</th>
      <td>1</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <th>55</th>
      <td>1</td>
      <td>15</td>
      <td>15</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>231</th>
      <td>1</td>
      <td>63</td>
      <td>63</td>
    </tr>
    <tr>
      <th>242</th>
      <td>1</td>
      <td>66</td>
      <td>66</td>
    </tr>
    <tr>
      <th>253</th>
      <td>1</td>
      <td>69</td>
      <td>69</td>
    </tr>
    <tr>
      <th>264</th>
      <td>1</td>
      <td>72</td>
      <td>72</td>
    </tr>
    <tr>
      <th>275</th>
      <td>1</td>
      <td>75</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 3 columns</p>
</div>




```python
data.sort_values(by="P1")
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.sort_values(by="P1",ascending=False)
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.sort_index()
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.sort_values(["P1","P2"])
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>



# Datatypes And Missing values



```python
data.P2.dtype
```




    dtype('int64')




```python
data.dtypes
```




    P1     int64
    P2     int64
    P3     int64
    P4     int64
    P5     int64
    P6     int64
    P7     int64
    P8     int64
    P9     int64
    P10    int64
    dtype: object




```python
data.P1.astype('float64')
```




    0     25.0
    1     24.0
    2     23.0
    3     22.0
    4     21.0
          ... 
    20     5.0
    21     4.0
    22     3.0
    23     2.0
    24     1.0
    Name: P1, Length: 25, dtype: float64




```python
data
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.index.dtype
```




    dtype('int64')




```python
data.isnull()
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>21</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>22</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>23</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>24</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data[pd.isnull(data.P1)]
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
data.fillna("NULL")
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>66</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data=data.replace(66,None)
```


```python
data
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>None</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.isnull()
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>21</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>22</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>23</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>24</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data=data.fillna("Hello")
data
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>Hello</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data.groupby("P2").P1.count()
```




    P2
    3        1
    6        1
    9        1
    12       1
    15       1
            ..
    63       1
    69       1
    72       1
    75       1
    Hello    1
    Name: P1, Length: 25, dtype: int64



# Renaming and Combing


```python
data.rename(columns={"P10":"P15"})
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
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>Hello</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>




```python
data=data.rename(index={0:"zero"})
```


```python
data.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
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
      <th>fields</th>
      <th>P1</th>
      <th>P2</th>
      <th>P3</th>
      <th>P4</th>
      <th>P5</th>
      <th>P6</th>
      <th>P7</th>
      <th>P8</th>
      <th>P9</th>
      <th>P10</th>
    </tr>
    <tr>
      <th>wines</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>zero</th>
      <td>25</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>14</td>
      <td>16</td>
      <td>18</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>9</td>
      <td>12</td>
      <td>15</td>
      <td>18</td>
      <td>21</td>
      <td>24</td>
      <td>27</td>
      <td>30</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22</td>
      <td>12</td>
      <td>16</td>
      <td>20</td>
      <td>24</td>
      <td>28</td>
      <td>32</td>
      <td>36</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21</td>
      <td>15</td>
      <td>20</td>
      <td>25</td>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5</td>
      <td>63</td>
      <td>84</td>
      <td>105</td>
      <td>126</td>
      <td>147</td>
      <td>168</td>
      <td>189</td>
      <td>210</td>
      <td>231</td>
    </tr>
    <tr>
      <th>21</th>
      <td>4</td>
      <td>Hello</td>
      <td>88</td>
      <td>110</td>
      <td>132</td>
      <td>154</td>
      <td>176</td>
      <td>198</td>
      <td>220</td>
      <td>242</td>
    </tr>
    <tr>
      <th>22</th>
      <td>3</td>
      <td>69</td>
      <td>92</td>
      <td>115</td>
      <td>138</td>
      <td>161</td>
      <td>184</td>
      <td>207</td>
      <td>230</td>
      <td>253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>72</td>
      <td>96</td>
      <td>120</td>
      <td>144</td>
      <td>168</td>
      <td>192</td>
      <td>216</td>
      <td>240</td>
      <td>264</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>75</td>
      <td>100</td>
      <td>125</td>
      <td>150</td>
      <td>175</td>
      <td>200</td>
      <td>225</td>
      <td>250</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 10 columns</p>
</div>


