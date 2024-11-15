#Gutierrez Hernandez Kevin Andrew

from sympy import symbols, expand
from sympy import pprint
class Orden:
    def orden_1_g(self):
        x = symbols('x')
        print("---Digite los valores de x y f(x)---")
        x0 = float(input("Digite el valor de x0: "))
        fx0 = float(input("Digite el valor de f(x0): "))
        x1 = float(input("Digite el valor de x1: "))
        fx1 = float(input("Digite el valor de f(x1): "))

        term1 = ((x - x1) / (x0 - x1)) * fx0
        term2 = ((x - x0) / (x1 - x0)) * fx1
        print("Término 1:", term1)
        print("Término 2:", term2)

        orden_lg = expand(term1 + term2)
        print("Su ecuación de orden 1 es: " + str(orden_lg))
        
        Ax = float(input("Digite el valor de aproximación x: "))
        orden1_lg = term1.subs(x, Ax) + term2.subs(x, Ax)
        print("Su resultado es: " + str(orden1_lg))
        return

    def orden_2_g(self):
        x = symbols('x')
        print("---Digite los valores de x y f(x)---")
        x0 = float(input("Digite el valor de x0: "))
        fx0 = float(input("Digite el valor de f(x0): "))
        x1 = float(input("Digite el valor de x1: "))
        fx1 = float(input("Digite el valor de f(x1): "))
        x2 = float(input("Digite el valor de x2: "))
        fx2 = float(input("Digite el valor de f(x2): "))

        term1 = (((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))) * fx0
        term2 = (((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))) * fx1
        term3 = (((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))) * fx2
        pprint("Término 1:", term1)
        pprint("Término 2:", term2)
        pprint("Término 3:", term3)

        orden2_lg = expand(term1 + term2 + term3)
        print("Su ecuación de orden 2 es: " + str(orden2_lg))
        
        Ax2 = float(input("Digite el valor de aproximación x: "))
        orden2 = term1.subs(x, Ax2) + term2.subs(x, Ax2) + term3.subs(x, Ax2)
        print("Su resultado es: " + str(orden2))
        return

    def orden_3_g(self):
        x = symbols('x')
        print("---Digite los valores de x y f(x)---")
        x0 = float(input("Digite el valor de x0: "))
        fx0 = float(input("Digite el valor de f(x0): "))
        x1 = float(input("Digite el valor de x1: "))
        fx1 = float(input("Digite el valor de f(x1): "))
        x2 = float(input("Digite el valor de x2: "))
        fx2 = float(input("Digite el valor de f(x2): "))
        x3 = float(input("Digite el valor de x3: "))
        fx3 = float(input("Digite el valor de f(x3): "))

        term1 = (((x - x1) * (x - x2) * (x - x3)) / ((x0 - x1) * (x0 - x2) * (x0 - x3))) * fx0
        term2 = (((x - x0) * (x - x2) * (x - x3)) / ((x1 - x0) * (x1 - x2) * (x1 - x3))) * fx1
        term3 = (((x - x0) * (x - x1) * (x - x3)) / ((x2 - x0) * (x2 - x1) * (x2 - x3))) * fx2
        term4 = (((x - x0) * (x - x1) * (x - x2)) / ((x3 - x0) * (x3 - x1) * (x3 - x2))) * fx3
        pprint("Término 1:", term1)
        pprint("Término 2:", term2)
        pprint("Término 3:", term3)
        pprint("Término 4:", term4)

        orden3_lg = expand(term1 + term2 + term3 + term4)
        print("Su ecuación de tercer orden es: " + str(orden3_lg))
        
        Ax3 = float(input("Digite el valor de aproximación x: "))
        orden3 = term1.subs(x, Ax3) + term2.subs(x, Ax3) + term3.subs(x, Ax3) + term4.subs(x, Ax3)
        print("Su resultado es: " + str(orden3))
        return

def main():
    opc = 0
    o = Orden()
    while opc != 4:
        print("\nMenu de opciones")
        print("1. Lagrange orden 1")
        print("2. Lagrange orden 2")
        print("3. Lagrange orden 3")
        print("4. Salir")
        opc = int(input("Elija una opción: "))

        if opc == 1:
            o.orden_1_g()
        elif opc == 2:
            o.orden_2_g()
        elif opc == 3:
            o.orden_3_g()
        elif opc == 4:
            print("Saliendo...")
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
