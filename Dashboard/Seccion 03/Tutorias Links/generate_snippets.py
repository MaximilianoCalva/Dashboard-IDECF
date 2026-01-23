#!/usr/bin/env python3
"""
Script para generar snippets de tutorial links para IDECF (estilo IDEMAB)
"""

import os

# Template para snippet de link (botón que redirige)
SNIPPET_TEMPLATE_DCF = '''<!-- Tailwind CSS (Ensure this is loaded only once per page if possible, but included here for snippet self-sufficiency) -->
<script src="https://cdn.tailwindcss.com"></script>

<a href="https://panel.idecf.com/dcfg{number:02d}/" class="block w-full group no-underline mb-4">
    <div class="relative overflow-hidden bg-white p-5 rounded-2xl shadow-sm border border-gray-100 transition-all duration-300 hover:shadow-lg hover:border-[#6D0757]/20 hover:-translate-y-1">
        <!-- Colored Accent Line -->
        <div class="absolute left-0 top-0 bottom-0 w-1.5 bg-[#6D0757] group-hover:w-2.5 transition-all duration-300"></div>
        
        <div class="flex items-center justify-between pl-3">
            <div class="flex flex-col">
                <span class="text-[10px] font-bold text-[#6D0757] tracking-widest uppercase mb-1 opacity-70">Acceder a tutorías grabadas de</span>
                <span class="text-xs font-bold text-gray-500 uppercase mb-1">Diplomado en Constelaciones Familiares</span>
                <span class="text-lg font-extrabold text-gray-800 group-hover:text-[#6D0757] transition-colors">Generación {number:02d}</span>
            </div>
            
            <!-- Icon Circle -->
            <div class="w-10 h-10 bg-gray-50 rounded-full flex items-center justify-center group-hover:bg-[#6D0757] transition-all duration-300 shadow-inner group-hover:shadow-none min-w-[2.5rem]">
                <svg class="w-5 h-5 text-gray-400 group-hover:text-white transition-colors duration-300 transform group-hover:translate-x-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                </svg>
            </div>
        </div>
    </div>
</a>
'''

SNIPPET_TEMPLATE_DTG = '''<!-- Tailwind CSS (Ensure this is loaded only once per page if possible, but included here for snippet self-sufficiency) -->
<script src="https://cdn.tailwindcss.com"></script>

<a href="https://panel.idecf.com/dtgg{number:02d}/" class="block w-full group no-underline mb-4">
    <div class="relative overflow-hidden bg-white p-5 rounded-2xl shadow-sm border border-gray-100 transition-all duration-300 hover:shadow-lg hover:border-[#6D0757]/20 hover:-translate-y-1">
        <!-- Colored Accent Line -->
        <div class="absolute left-0 top-0 bottom-0 w-1.5 bg-[#6D0757] group-hover:w-2.5 transition-all duration-300"></div>
        
        <div class="flex items-center justify-between pl-3">
            <div class="flex flex-col">
                <span class="text-[10px] font-bold text-[#6D0757] tracking-widest uppercase mb-1 opacity-70">Acceder a tutorías grabadas de</span>
                <span class="text-xs font-bold text-gray-500 uppercase mb-1">Diplomado en Terapia Gestalt</span>
                <span class="text-lg font-extrabold text-gray-800 group-hover:text-[#6D0757] transition-colors">Generación {number:02d}</span>
            </div>
            
            <!-- Icon Circle -->
            <div class="w-10 h-10 bg-gray-50 rounded-full flex items-center justify-center group-hover:bg-[#6D0757] transition-all duration-300 shadow-inner group-hover:shadow-none min-w-[2.5rem]">
                <svg class="w-5 h-5 text-gray-400 group-hover:text-white transition-colors duration-300 transform group-hover:translate-x-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                </svg>
            </div>
        </div>
    </div>
</a>
'''

def generate_snippet_links():
    """Genera los snippets de tutorial links para IDECF"""
    
    base_path = "/Users/maximilianocalva/Documents/GitHub/IDECF/panel.idecf.com/Dashboard/Seccion 03/Tutorias Links"
    
    # Generar snippets DCF
    dcf_path = os.path.join(base_path, "DCF")
    print("📁 Generating DCF snippets...")
    for i in range(1, 21):
        filename = f"snippet-dcfg{i:02d}.html"
        filepath = os.path.join(dcf_path, filename)
        
        content = SNIPPET_TEMPLATE_DCF.format(number=i)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Created: {filename}")
    
    # Generar snippets DTG
    dtg_path = os.path.join(base_path, "DTG")
    print("\n📁 Generating DTG snippets...")
    for i in range(1, 21):
        filename = f"snippet-dtgg{i:02d}.html"
        filepath = os.path.join(dtg_path, filename)
        
        content = SNIPPET_TEMPLATE_DTG.format(number=i)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Created: {filename}")
    
    print(f"\n🎉 Successfully generated 40 tutorial link snippets!")
    print(f"\n📝 These snippets are buttons that link to:")
    print(f"   https://panel.idecf.com/dcfg01/ ... dcfg20/")
    print(f"   https://panel.idecf.com/dtgg01/ ... dtgg20/")

if __name__ == "__main__":
    generate_snippet_links()
