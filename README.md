# Desafio de Automação Digital: Gestão de Peças ⚙️

Este projeto é um protótipo de automação em Python desenvolvido para o controle de produção e qualidade de peças industriais. O sistema substitui a inspeção manual, reduzindo falhas e organizando o armazenamento automaticamente.

## 🚀 Como funciona
O sistema possui um menu interativo via terminal onde o usuário pode cadastrar peças informando seu ID, peso, cor e comprimento. O algoritmo avalia as regras de qualidade e, se aprovada, armazena a peça. A cada 10 peças aprovadas, uma caixa é automaticamente "fechada".

### Regras de Aprovação:
- Peso: 95g a 105g
- Cor: Azul ou Verde
- Comprimento: 10cm a 20cm

## 💻 Como rodar o programa
1. Certifique-se de ter o [Python 3.x](https://www.python.org/) instalado na sua máquina.
2. Clone este repositório: https://github.com/oThi3rry/automacao-industrial-python
3. Abra o terminal na pasta do projeto.
4. Execute o comando: `python main.py`

## 📋 Exemplos de Entrada e Saída

**Entrada de Peça Aprovada:**
- ID: 101
- Peso: 100
- Cor: azul
- Comprimento: 15
*Saída:* ✅ Peça APROVADA com sucesso!

**Entrada de Peça Reprovada:**
- ID: 102
- Peso: 90
- Cor: vermelho
- Comprimento: 15
*Saída:* ❌ Peça REPROVADA. Motivo(s): Peso fora do padrão (95g - 105g) | Cor inválida (deve ser azul ou verde)
