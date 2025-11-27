import os
import tweepy
from datetime import date

# 1. Configuración de Autenticación
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_secret = os.environ.get("ACCESS_SECRET")

def publicar_tweet():
    # 2. Calcular el tiempo exacto
    ultima_champions = date(2015, 6, 6)
    hoy = date.today()
    
    # Diferencia total absoluta
    diferencia_total = hoy - ultima_champions
    
    # Cálculo manual de Años + Días restantes
    # Verificamos cuántos años completos han pasado
    anios = hoy.year - ultima_champions.year
    aniversario_este_anio = date(hoy.year, 6, 6)
    
    # Si aún no llegamos a junio de este año, restamos un año
    if hoy < aniversario_este_anio:
        anios -= 1
        ultimo_aniversario = date(hoy.year - 1, 6, 6)
    else:
        ultimo_aniversario = aniversario_este_anio
    
    # Los días sobrantes son desde el último aniversario (junio) hasta hoy
    dias_sobrantes = (hoy - ultimo_aniversario).days
    
    # 3. Construir el mensaje EXACTO
    txt_anos = "año" if anios == 1 else "años"
    txt_dias = "día" if dias_sobrantes == 1 else "días"
    
    # NOTA: {:,} pone la coma de miles automáticamente (Ej: 3,827)
    # Sin punto final.
    mensaje = (
        f"El Barcelona lleva {diferencia_total.days:,} días sin ganar la Champions League "
        f"({anios} {txt_anos}, {dias_sobrantes} {txt_dias})"
    )
    
    print(f"Nuevo mensaje exacto: {mensaje}")

    # 4. Conectar y Publicar
    if not api_key:
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
    
