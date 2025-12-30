# Estadísticas de Darkroom

Este archivo explica cómo configurar el visualizador de estadísticas de Google Analytics.

## Configuración rápida

### 1. Instalar dependencias

```bash
pip install google-analytics-data google-auth
```

### 2. Crear cuenta de servicio en Google Cloud

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un proyecto nuevo o selecciona uno existente
3. Habilita la **Google Analytics Data API**:
   - Menu > APIs y servicios > Biblioteca
   - Busca "Google Analytics Data API"
   - Clic en Habilitar

4. Crear cuenta de servicio:
   - Menu > APIs y servicios > Credenciales
   - Crear credenciales > Cuenta de servicio
   - Dale un nombre (ej: "darkroom-stats")
   - Clic en Crear y continuar
   - Rol: Ninguno (lo daremos en GA)
   - Clic en Listo

5. Descargar credenciales JSON:
   - Clic en la cuenta de servicio creada
   - Pestaña "Claves"
   - Agregar clave > Crear clave nueva
   - Tipo: JSON
   - Se descargará un archivo `.json`

6. Guarda el archivo como `ga-credentials.json` en la carpeta Darkroom

### 3. Dar acceso en Google Analytics

1. Ve a [Google Analytics](https://analytics.google.com/)
2. Admin > Acceso a la propiedad
3. Clic en el + para agregar usuarios
4. Pega el email de la cuenta de servicio (termina en @*.iam.gserviceaccount.com)
5. Rol: **Lector**
6. Clic en Agregar

### 4. Obtener tu Property ID

1. En Google Analytics: Admin > Detalles de la propiedad
2. Copia el "ID de propiedad" (números como: 123456789)
3. Edita `ver_estadisticas.py` línea 31:
   ```python
   PROPERTY_ID = "123456789"  # Tu ID aquí
   ```

### 5. Ejecutar el programa

```bash
python ver_estadisticas.py
```

## Qué muestra el programa

- ✅ Usuarios únicos
- ✅ Total de vistas de página
- ✅ Sesiones totales
- ✅ Top 10 páginas más vistas
- ✅ Visitas diarias de la última semana

## Opciones del menú

1. **Últimos 7 días** - Resumen semanal
2. **Últimos 30 días** - Resumen mensual
3. **Últimos 90 días** - Resumen trimestral

## Solución de problemas

### Error: "Property ID no encontrado"
- Verifica que el Property ID sea correcto en la línea 31
- Debe ser solo números, sin espacios

### Error: "Permission denied"
- Verifica que la cuenta de servicio tenga acceso en Google Analytics
- El email debe estar en Admin > Acceso a la propiedad con rol Lector

### Error: "API not enabled"
- Asegúrate de habilitar "Google Analytics Data API" en Google Cloud Console

---

**Nota**: Las estadísticas pueden tardar hasta 24-48 horas en aparecer en Google Analytics después de la primera configuración.
