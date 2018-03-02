def test_pull_request():
	#Abrir archivo y guardar sus lineas
	funciones = open('./API_web.py')
	test = open('./API_web_test.py')
	lineas_funciones = funciones.readlines()
	lineas_test = test.readlines()
	
	contador_funciones = 0
	contador_test = 0
	
	#Recorremos las lineas de las funciones y nos quedamos con las palabras de una linea
	for l_f in lineas_funciones:
		palabras_f = l_f.split(' ')
		#Recorremos las palabras y guardamos el nombre de la funcion principal
		for p_f in palabras_f:
			if p_f=='def':
				nombre_funcion = palabras_f[1]
				contador_funciones = contador_funciones + 1
				#Recorremos las lineas de los test y nos quedamos con las palabras de una linea
				for l_t in lineas_test:
					palabras_t = l_t.split(' ')
					#Recorremos las palabras y guardamos el nombre de la funcion principal
					for p_t in palabras_t:
						if p_t=='def':
							nombre_test = palabras_t[1]
							#Le anyadimos test_ a la funcion y comprobamos que son iguales.
							nombre_funcion_con_test = "test_"+nombre_funcion
							if (nombre_test==nombre_funcion_con_test):
								contador_test = contador_test + 1
	
	return contador_test == contador_funciones
