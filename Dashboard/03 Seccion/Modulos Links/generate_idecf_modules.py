import os

# Configuration
# Web App URLs are now specific to each course

courses = [
    {
        "name": "Diplomado en Constelaciones Familiares 1er plan de estudio",
        "code": "constelaciones1",
        "modules": 24,
        "path": "Modulos Links/Modulos/Diplomado en Constelaciones Familiares 1er plan de estudio",
        "web_app_url": "https://script.google.com/macros/s/AKfycbxUA0cuRfPPyQshS5QCeP4bLRG73URMw9qdcbQQLg9Zq96lV6l2MxKxANMXryNImps7Lw/exec"
    },
    {
        "name": "Diplomado en Constelaciones Familiares 2do plan de estudios",
        "code": "constelaciones2",
        "modules": 24,
        "path": "Modulos Links/Modulos/Diplomado en Constelaciones Familiares 2do plan de estudios",
        "web_app_url": "https://script.google.com/macros/s/AKfycbwpXf3Uc-6dADk59JrXHemfJembHhORHrG_z7ED2XV5x44pNVZP8GH1bi9KZ4ZZRZdUUA/exec"
    },
    {
        "name": "Diplomado en Terapia Gestalt",
        "code": "gestalt",
        "modules": 12,
        "path": "Modulos Links/Modulos/Diplomado en Terapia Gestalt",
        "web_app_url": "https://script.google.com/macros/s/AKfycbxiaHxJ_MwB5x3LZy-vn8kbx1hcYVAYuQZobIB2RlyHC5as-s8nPfA5Fce3A6TAuppk/exec"
    }
]

base_dir = "/Users/maximilianocalva/Documents/GitHub/IDECF/panel.idecf.com/Dashboard/03 Seccion"

