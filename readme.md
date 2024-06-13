# Bot de Imagens Aleatórias

Este script em Python automatiza a postagem de imagens aleatórias no Twitter usando a biblioteca Tweepy. O bot seleciona uma imagem aleatória de uma pasta especificada, verifica se um tweet foi feito recentemente e publica a imagem junto com o nome do arquivo como texto.

## Índice

- [Configuração](#configuração)
- [Funcionalidades](#funcionalidades)
- [Dependências](#dependências)
- [Uso](#uso)
- [Estrutura de Arquivos](#estrutura-de-arquivos)

---

## Configuração <a name="configuração"></a>

Antes de executar o bot, certifique-se de configurar suas chaves de API do Twitter no script:

```python
bearer_token = ''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```

Substitua as strings vazias pelos seus valores reais das chaves de API do Twitter.

## Funcionalidades <a name="funcionalidades"></a>

- **Seleção Aleatória:** Seleciona aleatoriamente um arquivo de imagem de uma pasta especificada.
- **Temporização de Tweets:** Garante que os tweets sejam espaçados para cumprir os limites de taxa da API do Twitter.
- **Rastreamento de Estado:** Mantém o controle do horário do último tweet para evitar postagens rápidas.

## Dependências <a name="dependências"></a>

As seguintes bibliotecas Python são necessárias:

- `tweepy`: Para interação com a API do Twitter.
- `os`: Para operações com arquivos e diretórios.
- `random`: Para seleção aleatória de arquivos.
- `time`: Para operações relacionadas ao tempo.
- `datetime`: Para trabalhar com datas e horas.

Certifique-se de que essas bibliotecas estejam instaladas usando o pip:

```bash
pip install tweepy
```

## Uso <a name="uso"></a>

1. **Clonar o Repositório:** Clone o repositório ou faça o download do script Python.

2. **Instalar Dependências:** Instale as dependências necessárias conforme mencionado acima.

3. **Configurar Chaves da API do Twitter:** Substitua os valores fictícios no script pelas suas chaves reais da API do Twitter.

4. **Configurar Pastas:** Defina os caminhos das pastas onde suas imagens estão armazenadas. Atualize a lista `folders` com os caminhos apropriados:

   ```python
   folders = [
       './path/to/your/folders/'
   ]
   ```

5. **Executar o Script:** Execute o script Python:

   ```bash
   python main.py
   ```

6. **Execução Contínua:** O script é executado continuamente e posta um tweet aproximadamente a cada hora, dependendo dos intervalos de espera configurados.

## Estrutura de Arquivos <a name="estrutura-de-arquivos"></a>

- `main.py`: O script principal em Python.
- `savestate.txt`: Um arquivo de texto usado para armazenar o timestamp do último tweet para evitar postagens rápidas.
