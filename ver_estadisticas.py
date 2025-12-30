"""
Visualizador de estadísticas de Google Analytics para Darkroom
Muestra visitas, páginas más vistas y datos de audiencia
"""

import os
import sys
from datetime import datetime, timedelta

try:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        DateRange,
        Dimension,
        Metric,
        RunReportRequest,
    )
    from google.oauth2 import service_account
except ImportError:
    print("❌ Error: No se encontró la librería de Google Analytics.")
    print("\nPara instalar, ejecuta:")
    print("pip install google-analytics-data google-auth")
    sys.exit(1)

# ID de la propiedad de Google Analytics 4
PROPERTY_ID = "TU_PROPERTY_ID"  # Reemplazar con tu Property ID de GA4

def obtener_credenciales():
    """
    Busca las credenciales del archivo JSON de la cuenta de servicio
    """
    credentials_path = "ga-credentials.json"
    if not os.path.exists(credentials_path):
        print("❌ No se encontró el archivo 'ga-credentials.json'")
        print("\nPara usar este programa necesitas:")
        print("1. Crear un proyecto en Google Cloud Console")
        print("2. Habilitar la API de Google Analytics Data")
        print("3. Crear una cuenta de servicio y descargar el JSON")
        print("4. Guardar el archivo como 'ga-credentials.json' en este directorio")
        print("5. Darle acceso a esta cuenta en Google Analytics")
        return None
    
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=["https://www.googleapis.com/auth/analytics.readonly"]
    )
    return credentials

def formato_numero(numero):
    """Formatea números con separadores de miles"""
    return f"{int(numero):,}".replace(",", ".")

def obtener_visitas_totales(client, dias=30):
    """Obtiene el total de visitas en los últimos N días"""
    fecha_fin = datetime.now().strftime("%Y-%m-%d")
    fecha_inicio = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d")
    
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        date_ranges=[DateRange(start_date=fecha_inicio, end_date=fecha_fin)],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="screenPageViews"),
            Metric(name="sessions"),
        ],
    )
    
    response = client.run_report(request)
    return response

def obtener_paginas_mas_vistas(client, dias=30, limit=10):
    """Obtiene las páginas más visitadas"""
    fecha_fin = datetime.now().strftime("%Y-%m-%d")
    fecha_inicio = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d")
    
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        date_ranges=[DateRange(start_date=fecha_inicio, end_date=fecha_fin)],
        dimensions=[Dimension(name="pageTitle"), Dimension(name="pagePath")],
        metrics=[Metric(name="screenPageViews")],
        limit=limit,
    )
    
    response = client.run_report(request)
    return response

def obtener_visitas_por_dia(client, dias=7):
    """Obtiene las visitas diarias"""
    fecha_fin = datetime.now().strftime("%Y-%m-%d")
    fecha_inicio = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d")
    
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        date_ranges=[DateRange(start_date=fecha_inicio, end_date=fecha_fin)],
        dimensions=[Dimension(name="date")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="screenPageViews"),
        ],
    )
    
    response = client.run_report(request)
    return response

def mostrar_resumen(client, dias=30):
    """Muestra un resumen de las estadísticas"""
    print("=" * 60)
    print(f"📊 ESTADÍSTICAS DE DARKROOM - Últimos {dias} días")
    print("=" * 60)
    print()
    
    # Visitas totales
    response = obtener_visitas_totales(client, dias)
    if response.row_count > 0:
        row = response.rows[0]
        usuarios = row.metric_values[0].value
        vistas = row.metric_values[1].value
        sesiones = row.metric_values[2].value
        
        print("📈 RESUMEN GENERAL")
        print("-" * 60)
        print(f"   Usuarios únicos:     {formato_numero(usuarios)}")
        print(f"   Vistas de página:    {formato_numero(vistas)}")
        print(f"   Sesiones:            {formato_numero(sesiones)}")
        print()
    
    # Páginas más vistas
    print("🏆 TOP 10 PÁGINAS MÁS VISTAS")
    print("-" * 60)
    response = obtener_paginas_mas_vistas(client, dias, 10)
    
    for i, row in enumerate(response.rows, 1):
        titulo = row.dimension_values[0].value
        ruta = row.dimension_values[1].value
        vistas = row.metric_values[0].value
        
        # Acortar título si es muy largo
        if len(titulo) > 40:
            titulo = titulo[:37] + "..."
        
        print(f"   {i:2}. {titulo:42} | {formato_numero(vistas):>6} visitas")
    
    print()
    
    # Visitas por día (últimos 7 días)
    print("📅 VISITAS POR DÍA (Últimos 7 días)")
    print("-" * 60)
    response = obtener_visitas_por_dia(client, 7)
    
    for row in response.rows:
        fecha_str = row.dimension_values[0].value
        usuarios = row.metric_values[0].value
        vistas = row.metric_values[1].value
        
        # Formatear fecha
        fecha = datetime.strptime(fecha_str, "%Y%m%d")
        fecha_fmt = fecha.strftime("%d/%m/%Y")
        dia_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"][fecha.weekday()]
        
        print(f"   {fecha_fmt} ({dia_semana}) | {formato_numero(usuarios):>5} usuarios | {formato_numero(vistas):>5} vistas")
    
    print()
    print("=" * 60)

def menu_principal():
    """Menú interactivo"""
    print("\n" + "=" * 60)
    print("🎯 ESTADÍSTICAS DE DARKROOM")
    print("=" * 60)
    print("\n1. Ver resumen de últimos 7 días")
    print("2. Ver resumen de últimos 30 días")
    print("3. Ver resumen de últimos 90 días")
    print("4. Salir")
    print()
    opcion = input("Selecciona una opción (1-4): ").strip()
    return opcion

if __name__ == "__main__":
    # Verificar credenciales
    credentials = obtener_credenciales()
    if not credentials:
        sys.exit(1)
    
    # Verificar Property ID
    if PROPERTY_ID == "TU_PROPERTY_ID":
        print("❌ Error: Debes configurar tu PROPERTY_ID en el script")
        print("\nPara encontrar tu Property ID:")
        print("1. Ve a Google Analytics")
        print("2. Admin > Detalles de la propiedad")
        print("3. Copia el ID de la propiedad (números)")
        sys.exit(1)
    
    # Crear cliente
    try:
        client = BetaAnalyticsDataClient(credentials=credentials)
        
        while True:
            opcion = menu_principal()
            
            if opcion == "1":
                mostrar_resumen(client, 7)
            elif opcion == "2":
                mostrar_resumen(client, 30)
            elif opcion == "3":
                mostrar_resumen(client, 90)
            elif opcion == "4":
                print("\n👋 ¡Hasta luego!\n")
                break
            else:
                print("\n❌ Opción inválida. Intenta de nuevo.")
    
    except Exception as e:
        print(f"\n❌ Error al conectar con Google Analytics: {e}")
        print("\nVerifica que:")
        print("- El Property ID sea correcto")
        print("- Las credenciales tengan acceso a esta propiedad")
        print("- La API de Google Analytics Data esté habilitada")
