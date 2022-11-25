print()
print('   Diseña tu Vaquero   ')
print('_______________________')
print()
print()

print('   Menu Principal   ')
print('____________________')

Menu=int(input("\n 1-REGISTRARSE \n 2-SELECCIONAR PANTALON VAQUERO \n 3-PAGAR \n 4-CODIGO DE SEGUIMIENTO \n 5-SALIR \n Selecciona Numero:  "))
while Menu!=0:
    if Menu==1:
        print()
        print('   Registro   ')
        print('______________')
        Nombre=input('Nombre: ')
        Apellidos:input('Apellidos: ')
        dni=input('DNI: ')
        Correo=input('Correo Electronico: ')
        Tlf=input('Telf: ')

    elif Menu==2:
        print()
        print('   TU ESTILO   ')
        print('_______________')
        print()
        print('1-Cargo')
        print('2-Slim')
        print('3-Super Skinny')
        print('4-Skinny')
        print('5-Campana')

        Menu1=int(input('Que estilo quieres Nº: '))
        if Menu1==1:
            print()
            print('Has elegido Cargo')
        elif Menu1==2:
            print()
            print('Has elegido Slim')
        elif Menu1==3:
            print()
            print('Has elegido Super Skinny')
        elif Menu1==4:
            print()
            print('Has elegido Skinny')
        elif Menu1==5:
            print()
            print('Has elegido Campana')
        else:
            print()
            print('Ese estilo no esta')
            print()

        print('   TU TALLA   ')
        print('______________')
        print()
        print('1-XXS')
        print('2-XS')
        print('3-S')
        print('4-M')
        print('5-L')

        Menu2=int(input('Que talla quieres Nº: '))
        if Menu2==1:
            print()
            print('Has elegido XXS')
        elif Menu2==2:
            print()
            print('Has elegido XS')
        elif Menu2==3:
            print()
            print('Has elegido S')
        elif Menu2==4:
            print()
            print('Has elegido M')
        elif Menu2==5:
            print()
            print('Has elegido L')
        else:
            print()
            print('Esa talla no esta')
            print()
        
        print('   TU COLOR   ')
        print('______________')
        print()
        print('1-Azul')
        print('2-Negro')
        print('3-Blanco')
        print('4-Marron')
        print('5-Verde Militar')

        Menu3=int(input('Que color quieres Nº: '))
        if Menu3==1:
            print()
            print('Has elegido Azul')
        elif Menu3==2:
            print()
            print('Has elegido Negro')
        elif Menu3==3:
            print()
            print('Has elegido Blanco')
        elif Menu3==4:
            print()
            print('Has elegido Marron')
        elif Menu3==5:
            print()
            print('Has elegido Verde Militar')
        else:
            print()
            print('Ese color no esta')
            print()

    elif Menu==3:
        print()
        print('   Efectuar Pago   ')
        print('___________________') 
        NTarjeta=input('Nª Tarjeta: ')
        FValidez=input('Valida Hasta: ')
        cvv=input('CVV: ')
        print()
        print(f'La factura se enviara al siguiente correo: {Correo}')
        print()

    elif Menu==4:
        print()
        print(f'Su codigo de seguimiento se le enviara al {Tlf} y a {Correo}')
        print()

    elif Menu==5:
        break
    
    else:
        print()
        print('Esa eleccion no existe')
    print()
    print('   Menu Principal   ')
    print('____________________')
    Menu=int(input("\n 1-REGISTRARSE \n 2-SELECCIONAR PANTALON VAQUERO \n 3-PAGAR  \n 4-CODIGO DE SEGUIMIENTO \n 5-SALIR \n Selecciona Numero:  "))
