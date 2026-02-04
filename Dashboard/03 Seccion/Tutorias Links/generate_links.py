#!/usr/bin/env python3
"""
Script para generar archivos HTML de tutorías con URLs cortas para IDECF
Genera dcfg01-dcfg20 y dtgg01-dtgg20
"""

import os

# Template HTML base (página completa con el snippet embebido)
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - IDECF</title>
    <meta name="description" content="Tutorías grabadas del {diploma} - IDECF Instituto Internacional de Constelaciones Familiares">
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #f9fafb;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Aquí va el snippet de tutorías -->
        [elementor-template id="{template_id}"]
    </div>
</body>
</html>
'''

def generate_tutorial_link_files():
    """Genera los archivos HTML de tutorías con URLs cortas para IDECF"""
    
    base_path = "/Users/maximilianocalva/Documents/GitHub/IDECF/panel.idecf.com/Tutorias Links"
    
    # Generar dcfg01 a dcfg20 (Diplomado en Constelaciones Familiares)
    dcf_path = os.path.join(base_path, "DCF")
    for i in range(1, 21):
        short_name = f"dcfg{i:02d}"
        filename = f"{short_name}.html"
        filepath = os.path.join(dcf_path, filename)
        
        # Template ID será diferente para cada archivo (ajustar según necesites)
        template_id = f"DCFG{i:02d}"
        
        html_content = HTML_TEMPLATE.format(
            title=f"Tutorías {template_id}",
            diploma="Diplomado en Constelaciones Familiares",
            template_id=template_id
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Created: {filename}")
    
    # Generar dtgg01 a dtgg20 (Diplomado en Terapia Gestalt)
    dtg_path = os.path.join(base_path, "DTG")
    for i in range(1, 21):
        short_name = f"dtgg{i:02d}"
        filename = f"{short_name}.html"
        filepath = os.path.join(dtg_path, filename)
        
        # Template ID será diferente para cada archivo
        template_id = f"DTGG{i:02d}"
        
        html_content = HTML_TEMPLATE.format(
            title=f"Tutorías {template_id}",
            diploma="Diplomado en Terapia Gestalt",
            template_id=template_id
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Created: {filename}")
    
    print(f"\n🎉 Successfully generated 40 tutorial link files for IDECF!")
    print(f"📁 DCF: 20 files (dcfg01-dcfg20)")
    print(f"📁 DTG: 20 files (dtgg01-dtgg20)")
    print(f"\n📝 URLs will be:")
    print(f"   https://panel.idecf.com/dcfg01/ ... dcfg20/")
    print(f"   https://panel.idecf.com/dtgg01/ ... dtgg20/")

if __name__ == "__main__":
    generate_tutorial_link_files()
