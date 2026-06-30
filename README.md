# WinthorExport

Automação de geração e exportação de relatórios do sistema WinThor (TOTVS) via PyAutoGUI.

## O que faz

O script acessa o WinThor automaticamente, executa as rotinas configuradas, exporta os relatórios em CSV e os organiza em pastas por data. Ao final, transfere os arquivos para as pastas de base de dados da equipe e atualiza as planilhas de VDA e estoque.

**Rotinas automatizadas:** 8524, 8536, 8551, 8588, 8598, 8680, 8685, 8688, 8770, 8796

## Pré-requisitos

- Python 3.12 (recomendado)
- AppController (GraphOn) instalado
- Acesso à rede compartilhada

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

Copie o arquivo de exemplo e preencha com os dados do seu ambiente:

```bash
cp config.example.py config.py
```

Abra o `config.py` e informe:
- `SERVIDOR_WINTHOR` — endereço do servidor WinThor
- `CAMINHO_EXPORT` — pasta local onde os CSVs serão salvos (drive H:)
- `CAMINHO_WINTHOR` — mesma pasta acessada pelo WinThor (drive W:)
- `CAMINHO_BD` — pasta de destino da base de dados
- `CAMINHO_BD_VDA` — pasta de destino das planilhas de VDA

> **O arquivo `config.py` nunca deve ser enviado ao repositório.** Ele contém dados do ambiente da sua empresa.

## Como usar

Execute o script principal:

```bash
python TR.py
```

O sistema pedirá as informações na seguinte ordem:

1. **Datas do período** — início, fim e início do estoque (formato `dd/mm/aaaa`, com validação)
2. **Usuário e senha do WinThor** — senha digitada de forma segura e confirmada
3. **Agendamento** — data e hora para iniciar (formato `dd/mm/aaaa` e `hh:mm`, com validação); se a data já passou, inicia imediatamente

Após a execução, um arquivo de log é gerado automaticamente na pasta `Logs/` com o registro completo de tudo que foi impresso no terminal.

## Estrutura do projeto

```
TR.py                  — script principal
requirements.txt       — dependências Python
01 - Imgs/             — imagens de referência para o PyAutoGUI
02 - Rotinas/          — uma rotina por arquivo (g = gerar, e = exportar)
Addons/
  TransArquivos.py     — compilar partes do 8598 e transferir arquivos
  acoes_winthor.py     — funções de automação (clique, imagem, login)
  config.example.py    — modelo de configuração (copie para config.py)
Relatorios/
  vdaTLMK.py           — atualiza planilha de VDA do TLMK
  bdEstoque.py         — atualiza base de dados de estoque
  bdVDA.py             — atualiza base de dados de vendas
Logs/                  — logs de execução gerados automaticamente (não versionados)
```
