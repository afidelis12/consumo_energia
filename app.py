# Calculadora de Gasto com Combustível
# Exemplo de aula - Prof. Adriana

# 1. Solicita o nome/modelo do veículo
veiculo = input("Digite o modelo do veículo: ")

# 2. Solicita o consumo médio (km por litro)
consumoKmL = float(input("Digite o consumo médio (km/L): "))

# 3. Solicita a distância média percorrida por dia (km)
distanciaDia = float(input("Digite a distância média percorrida por dia (km): "))

# 3.1 (Dica aplicada) Solicita o preço do litro do combustível
precoLitro = float(input("Digite o preço do litro do combustível (R$): "))

# 4. Calcula o consumo diário em litros
litrosDia = distanciaDia / consumoKmL

# 4.1 Calcula o total de litros consumidos no mês (30 dias)
litrosMes = litrosDia * 30

# 4.2 Calcula o gasto mensal com combustível
gastoMensal = litrosMes * precoLitro

# 5. Mostra o resultado formatado na tela
print("\nVeículo:", veiculo)
print("Consumo mensal estimado:", round(litrosMes, 2), "litros")
print("Gasto estimado: R$ %.2f/mês" % gastoMensal)
