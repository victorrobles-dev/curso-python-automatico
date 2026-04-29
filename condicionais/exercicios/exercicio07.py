# Peça para o usuário digitar um meio de transporte. Mostre uma mensagem conforme a entrada: "carro" → "Veículo terrestre", "bicicleta" → "Transporte sustentável", "avião" ou "helicóptero" → "Transporte aéreo", Qualquer outro → "Transporte desconhecido"
transporte = input('Digite o meio de transporte que deseja utilizar: ')

match transporte:
    case 'carro':
        print('Veículo terrestre')
    case 'bicicleta':
        print('Transporte sustentável')
    case 'avião' | 'helicóptero':
        print('Veículo aéreo')
    case _:
        print('Transporte desconhecido')







