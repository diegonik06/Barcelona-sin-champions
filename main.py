import os
import tweepy
from datetime import date
from dateutil.relativedelta import relativedelta

# 1. Configuración de Autenticación
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_secret = os.environ.get("ACCESS_SECRET")

def publicar_tweet():
    # 2. Calcular el tiempo (Desde el 6 de junio de 2015)
    ultima_champions = date(2015, 6, 6)
    hoy = date.today()
    
    diferencia_total = hoy - ultima_champions
    desglose = relativedelta(hoy, ultima_champions)
    
    # 3. Construir el mensaje
    txt_anos = "año" if desglose.years == 1 else "años"
    txt_dias = "día" if desglose.days == 1 else "días"
    
    mensaje = (
        f"El Barcelona lleva {diferencia_total.days:,} días sin ganar una Champions "
        f"({desglose.years} {txt_anos}, {desglose.days} {txt_dias})."
    ).replace(",", ".") 
    
    print(f"Tweet a publicar: {mensaje}")

    # 4. Conectar y Publicar
    if not api_key:
        print("No se encontraron las claves. Asegúrate de configurar los SECRETS.")
        return

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret
    )
    
    try:
        client.create_tweet(text=mensaje)
        print("Tweet enviado con éxito.")
    except Exception as e:
        print(f"Error: {e}")
        raise e

if __name__ == "__main__":
    publicar_tweet()
  
