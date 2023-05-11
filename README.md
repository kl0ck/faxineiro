# faxineiro.py
Script simples para remoção de linhas de código inúteis.

![image](https://github.com/kl0ck/faxineiro.py/assets/12021775/4c64e9c7-a037-4799-a187-43be21d731b2)

## Como usar o script
- Adicione no arquivo `faxineiro-linhas-remover.txt` as linhas que você quer remover do arquivo de entrada, exatamente como elas aparecem no arquivo original. Espaços em branco e quebra de linha são desconsiderados. Texto é case sensitive.
- Execute o script passando o nome do arquivo a limpar, através dos argumentos `-inputFile <nome_do_arquivo>`.

## Exemplo de uso
python faxineiro.py -inputFile MinhaClasse.java
