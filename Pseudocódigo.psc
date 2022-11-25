Algoritmo Hito_Individual
	Repetir
		
		
		Escribir "    Menu Principal   "
		Escribir "_____________________"
		Escribir " "
		Escribir "1-Registrarse"
		Escribir "2-Seleccionar Pantalon"
		Escribir "3-Pagar"
		Escribir "4-Codigo de seguimiento"
		Escribir "5-Salir"
		Escribir "Eleccion Nº: "
		Leer OP
		Segun OP Hacer
			1:
				Escribir "Nombre: "
				Leer Nombre
				Escribir "Apellidos: "
				Leer Apellidos
				Escribir "DNI: "
				Leer DNI
				Escribir "Tlf: "
				Leer Tlf
				Escribir "Correo: "
				Leer Correo
			2:
				Escribir "   Estilo   "
				Escribir "____________"
				Escribir " "
				Escribir "1-Cargo"
				Escribir "2-Slim"
				Escribir "3-Super Skinny"
				Escribir "4-Skinny"
				Escribir "5-Campana"
				Escribir "Eleccion Nº: "
				Leer OP
				Segun OP Hacer
					1:
						Escribir "Has elegido Cargo"
					2:
						Escribir "Has elegido Slim"
					3:
						Escribir "Has elegido Super Skinny"
					4:
						Escribir "Has elegido Skinny"
					5:
						Escribir "Has elegido Cargo"
				FinSegun
				Escribir "   Talla   "
				Escribir "____________"
				Escribir " "
				Escribir "1-XXS"
				Escribir "2-XS"
				Escribir "3-S"
				Escribir "4-M"
				Escribir "5-L"
				Escribir "Eleccion Nº: "
				Leer Talla
				Segun OP Hacer
					1:
						Escribir "Has elegido XXS"
					2:
						Escribir "Has elegido XS"
					3:
						Escribir "Has elegido S"
					4:
						Escribir "Has elegido M"
					5:
						Escribir "Has elegido L"
				FinSegun
				Escribir "   COLOR   "
				Escribir "____________"
				Escribir " "
				Escribir "1-Azul"
				Escribir "2-Blanco"
				Escribir "3-Negro"
				Escribir "4-Marron"
				Escribir "5-Verde Militar"
				Escribir "Eleccion Nº: "
				Leer Color
				Segun Color Hacer
					1:
						Escribir "Has elegido Azul"
					2:
						Escribir "Has elegido Blanco"
					3:
						Escribir "Has elegido Negro"
					4:
						Escribir "Has elegido Marron"
					5:
						Escribir "Has elegido Verde Militar"
				FinSegun
			3:
				Escribir "Tarjeta: "
				Leer Tarjeta
				Escribir "CVV: "
				Leer CVV
				Escribir "La factura sera enviada a la siguiente direccion de correo " Correo
			4:
				Escribir "Su codigo de seguimiento sera envisado al " Tlf " y al siguiente correo " Correo 
			5:
			De Otro Modo:
				Escribir "Eleccion no valida"
		Fin Segun  
	Hasta Que OP=5	
	Escribir "Hasta la Proxima"
	
FinAlgoritmo
