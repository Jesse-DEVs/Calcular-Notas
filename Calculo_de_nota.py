def obter_nota(materia):
    while True:
        try:
            nota = float(input(f'Digite a nota de {materia} (0 a 10): '))
            if 0 <= nota <= 10:
             return nota
            else:
                print('a nota deve ser entre 0 e 10, tente novamente')
        except ValueError: 
            print('entrada invalida. digite um número entre 0 e 10')      
def calcular (): 
    print('Bem vindo ao sistema de calculo de notas')
    nome = input('Digite seu nome completo: ')
    
    materias = ['Matemática', 'Português', 'Inglês', 'História']
    notas = [] 
    for materia in materias:
        notas.append(obter_nota(materia))
    media = sum(notas) / len(notas)
    
    print(f'\nAluno: {nome}')
    print(f'media: {media:.1f}')
    if media >= 5:
        print('Aprovado')
    else:
        print('Reprovado')
        
if __name__ == '__main__':
    calcular()
    
   