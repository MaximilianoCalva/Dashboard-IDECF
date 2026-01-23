#!/usr/bin/env python3
"""
Script para actualizar la URL del Apps Script en todos los archivos de tutorías de IDECF
"""

import os
import re

# Nueva URL del Apps Script de IDECF
NEW_URL = "https://script.google.com/macros/s/AKfycbzbr5gMZQGnY6ZHVncD0JUsgB0jQ97KOaVwcF8dez0vax37o4VXqvW0KhJnPNhuWAI_sA/exec"

# URL antigua (de IDEBIO)
OLD_URL = "https://script.google.com/macros/s/AKfycbzE-dsS3EbQ74c0CwUmNjVGKTezSBbMiKB_WbHqBPiQdRQQuWt6aXYEVEAEOrdq5j9H/exec"

def update_files_in_directory(directory):
    """Actualiza todos los archivos HTML en un directorio"""
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            
            # Leer el archivo
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Reemplazar la URL antigua con la nueva
            if OLD_URL in content:
                new_content = content.replace(OLD_URL, NEW_URL)
                
                # Escribir el archivo actualizado
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"✅ Updated: {filename}")
                count += 1
            else:
                print(f"⚠️  Skipped (URL not found): {filename}")
    
    return count

def main():
    base_path = "/Users/maximilianocalva/Documents/GitHub/IDECF/panel.idecf.com/Tutorias Grabadas"
    
    # Actualizar archivos en DCF
    dcf_path = os.path.join(base_path, "DCF")
    print("📁 Updating DCF files...")
    dcf_count = update_files_in_directory(dcf_path)
    
    # Actualizar archivos en DTG
    dtg_path = os.path.join(base_path, "DTG")
    print("\n📁 Updating DTG files...")
    dtg_count = update_files_in_directory(dtg_path)
    
    print(f"\n🎉 Successfully updated {dcf_count + dtg_count} files!")
    print(f"   DCF: {dcf_count} files")
    print(f"   DTG: {dtg_count} files")
    print(f"\n✨ New Apps Script URL:")
    print(f"   {NEW_URL}")

if __name__ == "__main__":
    main()
