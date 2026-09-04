# ⛽ 👨‍🔧 Calculadora de Gasto com Combustível

Programa em Python desenvolvido como **exemplo de aula** para o curso introdutório de Programação — Etec Alberto Santos Dumont, Guarujá.

O objetivo é demonstrar, na prática, o uso de **entrada de dados (`input`)**, **conversão de tipos**, **operações matemáticas** e **formatação de saída (`print`)** em Python.

---

## 📋 Descrição

O programa solicita ao usuário algumas informações sobre o seu veículo e calcula uma estimativa do **gasto mensal com combustível**, com base na distância percorrida diariamente e no consumo médio do carro.

### Dados solicitados ao usuário

| Dado | Descrição | Tipo |
|---|---|---|
| `veiculo` | Nome ou modelo do veículo (ex.: "Onix") | `str` |
| `consumoKmL` | Consumo médio do veículo em km/L | `float` |
| `distanciaDia` | Distância média percorrida por dia (km) | `float` |
| `precoLitro` | Preço do litro do combustível (R$) | `float` |

---

## 🧮 Fórmulas utilizadas

```python
litrosDia = distanciaDia / consumoKmL
litrosMes = litrosDia * 30
gastoMensal = litrosMes * precoLitro
```

1. **Litros consumidos por dia** = distância percorrida ÷ consumo médio do veículo
2. **Litros consumidos no mês** = litros por dia × 30 (dias)
3. **Gasto mensal estimado** = litros no mês × preço do litro

---

## 💻 Código completo

```python
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
```

---

## ▶️ Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Salve o código em um arquivo chamado `gasto_combustivel.py`.
3. Execute pelo terminal:

```bash
python gasto_combustivel.py
```

4. Informe os dados solicitados quando pedido.

---

## 🖥️ Exemplo de execução

```
Digite o modelo do veículo: Onix
Digite o consumo médio (km/L): 12
Digite a distância média percorrida por dia (km): 40
Digite o preço do litro do combustível (R$): 6.10

Veículo: Onix
Consumo mensal estimado: 100.0 litros
Gasto estimado: R$ 610,00/mês
```

---

## 📚 Conceitos praticados

- Entrada de dados com `input()`
- Conversão de tipos com `float()`
- Operadores aritméticos (`/`, `*`)
- Arredondamento de números com `round()`
- Formatação de strings com `%.2f`
- Concatenação de valores no `print()`

---

## 💡 Sugestões de aprimoramento

- Perguntar quantos dias por semana o veículo é usado, em vez de assumir uso diário.
- Comparar o gasto estimado entre dois veículos diferentes.
- Exibir o resultado também em formato de tabela.
- Tratar entradas inválidas com `try/except`.

---

## 👩‍🏫 Contexto pedagógico

Este exemplo foi construído para espelhar a estrutura de um exercício avaliativo proposto aos alunos (cálculo de consumo elétrico de aparelhos domésticos), servindo como demonstração em aula sem revelar a resposta da atividade oficial.

**Etapas seguidas no exemplo:**
1. Solicitar dados de entrada
2. Realizar cálculo com fórmula
3. Exibir resultado formatado
4. Sugerir um incremento opcional (dica de aprofundamento)

---

## 📄 Licença

Material de uso educacional — livre para reprodução e adaptação em contexto de ensino.
