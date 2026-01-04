# IDECF - Instituto Internacional de Constelaciones Familiares

## Información Institucional

**Nombre Completo:** Instituto Internacional de Constelaciones Familiares  
**Acrónimo:** IDECF  
**Sitio Web:** https://idecf.com  
**Panel:** https://panel.idecf.com

## SEO y Metadata

### Dashboard (Panel de Estudiantes)
**Título del Sitio:** IDECF - Panel de Alumnos | Constelaciones Familiares Internacional
**Descripción Corta:** Acceso a la plataforma educativa del Instituto Internacional de Constelaciones Familiares. Gestiona tus cursos, pagos y certificaciones en línea.

## Colores Institucionales

### Paleta de Colores
- **Color Primario:** `#6D0757`
- **Color Secundario:** `#9B4F96`
- **Color Accent:** `#C084B8`
- **Gradiente Principal:** `linear-gradient(135deg, #6D0757 0%, #9B4F96 100%)`

### Colores de Sistema
- **Blanco:** `#FFFFFF`
- **Gris Claro:** `#F5F5F5`
- **Éxito (Verde):** `#10b981`
- **Advertencia (Amarillo):** `#f59e0b`
- **Peligro (Rojo):** `#ef4444`

## Contacto

**WhatsApp Soporte:** +52 1 33 3405 4655  
**URL WhatsApp:** https://wa.me/5213334054655  
**Canal WhatsApp:** https://whatsapp.com/channel/0029Vb6g37Z3bbV3WXetDx2J

## URLs del Panel

- **Mi Cuenta:** https://panel.idecf.com/mi-cuenta/
- **Iniciar Sesión:** https://panel.idecf.com/iniciar-sesion/
- **Panel Access:** https://panel.idecf.com/panel-access/

## Componentes: Headers & Navegación

### Headers (Optimizados Tablet/Mobile 1024px)
Sistema de headers responsivos con menú hamburguesa para dispositivos con ancho menor a 1024px (tablets y móviles).

#### 1. Header Logged In (Usuario Autenticado)
**Archivo:** `Header/header-logged-in-IDECF.html`

- **Marca:** Logo/Texto "IDECF" clickeable (redirige a https://idecf.com).
- **Desktop (>1024px):** Botones visibles:
  - 📊 Dashboard
  - 💬 Soporte (WhatsApp)
  - 🚪 Cerrar Sesión
- **Tablet/Móvil (≤1024px):** Menú hamburguesa lateral con overlay.

#### 2. Header Logged Out (Usuario No Autenticado)
**Archivo:** `Header/header-logged-out-IDECF.html`

- **Marca:** Logo/Texto clickeable.
- **Acción:** Botón "Acceso a tu diplomado".
- **Responsive:** Menú hamburguesa en tablet/móvil.

#### 3. Header Web Principal
**Archivo:** `header-idecf.html` (en repo web)
- Navegación completa del sitio web.
- Breakpoint 1024px para menú móvil.
- Dropdowns responsivos.

### Implementación Técnica
- **Breakpoint JS/CSS:** 1024px.
- **Z-Index:** Header (1000), Overlay (998), Menú Lateral (999).

---

## Estructura de Sección Inicio (Dashboard)

La sección inicio del Dashboard IDECF está organizada en **13 componentes**:

### 1️⃣ Header y Bienvenida
- **01-dashboard-inicio-IDECF.html** - Título "DASHBOARD".
- **02-bienvenida-IDECF.html** - Mensaje de bienvenida.

### 2️⃣ Avisos y Accesos
- **03-aviso-admin-docentes-IDECF.html** 👥 - Aviso docentes.
- **04-accesos-rapidos-IDECF.html** ⚡ - Accesos rápidos.
- **05-aviso-solo-visualizacion-IDECF.html** 👁️ - Solo visualización.
- **06-reglamento-IDECF.html** - Reglamento.
- **07-plataforma-inactiva-IDECF.html** - Aviso inactiva.

### 3️⃣ Sección Administrativa
- **08-aviso-solo-administrativos-IDECF.html** 🔒 - Aviso admin.
- **09-informacion-chatbot-IDECF.html** - Chatbot.
- **10-oferta-activa-IDECF.html** - Tabla oferta activa.
- **11-requisiciones-IDECF.html** 📋 - Formularios requisiciones.
- **12-correos-activos-IDECF.html** 📧 - Correos activos.

### 4️⃣ Sección Estudiantil
- **13-aviso-dashboard-estudiantil-IDECF.html** 📚 - Aviso estudiantil.

---

## Recursos Adicionales (Extras)

### Carpeta: `Extras/`
**Archivo principal:** `extras-grid-idecf.html`

Grid de recursos con 6 secciones idéntico al sistema central pero con colores IDECF (#6D0757).

---

## 🎓 Sistema de Dashboards de Alumnos

### Ubicación: `Dashboard/Seccion 02/`

- **`seccion-02-informacion-alumno-idecf.html`**: Template base.
- **`generar-alumnos.py`**: Script de generación.
- **`alumnos-generados/`**: 163 HTMLs generados (ignorado en git).

**Funcionalidades:**
1. Card de Información (Correo, Nombre, No. Alumno).
2. Secciones expandibles: Pagos, Calificaciones, Exámenes, Terapia.

---

## 🛠️ Cómo Usar en Elementor

1. **Editar Página**: Usar Elementor.
2. **Widget HTML**: Arrastrar widget HTML.
3. **Pegar Código**: Copiar TODO el contenido del archivo HTML.
4. **Guardar**: Publicar cambios.

---

**Versión:** 4.1 (Update Headers 1024px)
**Fecha:** Enero 2026
