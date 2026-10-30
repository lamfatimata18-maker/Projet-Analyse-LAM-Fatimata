import json
import os
import matplotlib.pyplot as plt
import pandas as pd

# 1. Charger les données
df = pd.read_csv('data/logs_reseau.csv')

# 2. Nettoyage
# - Supprimer les doublons exacts
df = df.drop_duplicates()

# - Mettre le protocole en MAJUSCULES
df['protocol'] = df['protocol'].str.upper()

# - Remplacer les bytes_sent manquants par la médiane
mediane_bytes = df['bytes_sent'].median()
df['bytes_sent'] = df['bytes_sent'].fillna(mediane_bytes)

# 3. Calculs des résultats
nb_lignes_apres = int(len(df))

# Port de destination le plus fréquent
top_port = int(df['dst_port'].mode()[0])

# Taux de DENY en pourcentage (décimal)
total_connexions = len(df)
nb_deny = len(df[df['action'] == 'DENY'])
taux_deny_pct = float((nb_deny / total_connexions) * 100) if total_connexions > 0 else 0.0

# IP scanner (src_ip qui a contacté le plus de ports distincts)
ip_scanner = df.groupby('src_ip')['dst_port'].nunique().idxmax()

# IP exfiltration (src_ip avec le plus grand total de bytes_sent)
ip_exfiltration = df.groupby('src_ip')['bytes_sent'].sum().idxmax()

# Dictionnaire des résultats
resultats = {
    'nb_lignes_apres_nettoyage': nb_lignes_apres,
    'top_port': top_port,
    'taux_deny_pct': round(taux_deny_pct, 12),
    'ip_scanner': str(ip_scanner),
    'ip_exfiltration': str(ip_exfiltration)
}

# Sauvegarde dans resultats.json
with open('resultats.json', 'w') as f:
    json.dump(resultats, f, indent=4)

# 4. Génération des graphiques (au moins 3)
os.makedirs('figures', exist_ok=True)

# Graphique 1 : Top des ports de destination
plt.figure(figsize=(8, 5))
df['dst_port'].value_counts().head(5).plot(kind='bar', color='skyblue')
plt.title('Top 5 des ports de destination les plus fréquents')
plt.xlabel('Port de destination')
plt.ylabel('Nombre de connexions')
plt.savefig('figures/top_ports.png')
plt.close()

# Graphique 2 : Répartition des actions ALLOW / DENY
plt.figure(figsize=(6, 6))
df['action'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'salmon'])
plt.title('Répartition des actions (ALLOW / DENY)')
plt.ylabel('')
plt.savefig('figures/actions_repartition.png')
plt.close()

# Graphique 3 : Volume d'octets par type d'appareil
plt.figure(figsize=(8, 5))
df.groupby('device_type')['bytes_sent'].sum().plot(kind='bar', color='orange')
plt.title("Volume total d'octets envoyés par type d'appareil")
plt.xlabel("Type d'appareil")
plt.ylabel("Octets envoyés")
plt.savefig('figures/bytes_par_device.png')
plt.close()

print("Analyse terminée avec succès ! Résultats et graphiques générés.")