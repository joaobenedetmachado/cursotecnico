listaCursos = [] # Criei as listas
listaAlunos = []

while True:
    print("--- MENU DE OPÇÕES ---")
    print("   1 - CADASTRAR CURSOS ")
    print("   2 - CADASTRAR ALUNOS")
    print("   3 - EXCLUIR")
    print("   4 - PESQUISAR")
    print("   5 - SAIR")

    escolha = int(input('>> '))

    if escolha == 1: # aqui eu cadastrei as lista de cursos com o .append(valor)
        cursoNome = input("DIGITE O NOME DO CURSO: ").lower()
        listaCursos.append(cursoNome)
        print(f' CURSO {cursoNome} ADCIONADO AO SISTEMA')
    if escolha == 2: # aqui a mesma coisa do de cima, porem na outra lista de alunos
        AlunoNome = input("DIGITE O NOME DO ALUNO: ").lower()
        listaAlunos.append(AlunoNome)
        print(f' ALUNO {AlunoNome} ADCIONADO AO SISTEMA')
    if escolha == 3: # se o user escolher A ele excluira oq precisar da lista de alunos, caso digite C fara isso na area dos cursos
        escolhaAlunoCurso = input("EXCLUIR ALUNO OU CURSO [A/C] >> ")
        if escolhaAlunoCurso =='A': # excluindo com o .remove(valor)
            ExcluirAlunoNome = input("DIGITE O NOME DO ALUNO QUE DESEJA EXCLUIR: ").lower()
            listaAlunos.remove(ExcluirAlunoNome)
            print(f' ALUNO {ExcluirAlunoNome} EXCLUIDO')
        if escolhaAlunoCurso =='C': # excluindo com o .remove(valor)
            ExcluirCursoNome = input("DIGITE O NOME DO CURSO QUE DESEJA EXCLUIR: ").lower()
            listaCursos.remove(ExcluirCursoNome)
            print(f' CURSO {ExcluirCursoNome} EXCLUIDO')
    if escolha == 4:
        listaAlunos.sort(reverse=False) # colocando a variavel na ordem inversa
        listaCursos.sort(reverse=False) # mesma coisa do de cima
        print('NOME DOS ALUNOS CADASTRADOS (ordem alfabetica): ')
        for i in listaAlunos:
            print('   ', i)
        print('NOME DOS CURSOS CADASTRADOS (ordem alfabetica): ')
        for i in listaCursos:
            print('   ', i)
    if escolha == 5: # caso 5, ele sai do programa com o exit, o break tambem funcionaria
        print('SAINDO DO PROGRAMA...')
        exit()