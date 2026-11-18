# 📘 Atividade: Testes Automatizados em Python

## 🎯 Objetivo

Aprenda a escrever testes automatizados com `unittest` para verificar se funções e classes em Python se comportam como esperado, inclusive em casos de erro.

## 📝 Tarefas

### 🛠️	Testar uma Função Simples

#### Descrição
Escreva testes para a função `calcular_media(notas)`, usando `assertEqual` para comparar o resultado esperado com o resultado obtido.

#### Requisitos
O programa concluído deve:

- Criar uma classe de teste herdando de `unittest.TestCase`
- Testar a média de uma lista com valores inteiros e outra com valores decimais
- Executar os testes e confirmar que todos passam


### 🛠️	Testar Casos de Erro

#### Descrição
Verifique se a função `calcular_media(notas)` levanta um erro quando recebe uma lista vazia, e se a função `classificar_nota(media)` retorna a classificação correta nos limites das faixas.

#### Requisitos
O programa concluído deve:

- Usar `assertRaises` para verificar que uma lista vazia gera `ValueError`
- Testar `classificar_nota` com valores exatamente nos limites (7 e 5)
- Testar pelo menos um valor abaixo de cada limite


### 🛠️	Testar uma Classe com `setUp`

#### Descrição
Escreva testes para a classe `ContaBancaria`, criando um objeto de teste em um método `setUp` que roda antes de cada teste.

#### Requisitos
O programa concluído deve:

- Usar `setUp` para criar uma nova conta antes de cada teste
- Testar depósitos e saques que alteram o saldo corretamente
- Testar que um saque acima do saldo gera `ValueError`
- Garantir que cada teste é independente dos outros
