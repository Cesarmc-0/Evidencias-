import random
preguntas={
  1:[
    {'pregunta':'¿Cuántos continentes hay en el mundo?','opciones':['a)5','b)6', 'c)7', 'd)8'], 'respuesta':'c)7'},
    {'pregunta':'¿En qué país se encuentra la Torre Eiffel?','opciones':['a)Italia','b)francia', 'c)alemania', 'd)Español'],'respuesta':'b)francia'}
],
2:[
    {'pregunta':'¿Cuál es el océano más grande del planeta?','opciones':['a)Atlántico','b)Índico', 'c) Ártico', 'd)Pacífico'],'respuesta':'d)Pacífico'},
    {'pregunta':'¿Quién pintó la Mona Lisa?','opciones':['a) Vincent van Gogh','b) Pablo Picasso','c) Leonardo da Vinci', 'd) Miguel Ángel'],'respuesta':'c) Leonardo da Vinci'}
],
3:[
    {'pregunta':'¿Cuál es la capital de España?','opciones':['a)Barcelona','b)Madrid', 'c) Valencia', 'd)Sevilla'],'respuesta':'b)Madrid'},
    {'pregunta':' ¿Cuál es el resultado de 9 x 6?','opciones':['a)54','b)15','c)63', 'd)71'],'respuesta':'a)54'}
],
4:[
    {'pregunta':'¿Qué gas respiramos para vivir?','opciones':['a)Hidrógeno','b)Oxígeno', 'c) Dióxido de carbono', 'd)Nitrógeno'],'respuesta':'b)Oxígeno'},
    {'pregunta':'¿Qué continente es conocido por su forma triangular y la presencia del desierto del Sahara?','opciones':['a)Asia','b)América','c)África', 'd)Oceanía'],'respuesta':'c)África'}
],
5:[
    {'pregunta':'¿Qué país tiene forma de bota en el mapa de Europa?','opciones':['a) España','b)Portugal', 'c)Italia', 'd)Grecia'],'respuesta':'c)Italia'},
    {'pregunta':' ¿Cuál es el idioma más hablado en el mundo como lengua materna?','opciones':['a)Inglés','b)Español','c)Chino mandarín', 'd)Árabe'],'respuesta':'c)Chino mandarín'}
],
6:[
    {'pregunta':'¿Qué científico formuló la teoría de la relatividad?','opciones':['a)Isaac Newton','b)Albert Einstein', 'c) Nikola Tesla', 'd) Galileo Galilei'],'respuesta':'b)Albert Einstein'},
    {'pregunta':' ¿Cuál es el país con más premios Nobel de la Paz?','opciones':['a) Alemania ','b) Noruega','c) Estados Unidos', 'd) Francia'],'respuesta':'c) Estados Unidos'}
],
7:[
    {'pregunta':'¿Qué guerra comenzó en 1914?','opciones':['a) Segunda Guerra Mundial','b) Guerra Fría ', 'c) Guerra de Vietnam', 'd) Primera Guerra Mundial '],'respuesta':'d) Primera Guerra Mundial '},
    {'pregunta':'¿Cuál es el nombre completo del escritor conocido como Shakespeare?','opciones':['a) John Shakespeare ','b) William Shakespeare','c) Richard Shakespeare ', 'd) Henry Shakespeare'],'respuesta':'b) William Shakespeare'}
],
8:[
    {'pregunta':'¿Qué país tiene el mayor número de volcanes activos?','opciones':['a) Japón','b) Chile ', 'c) Indonesia', 'd) Islandia '],'respuesta':'c) Indonesia'},
    {'pregunta':'¿Qué elemento químico tiene el símbolo W?','opciones':['a) Plomo','b) Zinc','c) Wolframio ', 'd) Mercurio'],'respuesta':'c) Wolframio '}
],
9:[
    {'pregunta':'¿Cuál es la capital de Mongolia?','opciones':['a) Katmandú ','b) Ulán Bator ', 'c) Tashkent', 'd) Bishkek '],'respuesta':'b) Ulán Bator '},
    {'pregunta':'¿Quién fue el primer ser humano en realizar una caminata espacial?','opciones':['a) Yuri Gagarin','b) Neil Armstrong','c) Buzz Aldrin ', 'd) Alexei Leonov'],'respuesta':'d) Alexei Leonov'}
],
10:[
    {'pregunta':'¿Qué filósofo escribió La crítica de la razón pura?','opciones':['a)  Karl Marx ','b) René Descartes ', 'c) Immanuel Kant', 'd) Friedrich Nietzsche '],'respuesta':'c) Immanuel Kant'},
    {'pregunta':'¿Qué matemático es considerado el padre de la informática?','opciones':['a) Blaise Pascal','b) Isaac Newton','c) Alan Turing ', 'd) Gottfried Leibniz'],'respuesta':'c) Alan Turing '}
]
}
print("BIENVENIDO A QUIEN QUIERE SER MILLONARIO")
print("-"* 160)
holi = 1
chao = 0
dinero = 50000
comodines = ["1.llama a un amigo ","2.50/50","3.cambio de pregunta"]
llamada = ['a','b','c','d']
llama= [preguntas[holi][chao]['opciones'][0],preguntas[holi][chao]["respuesta"]]
for i in preguntas:
    for p in preguntas[i]:
        print(f"Responda la siguiente pregunta:{preguntas[holi][chao]["pregunta"]} ")
        for j in preguntas[holi][chao]['opciones']:
            print(j)
        while len(comodines) >0:
            comodin= input("deseas utilizar un comodin?").upper()
            if comodin == "SI":
                for i in comodines:
                    print(i)
                como = int(input("elija el numero del comodin. "))
                if como == 2:
                    print(f"Responda la pregunta:{preguntas[holi][chao]["pregunta"]} ")
                    print(preguntas[holi][chao]['opciones'][0])
                    print(preguntas[holi][chao]["respuesta"])
                    comodines.remove("2.50/50")
                elif como == 1 :
                    amigo = random.choice(llama)
                    print(f"Tu amigo recomienda la opcion: {amigo}")
                    comodines.remove("1.llama a un amigo ")
                    print(f"Responda la pregunta:{preguntas[holi][chao]["pregunta"]} ")
                    if len(comodines) < 2:
                        print(preguntas[holi][chao]['opciones'][0])
                        print(preguntas[holi][chao]["respuesta"])
                    else:
                        for j in preguntas[holi][chao]['opciones']:
                            print(j)                           
                elif como == 3:
                    chao += 1
                    print(f"Su pregunta ahora es {preguntas[holi][chao]["pregunta"]}")
                    for o in preguntas[holi][chao]['opciones']:
                        print(o)
                    comodines.remove("3.cambio de pregunta")
            else:
                print("Responde tu respuesta sin comodin")
                break         
        respuesta= input("ingresa tu respuesta: ").lower()
        if respuesta == (preguntas[holi][chao]['respuesta'][0]):
            print("RESPUESTA CORRECTA")
            dinero *= 2
            print(f"tu dinero ganado es :{dinero}")
            holi += 1
            while holi <=10:
                retirar = input("Deseas retirarte del juego: ").lower()
                if retirar == "si":
                    print(f"TU DINERO GANADO FUE {dinero}, GRACIAS POR JUGAR.")
                    exit()
                else:
                    break
        else:
            print("RESPUESTA INCORRECTA.")
            print(f"TU DINERO GANADO FUE {dinero}, GRACIAS POR JUGAR.")
            exit()