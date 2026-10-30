{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "85a4c980-4916-418b-b65d-e6ba799b4f9e",
   "metadata": {},
   "source": [
    "# Rapport d'analyse des journaux de pare-feu\n",
    "\n",
    "## 1. Résumé de l'analyse\n",
    "Cette analyse s'est penchée sur une semaine d'historique des connexions réseau et des journaux de pare-feu (`logs_reseau.csv`) d'une entreprise comportant des postes informatiques, des serveurs et des objets connectés. Après un nettoyage rigoureux des données (suppression des doublons, uniformisation des protocoles et gestion des valeurs manquantes), plusieurs indicateurs clés ont été calculés et consignés dans le fichier `resultats.json`. L'examen des flux met en lumière des activités anormales nécessitant une intervention rapide de la sécurité.\n",
    "\n",
    "## 2. Comportements suspects observés\n",
    "* **Comportement 1 (Scan de ports) :** Une adresse IP source spécifique a été identifiée comme ayant contacté le plus grand nombre de ports distincts (`ip_scanner`). Ce comportement est typique d'une phase de reconnaissance ou d'un scan de vulnérabilités mené par un acteur malveillant pour cartographier le réseau de l'entreprise.\n",
    "* **Comportement 2 (Exfiltration potentielle de données) :** Une autre adresse IP source génère un volume anormalement élevé d'octets envoyés (`bytes_sent`), surpassant largement la moyenne des autres appareils (`ip_exfiltration`). Cela suggère une fuite de données massive ou un transfert non autorisé vers l'extérieur.\n",
    "\n",
    "## 3. Recommandations de sécurité\n",
    "1. **Segmentation du réseau IoT :** Isoler les objets connectés (caméras, capteurs) sur un VLAN dédié et étanche pour empêcher qu'un équipement compromis ne serve de passerelle vers les serveurs critiques de l'entreprise.\n",
    "2. **Durcissement des règles de pare-feu :** Bloquer immédiatement les flux provenant de l'adresse IP effectuant le scan de ports et restreindre les connexions sortantes non autorisées pour contrer tout risque d'exfiltration.\n",
    "3. **Fermeture des services non sécurisés :** Désactiver l'utilisation de protocoles et de ports obsolètes ou non chiffrés (tels que Telnet) au profit d'alternatives sécurisées (SSH).\n",
    "4."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7c1c0dc1-1e80-4689-b31f-4875f51c43d6",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6594f4f2-8e60-44a2-a632-5af81b87ca43",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
