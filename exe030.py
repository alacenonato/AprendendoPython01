nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3) /3 #Calcula a méida das notas

if media >= 7 :
    print("Aluno aprovado!")
elif media < 4 :
    print("Aluno reprovado!")
else:
    print("Aluno em recuperação!")
    