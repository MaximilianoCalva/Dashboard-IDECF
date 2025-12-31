# IDECF - Instituto Internacional de Constelaciones Familiares

## Información Institucional

**Nombre Completo:** Instituto Internacional de Constelaciones Familiares  
**Acrónimo:** IDECF  
**Sitio Web:** https://idecf.com  
**Panel:** https://panel.idecf.com

## SEO y Metadata

### Dashboard (Panel de Estudiantes)
**Título del Sitio:** IDECF - Mi Dashboard | Plataforma de Constelaciones Familiares  
**Descripción Corta:** Accede a tu plataforma de aprendizaje en Constelaciones Familiares. Consulta tus diplomados, talleres, certificados y avanza en tu formación terapéutica.

## Colores Institucionales

### Paleta de Colores
- **Morado Primario:** `#6D0757`
- **Morado Hover:** `#8E0970`

### Colores de Sistema
- **Blanco:** `#FFFFFF`
- **Gris Claro:** `#F5F5F5`
- **Éxito (Verde):** `#10b981`
- **Peligro (Rojo):** `#ef4444`

### Bordes y Sombras
- **Border Color:** `#f0e6ee`
- **Box Shadow:** `0 2px 8px rgba(109, 7, 87, 0.06)`

## Contacto

**WhatsApp Soporte:** +52 1 33 2935 7723  
**URL WhatsApp:** https://wa.me/5213329357723  
**Canal WhatsApp:** https://whatsapp.com/channel/0029VbAe4fl2P59rdcs99r44

## Redes Sociales

**Facebook:** https://facebook.com/203152456224733  
**Instagram:** https://instagram.com/constelacionesfamidecf  
**TikTok:** https://www.tiktok.com/@constelacionesfamidecf  
**YouTube:** https://www.youtube.com/channel/UCXZ3SI7AcpwRCjvWm9y7jzQ

## URLs del Panel

- **Mi Cuenta:** https://panel.idecf.com/mi-cuenta/
- **Iniciar Sesión:** https://panel.idecf.com/
- **Logout:** https://panel.idecf.com/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fpanel.idecf.com

## Recursos Visuales

### Logo
**URL:** https://idecf.com/wp-content/uploads/2024/02/IDECF-Logo-blanco.png

### Dimensiones del Logo
- **Desktop:** 30px altura
- **Mobile:** 25px altura
- **Max Width:** 150px

## Componentes del Dashboard

### Headers
- `Header/header-logged-in-IDECF.html` - Header para usuarios autenticados
- `Header/header-logged-out-IDECF.html` - Header para usuarios no autenticados

### Especificaciones del Header
- **Padding:** 3px 10px
- **Ancho:** 100% (full width)
- **Altura Mínima:** 50px
- **Font Size Brand:** 18px (desktop), 16px (mobile)
- **Font Size Subtitle:** 9px (desktop), 7-8px (mobile)
- **Color Brand:** Morado primario (#6D0757)

## Notas de Diseño

- Los headers usan texto "IDECF" en lugar de logo
- Color morado institucional para branding
- Diseño responsive con breakpoints en 768px y 480px
- Botones compactos con iconos de 14px
- Mismo tamaño y estructura que IDEBIO e IDEMAB

## Última Actualización

Fecha: 2025-12-30  
Versión: 1.0

## Archivos de Acceso al Dashboard

### Carpeta: `Acceso a dashboard/`

**Para usuarios autenticados (logged-in):**
- `login-idecf-snippet.html` - Página de bienvenida con botón "Ir al Dashboard"
  - Redirige a: `https://panel.idecf.com/mi-cuenta/`

**Para usuarios NO autenticados (logged-out):**
- `logout-idecf-snippet.html` - Formulario de inicio de sesión
  - Contiene shortcode: `[profilepress-login id="1"]`
  - Incluye instrucciones para el usuario

**Uso en WordPress:**
- Copiar y pegar el contenido completo en un widget HTML de Elementor
- Los snippets no afectan el diseño de la página existente
- Usan clases CSS únicas para evitar conflictos

## Recursos Adicionales (Extras)

### Carpeta: `Extras/`

**Archivo principal:** `extras-grid-idecf.html`

Grid de recursos adicionales con 3 secciones organizadas por programa:

1. **📚 Biblioteca DCF** (Constelaciones Familiares)
   - URL: https://panel.idecf.com/biblioteca-dcf/
   - Biblioteca del Diplomado en Constelaciones Familiares
   - Badge: "Constelaciones Familiares"

2. **🎥 Videoteca**
   - URL: https://panel.idecf.com/videoteca/
   - Biblioteca de videos educativos general

3. **📖 Biblioteca DTG** (Terapia Gestalt)
   - URL: https://panel.idecf.com/biblioteca-dtg/
   - Biblioteca del Diplomado en Terapia Gestalt
   - Badge: "Terapia Gestalt"

### Diseño de Extras
- **Colores**: Gradiente morado IDECF (#6D0757 a #8E0970)
- **Layout**: Grid responsive (3 columnas desktop, 1 mobile)
- **Badges**: Identificadores de programa en cada tarjeta
- **Interactividad**: Hover effects con elevación y sombra
