import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import PowerTransformer

# Sample Data
data = {'Value': [10, 12, 12, 13, 12, 11, 12, 14, 15, 100]}  # 100 is an outlier
df = pd.DataFrame(data)

# Log Transformation
df['Log_Transformed'] = np.log1p(df['Value'])

# Square Root Transformation
df['Sqrt_Transformed'] = np.sqrt(df['Value'])

# Box-Cox Transformation
shifted_value = df['Value'] - df['Value'].min() + 1  # Shifting to make all values positive
df['BoxCox_Transformed'], _ = stats.boxcox(shifted_value)

# Yeo-Johnson Transformation
pt = PowerTransformer(method='yeo-johnson')
df['YeoJohnson_Transformed'] = pt.fit_transform(df[['Value']])

# Visualizing the Transformed Data
plt.figure(figsize=(15, 10))

# Original Data
plt.subplot(2, 3, 1)
sns.histplot(df['Value'], kde=True)
plt.title('Original Data')

# Log Transformation
plt.subplot(2, 3, 2)
sns.histplot(df['Log_Transformed'], kde=True)
plt.title('Log Transformation')

# Square Root Transformation
plt.subplot(2, 3, 3)
sns.histplot(df['Sqrt_Transformed'], kde=True)
plt.title('Square Root Transformation')

# Box-Cox Transformation
plt.subplot(2, 3, 4)
sns.histplot(df['BoxCox_Transformed'], kde=True)
plt.title('Box-Cox Transformation')

# Yeo-Johnson Transformation
plt.subplot(2, 3, 5)
sns.histplot(df['YeoJohnson_Transformed'], kde=True)
plt.title('Yeo-Johnson Transformation')

plt.tight_layout()
plt.show()
