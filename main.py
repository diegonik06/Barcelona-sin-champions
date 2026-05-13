import os
import tweepy
from datetime import date

# 1. Configuración de Autenticación
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_secret = os.environ.get("ACCESS_SECRET")

def publicar_tweet():
    hoy = date.today()
    
    # Fecha de la última Champions (Berlín 2015)
    ultima_champions = date(2015, 6, 6)
    
    # Diferencia total absoluta
    diferencia_total = hoy - ultima_champions
    
    # Cálculo de Años + Días restantes
    anios = hoy.year - ultima_champions.year
    aniversario_este_anio = date(hoy.year, 6, 6)
    
    if hoy < aniversario_este_anio:
        anios -= 1
        ultimo_aniversario = date(hoy.year - 1, 6, 6)
    else:
        ultimo_aniversario = aniversario_este_anio
    
    dias_sobrantes = (hoy - ultimo_aniversario).days
    
    txt_anos = "año" if anios == 1 else "años"
    txt_dias = "día" if dias_sobrantes == 1 else "días"
    
    mensaje = (
        f"El Barcelona lleva {diferencia_total.days:,} días sin ganar la Champions League "
        f"({anios} {txt_anos}, {dias_sobrantes} {txt_dias})"
    )

    if not api_key:
        print("Error: No hay llaves configuradas.")
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
