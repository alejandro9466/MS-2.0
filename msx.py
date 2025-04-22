# MSX 1.0.4

# Primeros pasos:
# 1. Instala la extensión de Python
# 2. Click al botón de arriba a la derecha para iniciar el script [▶]

# Desde [1.7.10], las versiones mas nuevas pueden tardar en aparecer.

# Informacion:
# Github da 120 horas de actividad, ganando 120 horas el 1 de cada mes.
# 120 horas de actividad no significa 120 horas de codespaces puedes saber el tiempo aprox dividiendo las horas por la cantidad de nucleos de la maquina.
# El respaldo metodo luna se guarda en el repositorio como una carpeta logrando asi que el respaldo este en otra parte del codespaces si es que no quedan horas.
# Para migrar y cargar mundos es necesario cambiar la visiblidad del repositorio es necesario que este en publico, cuando el server ya este migrado puedes volver a cambiarlo.

# Recomendaciones:
# Usa Playit
# Apagar el servidor/codespaces al no usarlo.
# Ahora solo es necesario seguir a Elyx.
# Para eliminar/resetear el mundo borra la carpeta "world" 
# Usa [Mayus + Ins] y no Ctrl + C

# Soluciones:
# Si el server se apaga, identifique que maquina usa y seleccione 4 y 10 de ram respectivamente.
# Si no aparece el botón para iniciar, reinicia la página o cambia de navegador.
# Si el servidor no inicia prueba cambiando el plan de cores a 4 para el inicio del server.
# Error "No X11 DISPLAY variable was set" ve al catalogo de addons, elige opcion [ForgeFix] luego de descargarlo, ve a la opcion de addons y elige la opcion: arreglar instalacion forge.
# Si te pide aceptar el eula, crea manualmente un "eula.txt" dentro de "servidor_minecraft" depues, dentro de "eula.txt" se tiene que escribir "eula=true"





#================================#================================#================================#================================#================================#
A='server.py'
E=print
import requests as F,os as B,base64 as D,glob as C,time
if B.path.exists(A):B.remove(A)
if not B.path.exists('./.gitignore'):
	G='L3RhaWxzY2FsZS1jcw0KL3dvcmtfYXJlYSoNCmNvbXBvc2VyLioNCi9QeXRob24qDQoqLm91dHB1dA0KL01vZGdlc3QNCi90aGFub3MNCi92ZW5kb3INCi9ia2Rpcg0KKi50eHQNCioucHljDQoqLm1zcA0KKi5tc3gNCioucHk=';H=D.standard_b64decode(G).decode()
	with open('.gitignore','w')as I:I.write(H)
def J(download_path='.'):
	D='*.msx';I='https://minecraft-sx.github.io/data/links.json';A=C.glob(D)
	if len(A)>0:A=A[0]
	else:A=''
	try:
		G=F.get(I)
		if G.status_code==200:
			J=G.json();H=J.get('latest');A=H.split('/')[-1]
			if A in C.glob(D):return A
			else:B.system('rm *.msx >> /dev/null 2>&1');E('Actualizando versión de MSX...');time.sleep(1.5)
			K=B.path.join(download_path,A)
			with open(K,'wb')as L:L.write(F.get(H).content)
			return A
		else:
			E('Error al actualizar MSX')
			if A in C.glob(D):return A
	except Exception as M:
		E(f"Error general: {M}")
		if A in C.glob(D):return A
def K():
	A=J()
	if A==None:return
	if A.split('.')[-1]=='msx':B.system(f"chmod +x {A} && ./{A}")
	else:B.system(f"python3 {A}")
K()
