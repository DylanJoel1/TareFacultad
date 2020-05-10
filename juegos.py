import hangman
import reversegam
import tictactoeModificado
import json
import PySimpleGUI as sg
import json
import time





def main(args):
	
	# color de la ventana
	sg.theme('Topanga')  

	# Datos del jugador

	layoutDatos = [
		[sg.Text('ingrese su nombre: ')],
		[sg.Text('Nombre', size=(15, 1)), sg.InputText()],
		[sg.Submit(), sg.Cancel()]
	]

	window = sg.Window('Jugador/a', layoutDatos)
	#Me guardo los datos del jugador ingresados por teclado en "datos_jugador"
	
	e, datos_jugador = window.read()
	window.close()

	
	
	sigo_jugando = True
	while sigo_jugando:		
		# color de la ventana
		sg.theme('Topanga')
		 
		layoutMenu = [[sg.Text('Bienvenidx' + ' ' +datos_jugador[0]+ '. ' + 'Elegí con qué juego querés jugar: \n 1.- ahorcado \n 2.- TA-TE-TE \n 3.- Otello \n 4.- Salir '), sg.Text(size=(15,1), key='-Salida-')],
				 [sg.Input(key='-IN-')],
				 [sg.Button('Enter')]]

		window = sg.Window('Juegos', layoutMenu)
		
		#Espera a que se ingrese un valor por teclado
		while True: 
			evento, opcion = window.read()
			if evento == 'Enter':
				opcion = opcion['-IN-']
				break

		window.close()
		#Dependiendo de lo ingresado entra a un juego
		if opcion == '1':
			hangman.main()
			nombre_juego = 'ahorcado'
		elif opcion == '2':
			tictactoeModificado.main()
			nombre_juego = 'TA-TE-TI'
		elif opcion == '3':
			reversegam.main()
			nombre_juego = 'Otello'
		elif opcion == '4':
			sigo_jugando = False
		
		#Genero el archivo con los datos del jugador
		archivo = open("Player.txt", "w")
		datos_Jugador = [{'nombre': datos_jugador[0], 'fecha': time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()), 'Juego': nombre_juego }]
		json.dump(datos_Jugador, archivo)
		archivo.close()
	
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
