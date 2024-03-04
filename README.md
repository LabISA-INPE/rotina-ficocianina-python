# Rotina Ficocianina em Python

Rotina em Python para análise de Ficocianina.

## Execução

Para executar o código é necessário instalar as seguintes tecnologias:

* [Python](https://www.python.org/downloads/)
* [Anaconda](https://www.anaconda.com/download)

Clone o repositório com o comando:

```console
git clone https://github.com/LabISA-INPE/rotina-ficocianina-python.git
```

Com o Anaconda Prompt e na **raiz do projeto**, instale as bibliotecas necessárias no arquivo de ambiente:

```console
cd path/rotina-ficocianina-python
```

Observações:
* Confira o nome e o caminho do arquivo de ambiente e, caso necessário, modifique na linha de comando abaixo.
* Também é possível modificar o nome do ambiente (neste caso está com o nome ficocianina).
* Caso seja necessário, altere o arquivo de entrada na linha 5, do arquivo main, dentro das aspas. Veja o exemplo abaixo:
* df = pd.read_csv("C:/path/rotina-ficocianina-python/input/Altere_Aqui", delimiter="\t", decimal=",", index_col=0)
* Cole as linhas de código a seguir no Anaconda Prompt.

```console
conda env create --name ficocianina --file environment.yaml
```

Após isso, ative o ambiente:

```console
conda activate ficocianina
```

Rode o código em Python:

```console
python main.py
```

#

**Importante**: em caso de erro confira o arquivo selecionado para ánalise.

