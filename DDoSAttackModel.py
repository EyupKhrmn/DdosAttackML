import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('OtukenYoluYeni.csv')

# Her bir IP adresinin kaç kez göründüğünü hesapla
ip_counts = df['Source'].value_counts()

# 1500'den fazla istek gönderen IP adreslerini bul
ddos_ips = ip_counts[ip_counts > 1500].index

# Yeni bir sütun oluştur ve DDoS saldırısı yapan IP adreslerini belirle
df['IsDDoS'] = df['Source'].apply(lambda x: 1 if x in ddos_ips else 0)

# Değişiklikleri CSV dosyasına kaydet
df.to_csv('OtukenYoluYeni.csv', index=False)


#------------------------------------------------------------
# Veri setini oku
df = pd.read_csv('OtukenYoluYeni.csv')

# DDoS saldırılarının sayısını hesapla
ddos_count = df[df['IsDDoS'] == 1].count()

# Normal trafiğin sayısını hesapla
normal_traffic_count = df[df['IsDDoS'] == 0].count()

# DDoS saldırısı yapan IP adreslerini bul
ddos_ips = df.loc[df['IsDDoS'] == 1, 'Source'].unique()

# Sonuçları yazdır
print(f"DDoS saldırılarının sayısı: {ddos_count['IsDDoS']}")
print(f"Normal trafiğin sayısı: {normal_traffic_count['IsDDoS']}")
print(f"DDoS saldırısı yapan IP adresleri: {ddos_ips}")



#Mobil Uygulama ile yeni bir Ddos atağı atılarak veri seti oluşturulacak daha sonra bu veri seti Pyhton ile işlenecek
#Python ile oluşturulan model veri setininin içerisinde aynı IP Adresinden 1500 den fazla istek varsa bu IP adresi Ddos saldırısı yapmış olarak işaretleyecek
#daha sonra Veri setinin üzerinde bu IP adresinden gelen istekleri DDOS atağı olarak işaretleyecek ve sonuçları yazdıracak
#Gelen sonuçlar kaç adet Ddos saldırısı yapıldığını ve kaç adet normal trafik olduğunu gösterecek
#Son olarak Ddos saldırısı yapan IP adreslerini yazdıracak
