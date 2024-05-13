import pandas as pd

# CSV dosyasını oku
#df = pd.read_csv('UdpAttackNew.csv')

# Yeni bir sütun oluştur ve koşula bağlı olarak değer atama
#df = df['IsDDoS']

# Değişiklikleri CSV dosyasına kaydet
#df.to_csv('CSharpDDosAttackEski.csv', index=False)

import pandas as pd
import numpy as np

# CSV dosyasını oku
df = pd.read_csv('UdpAttackNew.csv')

# Yeni bir sütun oluştur ve tüm değerlerini NaN olarak ayarla
df['IsDDoS'] = np.nan

# Değişiklikleri CSV dosyasına kaydet
df.to_csv('UdpAttackNew.csv', index=False)


import pandas as pd

# CSV dosyasını oku
#df = pd.read_csv('UdpAttackNew.csv')

# 'NewColumn' sütununu sil
#df = df.drop('NewColumn', axis=1)

# Değişiklikleri CSV dosyasına kaydet
#df.to_csv('UdpAttackNew.csv', index=False)