# Templates
AULA_TV_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_prefix} - M{module_num}</title>
    
    <!-- PERFORMANCE & STYLES -->
    <link rel="preconnect" href="https://cdn.tailwindcss.com">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://player.vimeo.com">

    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Outfit', 'sans-serif'] }},
                    colors: {{
                        primary: '#233878',
                        secondary: '#1e3a8a',
                        accent: '#3b82f6',
                    }},
                    animation: {{
                        'spin-slow': 'spin 3s linear infinite',
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-50 min-h-screen">
    
    <!-- LOADER -->
    <div id="page-loader" class="fixed inset-0 z-50 flex items-center justify-center bg-white transition-opacity duration-500">
        <div class="flex flex-col items-center gap-4">
            <div class="w-12 h-12 border-4 border-indigo-100 border-t-indigo-600 rounded-full animate-spin"></div>
            <p class="text-sm text-gray-500 font-medium animate-pulse">Cargando lecciones...</p>
        </div>
    </div>

    <!-- MAIN CONTENT -->
    <main id="main-content" class="opacity-0 transition-opacity duration-700 p-4 md:p-8 max-w-7xl mx-auto">
        
        <!-- HEADER -->
        <header class="mb-10 text-center md:text-left">
            <div class="inline-block bg-white px-4 py-1.5 rounded-full shadow-sm border border-slate-100 mb-4">
                <span class="text-xs font-bold tracking-wider text-indigo-600 uppercase">Aula Virtual</span>
            </div>
            <h1 class="text-3xl md:text-4xl font-bold text-slate-800 mb-2">{title_prefix}</h1>
            <p class="text-slate-500 text-lg">Módulo {module_num}</p>
        </header>

        <!-- VIDEO PLAYER (Sticky/Main) -->
        <section class="mb-12">
            <div class="bg-black rounded-3xl shadow-2xl overflow-hidden aspect-video relative group ring-1 ring-slate-900/5">
                <iframe id="main-player" src="" class="absolute inset-0 w-full h-full" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
                
                <!-- Placeholder State -->
                <div id="player-placeholder" class="absolute inset-0 flex flex-col items-center justify-center bg-slate-900 text-white p-6 text-center">
                    <div class="w-20 h-20 bg-white/10 rounded-full flex items-center justify-center mb-6 backdrop-blur-sm">
                        <svg class="w-10 h-10 text-white/90" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <h3 class="text-2xl font-bold mb-2">Selecciona una clase para comenzar</h3>
                    <p class="text-slate-400 max-w-md">Explora el contenido del módulo en la lista inferior y haz clic en "Reproducir" para iniciar.</p>
                </div>
            </div>
            <div id="current-playing-info" class="mt-4 hidden bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex items-start gap-4">
               <div class="p-2 bg-indigo-50 rounded-lg text-indigo-600">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path></svg>
               </div>
               <div>
                    <h3 id="playing-title" class="font-bold text-slate-800 text-lg">Titulo del Video</h3>
                    <p id="playing-desc" class="text-slate-500 text-sm mt-1">Descripcion...</p>
               </div>
            </div>
        </section>

        <!-- SEARCH -->
        <div class="mb-8 relative max-w-md">
            <input type="text" id="searchInput" placeholder="Buscar clase..." class="w-full pl-12 pr-4 py-3 rounded-2xl border border-slate-200 focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all bg-white shadow-sm">
            <svg class="w-5 h-5 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>

        <!-- PLAYLIST GRID -->
        <div id="playlistItems" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Items injected by JS -->
        </div>

    </main>

    <script>
        // HARDCODED CONFIGURATION - ANTI-CACHE
        const CACHE_KEY = `idecf_{course_code}_m{module_num}_cache`;
        const FETCH_URL = "{web_app_url}?type=aulatv&course={course_code}&module={module_num}";

        (async function init() {{
            try {{
                // 1. Check LocalStorage
                const cached = localStorage.getItem(CACHE_KEY);
                let hasRendered = false;

                if (cached) {{
                    try {{
                        const parsed = JSON.parse(cached);
                        // 1 Hour validity for freshness
                        if (Date.now() - parsed.timestamp < 3600000) {{ 
                            console.log("Loading from cache:", CACHE_KEY);
                            processData(parsed.data);
                            hasRendered = true;
                            hideLoader();
                            // Fetch efficiently in background to update cache
                        }}
                    }} catch(e) {{ localStorage.removeItem(CACHE_KEY); }}
                }}

                // 2. Network Request (With Cache Buster)
                const finalUrl = FETCH_URL + "&t=" + Date.now();
                console.log("Fetching URL:", finalUrl);
                
                const response = await fetch(finalUrl);
                if (!response.ok) throw new Error("HTTP " + response.status);
                const data = await response.json();

                if (data.error) {{
                     // If explicit error from server, clear cache
                     localStorage.removeItem(CACHE_KEY);
                     throw new Error(data.error);
                }}

                // Update Cache and UI
                localStorage.setItem(CACHE_KEY, JSON.stringify({{ timestamp: Date.now(), data: data }}));
                
                if (!hasRendered) {{
                     processData(data);
                     hideLoader();
                }}

            }} catch (error) {{
                console.error("Error loading data:", error);
                
                // FORCE CLEAR CACHE ON ERROR
                localStorage.removeItem(CACHE_KEY);

                if (!document.querySelector('.playlist-item')) {{
                    document.getElementById('playlistItems').innerHTML = `<div class='col-span-full p-8 text-center text-red-500 bg-red-50 rounded-xl border border-red-100'>
                        <p class="font-bold mb-2">Error de Conexión</p>
                        <p class="text-sm font-mono mt-2 bg-red-50 p-2 rounded text-xs select-all text-left">
                            ${{error.message}}<br>
                            <span class="text-red-300">Target: ${{FETCH_URL}}</span>
                        </p>
                        <button onclick='location.reload(true)' class='mt-4 px-4 py-2 bg-red-100 text-red-700 rounded-lg text-sm hover:bg-red-200 transition-colors'>Reintentar (Limpiar Cache)</button>
                    </div>`;
                    hideLoader();
                }}
            }}
        }})();

        function hideLoader() {{
            document.getElementById('page-loader').classList.add('opacity-0', 'pointer-events-none');
            document.getElementById('main-content').classList.remove('opacity-0');
            setTimeout(() => document.getElementById('page-loader').remove(), 500);
        }}

        function processData(items) {{
            const grid = document.getElementById('playlistItems');
            
            if (items && items.length > 0) {{
                grid.innerHTML = items.map((item, idx) => {{
                    // Normalize keys
                    const title = item['Titulo'] || item['Título'] || 'Sin Título';
                    const link = item['Link'] || item['URL'] || '';
                    const desc = item['Descripcion'] || item['Descripción'] || '';
                    const num = item['Numero'] || item['N°'] || idx + 1;

                    if (!link) return ''; // Skip empty links

                    // Escape quotes for onclick
                    const safeTitle = title.replace(/'/g, "\\'");
                    const safeDesc = desc.replace(/'/g, "\\'");
                    
                    return `
                    <div class="playlist-item group bg-white border border-slate-200 rounded-2xl p-4 hover:shadow-xl hover:border-indigo-100 transition-all cursor-pointer flex gap-4 items-start" onclick="playVideo('${{link}}', '${{safeTitle}}', '${{safeDesc}}')">
                        <div class="w-12 h-12 bg-indigo-50 text-indigo-600 rounded-xl flex items-center justify-center shrink-0 font-bold group-hover:bg-indigo-600 group-hover:text-white transition-colors">
                            ${{num}}
                        </div>
                        <div class="flex-1 min-w-0">
                            <h3 class="font-bold text-slate-800 text-sm group-hover:text-indigo-600 line-clamp-2 leading-snug mb-1">${{title}}</h3>
                            <p class="text-xs text-slate-400 line-clamp-1">${{desc}}</p>
                        </div>
                        <div class="self-center opacity-0 group-hover:opacity-100 transition-opacity -translate-x-2 group-hover:translate-x-0">
                             <svg class="w-5 h-5 text-indigo-500" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>
                        </div>
                    </div>`;
                }}).join('');

                // Setup Search
                document.getElementById('searchInput').addEventListener('input', (e) => {{
                    const term = e.target.value.toLowerCase();
                    document.querySelectorAll('.playlist-item').forEach(el => {{
                        const text = el.innerText.toLowerCase();
                        el.style.display = text.includes(term) ? 'flex' : 'none';
                    }});
                }});

            }} else {{
                grid.innerHTML = `<div class="col-span-full text-center py-12 text-slate-400 bg-slate-50 rounded-2xl border border-dashed border-slate-200">No hay videos disponibles en este momento.</div>`;
            }}
        }}

        function playVideo(url, title, desc) {{
            const player = document.getElementById('main-player');
            const placeholder = document.getElementById('player-placeholder');
            const info = document.getElementById('current-playing-info');
            
            let embedUrl = url;
            if (url.includes('vimeo')) {{
                // Extract Vimeo ID properly even with params
                const id = url.split('/').pop().split('?')[0];
                embedUrl = `https://player.vimeo.com/video/${{id}}?autoplay=1`;
            }} else if (url.includes('youtube') || url.includes('youtu.be')) {{
                const id = url.includes('v=') ? url.split('v=')[1].split('&')[0] : url.split('/').pop();
                embedUrl = `https://www.youtube.com/embed/${{id}}?autoplay=1`;
            }}

            player.src = embedUrl;
            placeholder.classList.add('hidden');
            
            // Info Update
            info.classList.remove('hidden');
            document.getElementById('playing-title').innerText = title;
            document.getElementById('playing-desc').innerText = desc || 'Reproduciendo ahora...';
            
            // Smooth Scroll
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}
    </script>
</body>
</html>"""

MATERIAL_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_prefix} - Material M{module_num}</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://cdn.tailwindcss.com">

    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Outfit', 'sans-serif'] }},
                    colors: {{
                        primary: '#233878',
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-50 min-h-screen">
    
    <div id="page-loader" class="fixed inset-0 z-50 flex items-center justify-center bg-white">
        <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-primary"></div>
    </div>

    <!-- HEADER -->
    <div class="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-sm">
        <div class="max-w-5xl mx-auto px-6 py-4 flex items-center justify-between">
            <div>
                <span class="text-xs font-bold text-primary tracking-widest uppercase mb-1 block">Recursos Descargables</span>
                <h1 class="text-2xl font-bold text-slate-900 leading-none">{title_prefix}</h1>
            </div>
            <div class="text-right hidden md:block">
                <p class="text-sm text-slate-500">Módulo {module_num}</p>
            </div>
        </div>
    </div>

    <main id="main-content" class="max-w-5xl mx-auto px-6 py-10 opacity-0 transition-opacity duration-500">
        
        <div class="mb-4 text-sm breadcrumbs text-slate-400">
          <ul class="flex gap-2">
            <li><a href="#" onclick="history.back()" class="hover:text-primary">← Volver</a></li>
          </ul>
        </div>

        <div id="materialList" class="space-y-4">
            <!-- Injected Items -->
        </div>

        <footer class="mt-16 pt-8 border-t border-slate-200 text-center text-slate-400 text-sm">
            <p>&copy; 2026 IDECF. Todos los derechos reservados.</p>
        </footer>

    </main>

    <script>
        // HARDCODED CONFIGURATION - ANTI-CACHE
        const CACHE_KEY = `idecf_{course_code}_m{module_num}_mat_cache`;
        const FETCH_URL = "{web_app_url}?type=material&course={course_code}&module={module_num}";

        (async function init() {{
            try {{
                // 1. Local Cache
                const cached = localStorage.getItem(CACHE_KEY);
                let hasRendered = false;

                if (cached) {{
                    try {{
                        const parsed = JSON.parse(cached);
                        if (Date.now() - parsed.timestamp < 3600000 * 24) {{ // 24 Hours
                             console.log("Loading from cache:", CACHE_KEY);
                             processData(parsed.data);
                             hasRendered = true;
                             hideLoader();
                             // Fetch in background to update
                        }}
                    }} catch(e) {{ localStorage.removeItem(CACHE_KEY); }}
                }}

                // 2. Network Request (With Cache Buster)
                const finalUrl = FETCH_URL + "&t=" + Date.now();
                console.log("Fetching URL:", finalUrl);

                const response = await fetch(finalUrl);
                if(!response.ok) throw new Error("HTTP " + response.status);
                
                const data = await response.json();
                
                if (data.error) {{
                     localStorage.removeItem(CACHE_KEY);
                     throw new Error(data.error);
                }}

                // Update Cache
                localStorage.setItem(CACHE_KEY, JSON.stringify({{ timestamp: Date.now(), data: data }}));
                
                if (!hasRendered) {{
                     processData(data);
                     hideLoader();
                }}

            }} catch (error) {{
                console.error(error);
                
                // FORCE CLEAR CACHE
                localStorage.removeItem(CACHE_KEY);

                if (!document.querySelector('.doc-card')) {{
                     hideLoader();
                     document.getElementById('materialList').innerHTML = `<div class="p-6 bg-red-50 text-red-600 rounded-xl text-center border border-red-100">
                        <p class="font-bold">Error de Carga</p>
                        <p class="text-sm mt-1 mb-2 font-mono text-xs text-left bg-red-50 p-2 rounded">
                            ${{error.message}}<br>
                             <span class="text-red-300">Target: ${{FETCH_URL}}</span>
                        </p>
                        <button onclick="location.reload(true)" class="mt-4 underline hover:text-red-800">Reintentar (Limpiar Cache)</button>
                     </div>`;
                }}
            }}
        }})();

        function hideLoader() {{
            document.getElementById('page-loader').classList.add('hidden');
            document.getElementById('main-content').classList.remove('opacity-0');
        }}

        function processData(items) {{
            const listEl = document.getElementById('materialList');
            
            if (items && items.length > 0) {{
                listEl.innerHTML = "";
                items.forEach((item, idx) => {{
                    // Normalize keys
                    const title = item['Titulo'] || item['Título'] || 'Material';
                    const link = item['Link'] || item['URL'] || '#';
                    const desc = item['Descripcion'] || item['Descripción'] || '';
                    const format = item['Formato'] || 'DOC';
                    const num = item['Numero'] || item['N°'] || idx + 1;

                    const div = document.createElement('div');
                    div.className = "doc-card bg-white border border-slate-200 rounded-2xl p-6 flex flex-col md:flex-row items-center gap-6 group relative overflow-hidden transition-all hover:shadow-lg hover:border-indigo-100";
                    div.innerHTML = `
                        <div class="absolute top-4 right-4 text-xs font-bold text-slate-200 pointer-events-none">#${{num}}</div>
                        <div class="w-16 h-16 bg-slate-50 text-primary rounded-2xl flex items-center justify-center shrink-0 shadow-inner group-hover:bg-primary group-hover:text-white transition-colors">
                            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                        </div>
                        <div class="flex-1 text-center md:text-left w-full">
                            <h3 class="text-xl font-bold text-slate-800 mb-1 group-hover:text-primary transition-colors">${{title}}</h3>
                            <div class="flex items-center justify-center md:justify-start gap-2 text-sm text-slate-500">
                                 <span class="bg-slate-100 px-2 py-0.5 rounded text-xs font-semibold uppercase">${{format}}</span>
                            </div>
                        </div>
                        <div class="mt-2 md:mt-0 w-full md:w-auto">
                            <a href="${{link}}" target="_blank" class="bg-primary text-white px-8 py-3 rounded-xl font-semibold hover:bg-blue-900 transition-colors shadow-lg shadow-blue-900/10">Ver Recurso</a>
                        </div>
                    `;
                    listEl.appendChild(div);
                }});
            }} else {{
                listEl.innerHTML = `<div class="p-12 text-center bg-slate-50 rounded-2xl border border-dashed border-slate-200 text-slate-400">
                    <p>No hay recursos disponibles.</p>
                </div>`;
            }}
        }}

    </script>
</body>
</html>"""
def generate():
    for course in courses:
        full_path = os.path.join(base_dir, course["path"])
        
        # Ensure dir exists
        if not os.path.exists(full_path):
            print(f"Creating directory: {full_path}")
            os.makedirs(full_path)
            
        print(f"Generating {course['modules']} modules for: {course['name']}")
        
        for i in range(1, course["modules"] + 1):
            # Aula TV
            aula_filename = f"aula-tv-m{i}.html"
            aula_content = AULA_TV_TEMPLATE.format(
                title_prefix=course["name"],
                module_num=i,
                web_app_url=course["web_app_url"],
                course_code=course["code"]
            )
            with open(os.path.join(full_path, aula_filename), "w") as f:
                f.write(aula_content)
                
            # Material
            mat_filename = f"material-m{i}.html"
            mat_content = MATERIAL_TEMPLATE.format(
                title_prefix=course["name"],
                module_num=i,
                web_app_url=course["web_app_url"],
                course_code=course["code"]
            )
            with open(os.path.join(full_path, mat_filename), "w") as f:
                f.write(mat_content)
                
    print("Generation Complete!")

if __name__ == "__main__":
    generate()
