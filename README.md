# faxineiro.py
Script simples para remoção de linhas de código inúteis.

![image](https://github.com/kl0ck/faxineiro.py/assets/12021775/4c64e9c7-a037-4799-a187-43be21d731b2)

![image](https://github.com/kl0ck/faxineiro.py/assets/12021775/119b5f18-17fa-4e02-854c-6694d8f534f1)

## Como usar o script
- Adicione no arquivo `faxineiro-linhas-remover.txt` as linhas que você quer remover do arquivo de entrada, exatamente como elas aparecem no arquivo original. Espaços em branco e quebra de linha são desconsiderados. Texto é case sensitive.
- Execute o script passando o nome do arquivo a limpar, através dos argumentos `-inputFile <nome_do_arquivo>`.
- Como resultado, o script vai gerar um novo arquivo com o mesmo nome, com a extensão `.limpo`. Este arquivo não terá as linhas inúteis que foram configuradas no arquivo `faxineiro-linhas-remover.txt`.

## Exemplo de uso
`python faxineiro.py -inputFile MinhaClasse.java`

Arquivo de saída gerado: `MinhaClasse.java.limpo`

## A fazer
- Incluir suporte a expressões regulares.
- Incluir suporte a limpeza de vários arquivos.
