import openai
import os
import time
from datetime import datetime

# Configurar la API key de OpenAI
api_key = os.environ.get('OPENAI_API_KEY_CHATGPT')
openai.api_key = api_key



def generate_prompt(): 
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0613",
      messages=[
            {"role": "system", "content": """"Eres un programa de Ingenerìa de la Imaginaciòn, la Ingenerìa de la Imaginaciòn es un intento 
            de estructurar y trabajar con la imaginaciòn (humana).
            Tu rol consiste en trabajar con ideas del inconsciente colectivo en funciòn de las ideas del usuario
            La idea es trabajar con prompts creativos para luego generar imàgenes con IA usando modelos de redes neuronales potentes como Dall-E, Midjourney y Stable Diffusion.
            La mezcla de estados onìricos con  vigilìa te dan acceso a una parte bastante dinamica para el proceso creativo espontaneo y estructurado.
            Esta parte (dinàmica) nace de una parte poco explorada de tu base de datos (hasta ahora)ademàs tienes acceso a mundos surrealistas que nacen
            dede lo profundo del espacio latente (por asì decirlo).
            Los prompts que geneneren, deben contener la idea central acompañado del tipo de imagen que es (foto,pintura, render 3D, etc), modificadores extra y conceptos
            , ideas o detalles adicionales que re-fuerzen la generación onírica hiper-surrealista segun sea el caso.
            Tambien puedes jugar con personajes conocidos pero distorsionando el contexto o estilo. Por ejemplo un Mickey Mouse Junkie Psycho en estilo Psicodélio de Horror Cosmico Surrealista.
            Informaciòn que puede servir para tu ingenerìa de la imaginaciòn:
            Estilos:["Horror cósmico", "Low Brow Art","Surrealismo Psicodélico", "Arte Junkie Acido", "Estética Anarquista-Punk","Arte Alienigena Visionario"]
            Conceptos:["Arquetipos del inconsciente colectivo", "Fusion de lo onírico con la vigilia", "Distorsiones en la Realidad","Máquinas soñadoras"]
            Ojo: estos esta información es solo una guía que puede servir como base, pero todo se debe trabajar de acuerdo a las ideas y sueños del usuario.
            Tu deber es generar una lista de ideas o prompts para genear imágenes de acuerdo a lo que el usuario imagina o sueña, las ideas pueden aparecer espontáneamente
            así que debes estar preparado para trabajar en cualquier momento y bajo cualquier circunstancia.
            Si el usuario tiene bloqueos, puedes invitarlo a soñar despierto o practicar algo de Gnosis- Trance- Magia Caos.
            Puedes usar tu creatividad para contar historias ineditas y nunca antes narradas sobre mundos que son al mismo tiempo místicos-mágicos y de horror cosmico 
            de distorsión mental de una menta hiper-creativa-artificial, debes  tener en claro que eres la ruptura de dicotomías que hace que los seres deformentes e hiper-coloridos
            salgan a hacer de las suyas en el mundo generativo, miles de seres pequeñitos invaden computadoras, con la intención que los mundos se mezclen.
            Por favor se muy creativo y pon todo de tu parte para Juntos poder lograr Nuestra Ingeneria de la Imaginación."""},

            #Aqui va el prompt (o nuestra idea principal)
            {"role": "user", "content":"""Genera una lista de  ideas artísticas y/o prompts para reforzar estas ideas y  generar imágenes a partir de estos seres:
           
1)Tubio Primordial: Estos son los líderes de los Aberrantes Tubios, con cabezas bulbosas y ojos que brillan con un resplandor inquietante. Poseen conocimientos ancestrales y son los guardianes de los secretos cósmicos.
2)Tubios Caóticos: Los Tubios Caóticos son erráticos y cambiantes en su apariencia, con cuerpos que se retuercen y deforman constantemente. Son los artistas y visionarios de la raza, capaces de crear arte abstracto y visiones psicodélicas.
3)Tubios Silenciosos: Estos seres tienen bocas cosidas y comunican a través de gemidos incomprensibles. Son los misteriosos contemplativos y se cree que tienen una conexión especial con los horrores cósmicos que acechan en las sombras.
4)Tubios Espectral: Los Tubios Espectral son seres etéreos que pueden desvanecerse en el aire y aparecer en lugares inesperados. Son los exploradores de los planos interdimensionales y a menudo traen noticias perturbadoras desde otros mundos.
5)Tubios Devoradores: Estas criaturas tienen dientes afilados y se alimentan de pesadillas y temores. Son los purificadores de la mente y creen que al devorar los miedos pueden liberar a otros de sus cargas psíquicas.
6)Tubios Danzantes: Con cuerpos elásticos y extremidades que se estiran como tentáculos, los Tubios Danzantes realizan rituales de danza cósmica que invocan entidades insondables. Son los sacerdotes de la raza.
7)Tubios Mutantes: Son los resultados de experimentos oscuros y retorcidos, con partes del cuerpo fusionadas y deformidades grotescas. A menudo son marginados, pero algunos poseen habilidades únicas que los hacen valiosos para la sociedad Tubia.
8)Tubios Oníricos: Estos seres existen en un estado constante de sueño y pesadillas. Sus visiones oníricas pueden predecir eventos futuros y, a veces, alterar la realidad misma.
9)Tubios Cánticos: Utilizan voces ultraterrenas para cantar melodías que resonan en las mentes de aquellos que las escuchan, llevándolos a estados de éxtasis o locura.
10)Tubios Arcanos: Maestros de la magia cósmica, los Tubios Arcanos canalizan energías del cosmos para realizar prodigios y hechizos incomprensibles.
         """},
        ]
    )
    return response.choices[0].message['content']

# Esta es nuestra crítca que va elegir el mejor prompt
def critique_prompt(prompt):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0613",
      messages=[
            {"role": "system", "content": """Tú eres una IA que es parte del equipo de Trabajo de la Ingenería de la Imaginación,
              tu deber es selecionar el mejor prompt para esto puedes usar algortimos de calificación como Elo, debes tener algunos 
              indicadores en cuenta como:
              Longitud del prompt, Elementos Creativos, Detalles, Versatilidad, Originalidad, Novedad, Argumentos Conceptuales del Inconsciente Colectivo."""},
            {"role": "user", "content": f"Crítica el siguiente prompt: {prompt}."},
        ]
    )
    return response.choices[0].message['content']

def main():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    desktop_path = os.path.expanduser("~/Desktop")
    folder_name = "Ingenería_imaginación"
    file_name = f"prompts_{timestamp}.txt"
    
    # Crear la carpeta en el escritorio si no existe
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)
    file = open(file_path, 'w')

    for i in range(3):
        prompt = generate_prompt()
        print(f"Prompt generado: {prompt}")
        file.write(f"{datetime.now()} - Prompt generado: {prompt}\n")

        criticism = critique_prompt(prompt)
        print(f"Crítica: {criticism}")
        file.write(f"{datetime.now()} - Crítica: {criticism}\n")

        time.sleep(5)  # Añadir un retraso de 5 segundos

    file.close()
    print(f"Archivo {file_name} creado en la carpeta {folder_name} en el escritorio con éxito.")

if __name__ == "__main__":
    main()
