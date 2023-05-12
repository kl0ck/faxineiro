import os
import sys

__descricao = "Script para remoção de linhas de código inúteis."

def main(inputFileName):
    if not os.path.exists(inputFileName):
        print("error: Arquivo", inputFileName, "não existe!")
        sys.exit()

    print("Processando... \n")

    inputFile = open(inputFileName, "r")

    inputLines = inputFile.readlines()
    
    outputLines = []
    
    removeFile = open("faxineiro-linhas-remover.txt", "r")
    
    removeLines = removeFile.readlines()
    
    removeSet = set()
    
    for removeLine in removeLines:
        if (removeLine.strip() != ""):
            removeSet.add(removeLine.strip())

    for inputLine in inputLines:
        filtrarLinha(inputLine, removeSet, outputLines)

    outputFile = open(inputFileName + ".limpo", "w")
    
    outputFile.writelines(outputLines)
    
    inputFile.close()
    outputFile.close()
    
    print("Pronto! \n")
    
    print("outputFile =", outputFile.name, "\n")
    
def filtrarLinha(line, removeSet, outputLines):
    if (line.strip() not in removeSet):
        outputLines.append(line)
        
if __name__ == "__main__":
    # https://docs.python.org/3/howto/argparse.html
    import argparse

    parser = argparse.ArgumentParser(description = __descricao)
    
    parser.add_argument('-inputFile', required=True, help='arquivo com o código a limpar')
    
    args = parser.parse_args()
    
    print()
    print(__descricao, "\n")
    
    print()
    print("inputFile =", args.inputFile, "\n")
    
    main(args.inputFile)
