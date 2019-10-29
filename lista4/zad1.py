karton_mleka = {}

waznosc_mleka = ('Dzień:30', 'Miesiąc:12', 'Rok:2020')
karton_mleka['data_waznosci'] = waznosc_mleka
karton_mleka['waga'] = '1,5l'
karton_mleka['koszt'] = 5.79
karton_mleka['marka'] = 'Polskie Mleko'

for cat, text in karton_mleka.items():
    print(f"{cat}: {text}")

sixmilks = 6 * karton_mleka['koszt']

print(f"\nKoszt 6 mlek: {sixmilks}")