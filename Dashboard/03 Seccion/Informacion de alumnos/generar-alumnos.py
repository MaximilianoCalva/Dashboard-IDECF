#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Páginas Individuales de Alumnos - IDECF
Genera archivos HTML personalizados para cada alumno desde CSV consolidado
"""

import csv
import os
import sys
from pathlib import Path

# Obtener el directorio donde está el script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Configuración - usar rutas absolutas basadas en la ubicación del script
CSV_FILE = os.path.join(SCRIPT_DIR, 'alumnos-dcf-todas-generaciones.csv')
TEMPLATE_FILE = os.path.join(SCRIPT_DIR, 'seccion-02-informacion-alumno-idecf.html')
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'alumnos-generados')

def read_csv(csv_path):
    """Lee el archivo CSV consolidado y retorna lista de alumnos"""
    alumnos = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Saltar comentarios y líneas vacías
            if not line or line.startswith('#'):
                continue
            # Saltar header
            if line.startswith('codigo,'):
                continue
            
            parts = line.split(',')
            if len(parts) >= 3:
                alumnos.append({
                    'codigo': parts[0].strip(),
                    'nombre': parts[1].strip(),
                    'email': parts[2].strip(),
                    'generacion': parts[3].strip() if len(parts) > 3 else 'N/A',
                    'programa': parts[4].strip() if len(parts) > 4 else 'DCF'
                })
    return alumnos

def read_template(template_path):
    """Lee el archivo template HTML"""
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_student_html(template, student):
    """Genera HTML personalizado para un alumno"""
    html = template
    
    # Reemplazar datos del alumno
    html = html.replace('alumno@ejemplo.com', student['email'])
    html = html.replace('Nombre del Alumno', student['nombre'])
    html = html.replace('PDCF001', student['codigo'])
    
    # Reemplazar código de pagos (P + código)
    payment_code = 'P' + student['codigo']
    html = html.replace('PPDCF001', payment_code)
    
    # Actualizar título de la página
    html = html.replace(
        '<title>Información del Alumno - IDECF</title>',
        f'<title>Dashboard - {student["nombre"]} - IDECF</title>'
    )
    
    return html

def save_student_file(html, student, output_dir):
    """Guarda el archivo HTML del alumno"""
    filename = f"{student['codigo']}.html"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return filename

def main():
    """Función principal"""
    print("\n" + "=" * 60)
    print("🎓 Generador de Páginas de Alumnos - IDECF")
    print("=" * 60)
    print()
    
    # Verificar archivos necesarios
    if not os.path.exists(CSV_FILE):
        print(f"❌ Error: No se encontró el archivo {CSV_FILE}")
        print(f"   Ubicación esperada: {os.path.abspath(CSV_FILE)}")
        return
    
    if not os.path.exists(TEMPLATE_FILE):
        print(f"❌ Error: No se encontró el archivo {TEMPLATE_FILE}")
        print(f"   Ubicación esperada: {os.path.abspath(TEMPLATE_FILE)}")
        return
    
    print(f"📁 Directorio actual: {os.getcwd()}")
    print(f"📄 CSV: {CSV_FILE}")
    print(f"📄 Template: {TEMPLATE_FILE}")
    print()
    
    # Crear directorio de salida
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    print(f"📂 Directorio de salida: {OUTPUT_DIR}/")
    print()
    
    # Leer datos
    print("📖 Leyendo archivo CSV consolidado...")
    alumnos = read_csv(CSV_FILE)
    print(f"✓ {len(alumnos)} alumnos encontrados")
    print()
    
    print("📄 Leyendo template HTML...")
    template = read_template(TEMPLATE_FILE)
    print("✓ Template cargado")
    print()
    
    # Agrupar por generación
    generaciones = {}
    for alumno in alumnos:
        gen = alumno.get('generacion', 'N/A')
        if gen not in generaciones:
            generaciones[gen] = []
        generaciones[gen].append(alumno)
    
    # Generar archivos
    print("🔨 Generando archivos HTML personalizados...")
    print("-" * 60)
    
    total_generated = 0
    for gen in sorted(generaciones.keys()):
        alumnos_gen = generaciones[gen]
        print(f"\n📚 {gen} - {len(alumnos_gen)} alumnos:")
        
        for i, alumno in enumerate(alumnos_gen, 1):
            html = generate_student_html(template, alumno)
            filename = save_student_file(html, alumno, OUTPUT_DIR)
            
            payment_code = 'P' + alumno['codigo']
            nombre_truncado = alumno['nombre'][:35].ljust(35)
            print(f"  {i:2d}. {filename:15s} → {nombre_truncado} (Pagos: {payment_code})")
            total_generated += 1
    
    print("\n" + "-" * 60)
    print()
    
    # Resumen
    print("✅ GENERACIÓN COMPLETADA")
    print("=" * 60)
    print(f"\n📊 Resumen:")
    print(f"   • Total de archivos generados: {total_generated}")
    print(f"   • Ubicación: {OUTPUT_DIR}/")
    print(f"   • Generaciones procesadas: {len(generaciones)}")
    print()
    
    print("📁 Distribución por generación:")
    for gen in sorted(generaciones.keys()):
        count = len(generaciones[gen])
        print(f"   • {gen}: {count} archivos")
    
    print("\n💡 Próximos pasos:")
    print("   1. Revisa los archivos en 'alumnos-generados/'")
    print("   2. Cada archivo tiene los datos del alumno pre-cargados")
    print("   3. Copia el contenido a Elementor (widget HTML)")
    print("   4. Los shortcodes se procesarán automáticamente")
    print("\n" + "=" * 60 + "\n")

if __name__ == '__main__':
    main()
