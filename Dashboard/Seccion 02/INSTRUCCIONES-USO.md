# Instrucciones de Uso - Generador de Dashboards

## ⚠️ IMPORTANTE: Ubicación Correcta

El script **DEBE** ejecutarse desde el directorio correcto:

```bash
cd /Users/maximilianocalva/Documents/GitHub/Dashboard-IDECF/Dashboard/Seccion\ 02
```

## ✅ Comando Correcto

```bash
python3 generar-alumnos.py
```

## ❌ Error Común

Si ejecutas el script desde otro directorio, verás este error:
```
❌ Error: No se encontró el archivo alumnos-dcf-todas-generaciones.csv
```

**Solución:** Asegúrate de estar en el directorio correcto antes de ejecutar.

## 📁 Archivos Necesarios

El script busca estos archivos en el **mismo directorio**:
- `alumnos-dcf-todas-generaciones.csv` (base de datos)
- `seccion-02-informacion-alumno-idecf.html` (template)

## 🚀 Pasos Completos

1. **Abrir Terminal**

2. **Navegar al directorio correcto:**
   ```bash
   cd /Users/maximilianocalva/Documents/GitHub/Dashboard-IDECF/Dashboard/Seccion\ 02
   ```

3. **Verificar que estás en el lugar correcto:**
   ```bash
   pwd
   ```
   Debe mostrar: `/Users/maximilianocalva/Documents/GitHub/Dashboard-IDECF/Dashboard/Seccion 02`

4. **Listar archivos para confirmar:**
   ```bash
   ls -la *.csv *.html *.py
   ```
   Debes ver:
   - `alumnos-dcf-todas-generaciones.csv`
   - `seccion-02-informacion-alumno-idecf.html`
   - `generar-alumnos.py`

5. **Ejecutar el generador:**
   ```bash
   python3 generar-alumnos.py
   ```

6. **Resultado esperado:**
   - Se crea carpeta `alumnos-generados/`
   - Se generan 163 archivos HTML
   - Resumen en pantalla

## 📊 Salida Esperada

```
============================================================
🎓 Generador de Páginas de Alumnos - IDECF
============================================================

📁 Directorio actual: /Users/.../Dashboard/Seccion 02
📄 CSV: alumnos-dcf-todas-generaciones.csv
📄 Template: seccion-02-informacion-alumno-idecf.html

📂 Directorio de salida: alumnos-generados/

📖 Leyendo archivo CSV consolidado...
✓ 163 alumnos encontrados

📄 Leyendo template HTML...
✓ Template cargado

🔨 Generando archivos HTML personalizados...
...
✅ GENERACIÓN COMPLETADA
```

## 🔧 Regenerar Archivos

Si necesitas regenerar todos los archivos:

```bash
# 1. Eliminar carpeta de archivos generados
rm -rf alumnos-generados

# 2. Ejecutar generador nuevamente
python3 generar-alumnos.py
```

## 💡 Tips

- **Siempre verifica** que estés en el directorio correcto con `pwd`
- **No muevas** los archivos CSV o template a otros directorios
- **Si modificas** el template, regenera todos los archivos
- **Los archivos generados** están en `alumnos-generados/`

## 📝 Estructura de Directorios

```
Dashboard-IDECF/
└── Dashboard/
    └── Seccion 02/              ← DEBES ESTAR AQUÍ
        ├── generar-alumnos.py
        ├── alumnos-dcf-todas-generaciones.csv
        ├── seccion-02-informacion-alumno-idecf.html
        └── alumnos-generados/   ← SE CREA AQUÍ
            ├── DS109.html
            ├── CFP101.html
            └── ... (163 archivos)
```
