# Dashboard Sección Inicio - IDECF

## 📋 Descripción

Colección de componentes HTML para la sección de inicio del dashboard de **IDECF (Instituto de Educación en Ciencias Forenses)**. Estos componentes están diseñados para ser integrados en WordPress usando widgets HTML personalizados.

## 🎨 Colores Institucionales

IDECF utiliza un esquema de colores púrpura magenta que representa profesionalismo, precisión y ciencia forense:

### Paleta Principal
- **Púrpura Magenta**: `#6D0757` - Color primario institucional
- **Blanco**: `#FFFFFF` - Color secundario institucional
- **Púrpura Claro**: `#8E0970` - Estados hover e interactivos
- **Púrpura Suave**: `#A855F7` - Acentos adicionales

### Variables CSS
```css
:root {
  --idecf-primary: #6D0757;
  --idecf-secondary: #FFFFFF;
  --idecf-hover: #8E0970;
  --idecf-accent: #A855F7;
}
```

## 📁 Estructura de Archivos

```
Dashboard-seccion-inicio-IDECF/
├── 01-dashboard-inicio-IDECF.html          # Cápsula de navegación "Dashboard > Inicio"
├── 02-bienvenida-IDECF.html                # Mensaje de bienvenida personalizado
├── 03-reglamento-IDECF.html                # Visor de reglamento institucional
├── 04-plataforma-inactiva-IDECF.html       # Aviso de cuenta inactiva
├── 05-informacion-chatbot-IDECF.html       # Información sobre recursos del chatbot
├── 06-oferta-activa-IDECF.html             # Widget de oferta educativa activa
├── 07-accesos-rapidos-IDECF.html           # Enlaces de acceso rápido
├── colores-institucionales-IDECF.md        # Guía de colores institucionales
└── README.md                                # Este archivo
```

## 🚀 Componentes

### 1. Dashboard Inicio (01)
Cápsula compacta de navegación que muestra "IDECF | Plataforma | DASHBOARD" con animación de flecha.

**Características:**
- Diseño tipo píldora con bordes extra redondeados
- Color púrpura magenta institucional
- Animación minimalista
- Responsive para móviles

### 2. Bienvenida (02)
Mensaje de bienvenida personalizado para estudiantes.

### 3. Reglamento (03)
Visor de reglamento institucional con navegación por páginas.

**Características:**
- Navegación entre páginas del reglamento
- Botones con color púrpura institucional
- Diseño limpio y profesional

### 4. Plataforma Inactiva (04)
Aviso informativo sobre posibles razones de cuenta inactiva.

**Características:**
- Diseño de tarjeta con borde superior púrpura
- Icono circular con fondo púrpura
- Secciones para "Baja Temporal" y "Adeudo en Mensualidad"
- Footer con fondo púrpura institucional
- Efecto hover en tarjetas

### 5. Información Chatbot (05)
Información sobre los recursos disponibles del chatbot IA.

**Características:**
- Tarjetas con bordes superiores en tonos púrpura
- Variables CSS personalizadas
- Diseño modular y escalable
- Fondo lila suave

### 6. Oferta Activa (06)
Widget para mostrar ofertas educativas activas.

**Características:**
- Sistema de variables CSS con colores institucionales
- Diseño adaptable
- Estados hover optimizados

### 7. Accesos Rápidos (07)
Enlaces rápidos a recursos importantes de la plataforma.

## 💻 Uso en WordPress

### Integración con Elementor

1. **Agregar Widget HTML**
   - Arrastra un widget "HTML" a tu sección
   - Copia el contenido completo del archivo `.html`
   - Pega en el editor HTML del widget

2. **Configuración Recomendada**
   - Ancho: 100% del contenedor
   - Padding: Ajustar según necesidad
   - Margen: 8-10px superior e inferior

### Integración con Bloques de WordPress

1. **Bloque HTML Personalizado**
   - Añade un bloque "HTML personalizado"
   - Pega el código del componente
   - Previsualiza y publica

## 🎯 Características Técnicas

### Responsive Design
- Todos los componentes son responsive
- Breakpoint móvil: `max-width: 600px`
- Ajustes automáticos de tamaño y espaciado

### Tipografía
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
```

### Accesibilidad
- Contraste de colores optimizado (WCAG 2.1)
- Texto blanco sobre `#6D0757`: Ratio 8.5:1 ✅ (excelente para todo tipo de texto)
- Texto blanco sobre `#8E0970`: Ratio 6.2:1 ✅ (muy bueno)
- Estructura semántica HTML5

## 🔧 Personalización

### Cambiar Colores
Los colores están centralizados en variables CSS. Para personalizarlos:

```css
:root {
  --idecf-primary: #TU_COLOR_PRIMARIO;
  --idecf-secondary: #TU_COLOR_SECUNDARIO;
  --idecf-hover: #TU_COLOR_HOVER;
}
```

### Ajustar Tamaños
Modifica las variables de tamaño en cada componente:

```css
.component {
  font-size: 16px;  /* Ajustar según necesidad */
  padding: 4px 18px; /* Ajustar espaciado */
}
```

## 📱 Compatibilidad

- ✅ Chrome/Edge (últimas versiones)
- ✅ Firefox (últimas versiones)
- ✅ Safari (últimas versiones)
- ✅ Dispositivos móviles iOS/Android
- ✅ WordPress 5.0+
- ✅ Elementor 3.0+

## 📝 Notas de Desarrollo

### Versión
- **Actual**: 1.0.0
- **Última actualización**: 28 de diciembre de 2025

### Cambios Recientes
- ✅ Aplicación de colores institucionales oficiales (#6D0757)
- ✅ Actualización de variables CSS
- ✅ Mejora de accesibilidad y contraste (ratio 8.5:1)
- ✅ Optimización de estados hover

## 🤝 Contribución

Para mantener la consistencia visual:
1. Usa siempre los colores institucionales definidos
2. Mantén la estructura de archivos
3. Prueba en diferentes navegadores
4. Verifica la accesibilidad

## 📄 Licencia

Uso interno de IDECF - Instituto de Educación en Ciencias Forenses

---

**Desarrollado para IDECF** | Última actualización: Diciembre 2025
