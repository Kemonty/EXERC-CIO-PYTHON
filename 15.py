#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
valorhora = int(input("Valor por hora:R$"))
horastrabalhada = int(input("Total de horas trabalhada:"))
Salariobruto = valorhora * horastrabalhada
print ("Salário Bruto Mês:R$", Salariobruto) 
print ("Desconto IR:R$", Salariobruto*0.11 )
print ("Desconto INSS:R$", Salariobruto*0.08 )
print ("Desconto SINDICATO:R$", Salariobruto*0.05 )
print ("Salário Liquido Mês : R$" , Salariobruto - (Salariobruto*0.11)-(Salariobruto*0.08)-(Salariobruto*0.05))