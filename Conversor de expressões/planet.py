distancia_planetas = {
    'mercúrio':'91.700.000',
    'vênus':'41.400.000',
    'marte':'78.300.000',
    'júpiter':'628.000.000',
    'saturno':'1.280.400.000',
    'urano':'2.720.400.000',
    'netuno':'4.350.400.000'
}

planeta = input('Digite um planeta: ').lower()
distancia = distancia_planetas[planeta]

print('{} está a {} km da Terra'.format(planeta, distancia))
