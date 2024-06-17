# Suponga dos eventos, A y B, y que P(A) = 0.50, P(B) = 0.60 y P(A ∩ B) = 0.40.<br>
# a. calcule P(A | B).
# P(A | B) = P(A ∩ B) / P(B)
print("P(A | B) = P(A ∩ B) / P(B) = 0.40 / 0.60 = ", 0.40 / 0.60)

# Halle P(B | A).
# P(B | A) = P(A ∩ B) / P(A)
print("P(B | A) = P(A ∩ B) / P(A) = 0.40 / 0.50 = ", 0.40 / 0.50)

#P(AyB) = P(A) *  P(B)
print("P(AyB) = P(A) *  P(B) = 0.50 * 0.60 = ", 0.50 * 0.60)

# c. ¿A y B son independientes? ¿Por qué sí o por qué no?
# A y B son independientes si P(A ∩ B) = P(A) * P(B)
# P(A ∩ B) = 0.40
# P(A) * P(B) = 0.50 * 0.60 = 0.30
# Como P(A ∩ B) ≠ P(A) * P(B), A y B no son independientes.

#3. Si en la concesionaria se seleccionan dos ventas con reposición (Los sucesos son independientes.). Hallar la probabilidad de que las ventas sean:<br>
#a. La primera de un comprador de “menos de 40 años” y la segunda de uno de "entre 40 y 50 años". 
# A = P(comprador de “menos de 40 años”) = 30
# B = P(comprador de "entre 40 y 50 años") = 34
# Total = 80
# P(A) = 30/80
# P(B) = 34/80
# P(A) * P(B) = 30/80 * 34/80
print("P(A) * P(B) = 30/80 * 34/80 = ", 30/80 * 34/80)
  
#b. las dos sean de autos "nacionales".
# A = P(autos "nacionales") = 50
print("P(A) * P(A) = 50/80 * 50/80 = ", 50/80 * 50/80)

#4. Si la selección de las dos ventas se realiza sin reposición. Hallar la probabilidad de que las ventas sean: Los sucesos son condicionales.
#a. la primera de un comprador de “menos de 40 años” y la segunda de uno de "entre 40 y 50 años".
# A = P(comprador de “menos de 40 años”) = 30
# B = P(comprador de "entre 40 y 50 años") = 34
# Total = 80
# P(A) = 30/80
# P(B) = 34/79
# P(A) * P(B) = 30/80 * 34/79
print("P(A) * P(B) = 30/80 * 34/79 = ", 30/80 * 34/79)

#b. las dos sean de autos "nacionales".
# A = P(autos "nacionales") = 50
# P(A) * P(A) = 50/80 * 49/79
print("P(A) * P(A) = 50/80 * 49/79 = ", 50/80 * 49/79)

#5. Si la selección de las dos ventas se realiza sin reposición. Hallar la probabilidad de que las ventas sean:<br>
#Los sucesos son condicionales.
# a. De un comprador de “menos de 40 años” y de uno de "entre 40 y 50 años". Sin importar el orden.
# A = P(comprador de “menos de 40 años”) = 30
# B = P(comprador de "entre 40 y 50 años") = 34
# Total = 80
# P(A) = 30/80
# P(B) = 34/80

print("P(A) * P(B) = 30/80 * 34/79 + 34/80 * 30/79 = ", 30/80 * 34/79 + 34/80 * 30/79)


