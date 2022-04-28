# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:26:38 2022

"""
#Guido's Gorgeous Lasagna

#Instructions
# You're going to write some code to help you cook a gorgeous lasagna
# from your favorite cookbook.

# You have five tasks, all related to cooking your recipe.

# Definicion de tiempo de horneado.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time):
    """Calcular el tiempo de horneado restante.
 
    :param elapsed_bake_time: int tiempo de horneado ya transcurrido
    :return: int tiempo de horneado restante (en minutos) derivado de 'EXPECTED_BAKE_TIME'
 
    Función que toma los minutos reales que la lasaña ha estado en el horno como
    una discusión y devuelve cuántos minutos le falta hornear a la lasaña
    basado en el `EXPECTED_BAKE_TIME`.
   """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    """Calcular el tiempo de preparación.
 
     :param number_of_layers: int el número de capas de lasaña hechas
     :return: int cantidad de tiempo de preparación (en minutos), basado en 2 minutos 
      por capa añadida
 
     Esta función toma un número entero que representa el número de capas añadidas al 
     plato, calculando el tiempo de preparación utilizando un tiempo de 2 minutos por 
     capa añadida.
     """
    return number_of_layers * PREPARATION_TIME
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calcular el tiempo transcurrido.
 
     :param number_of_layers: int el número de capas en la lasaña
     :param elapsed_bake_time: int tiempo de cocción transcurrido
     :return: int tiempo total transcurrido (en minutos) preparando y cocinando
 
     Esta función toma dos números enteros que representan el número de capas de lasaña 
     y el tiempo de horneado y calcula el total de minutos transcurridos en la cocción 
     de la lasaña.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


 