"""
Aluno:
Matheus Paul Lopuch
Analisador léxico, usando apenas máquinas de estado finito capaz de validar todos os lexemas
necessários para a redação de um laço de repetição 𝒇𝒐𝒓 em Python. Observe que seu esforço é limitado ao laço 𝒇𝒐𝒓.
"""

def analisador_lexico(codigo):
    tokens = []
    i = 0
    linha = 1
    coluna = 1
    
    palavras_reservadas = ['for', 'in']
    
    while i < len(codigo):
        # Ignorar espaços e tabulações
        if codigo[i] in [' ', '\t']:
            coluna += 1
            i += 1
            continue
            
        # Verificar quebra de linha
        if codigo[i] == '\n':
            linha += 1
            coluna = 1
            i += 1
            continue
            
        # Identificar palavras reservadas e identificadores
        if codigo[i].isalpha() or codigo[i] == '_':
            inicio = i
            while i < len(codigo) and (codigo[i].isalnum() or codigo[i] == '_'):
                i += 1
            
            lexema = codigo[inicio:i]
            if lexema in palavras_reservadas:
                tokens.append({"valor": lexema, "classe": "Palavra Reservada", "linha": linha, "coluna": coluna})
            else:
                tokens.append({"valor": lexema, "classe": "Identificador", "linha": linha, "coluna": coluna})
            
            coluna += (i - inicio)
            continue
            
        # Identificar números
        if codigo[i].isdigit():
            inicio = i
            while i < len(codigo) and codigo[i].isdigit():
                i += 1
            
            tokens.append({"valor": codigo[inicio:i], "classe": "Número", "linha": linha, "coluna": coluna})
            coluna += (i - inicio)
            continue
            
        # Identificar caracteres especiais
        if codigo[i] in ['(', ')', ':', ',']:
            tokens.append({"valor": codigo[i], "classe": "Caractere Especial", "linha": linha, "coluna": coluna})
            coluna += 1
            i += 1
            continue
        
        # Se chegou aqui, é um caractere não reconhecido
        tokens.append({"valor": codigo[i], "classe": "Desconhecido", "linha": linha, "coluna": coluna})
        coluna += 1
        i += 1
    
    return tokens

# Exemplo de uso
codigo_for = "for i in range(10):"
tokens = analisador_lexico(codigo_for)
for token in tokens:
    print(f"{token['valor']} - {token['classe']} (Linha {token['linha']}, Coluna {token['coluna']})")