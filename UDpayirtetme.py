import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('UDPdDOsAttack.csv')

# 'Info' sütunundaki NaN değerleri 'Unknown' ile doldur
df['Info'].fillna('Unknown', inplace=True)

# 'Info' sütununda 'Len=1200' ifadesini içeren satırları bul ve 'IsDDOS' sütununu 1 yap
df.loc[df['Info'].str.contains('Len=1200'), 'IsDDOS'] = 1

# Diğer tüm satırlar için 'IsDDOS' sütununu 0 yap
df['IsDDOS'].fillna(0, inplace=True)

# Değişiklikleri CSV dosyasına kaydet
df.to_csv('UDPdDOsAttack.csv', index=False)