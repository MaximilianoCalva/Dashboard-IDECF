# Dashboard de Información del Alumno - IDECF

## 📋 Descripción

Componente HTML para mostrar información personalizada del alumno con secciones expandibles para registros académicos y administrativos.

---

## 📁 Archivos

- **`seccion-02-informacion-alumno-idecf.html`** - Componente principal
- **`alumnos-ejemplo.csv`** - Plantilla CSV con datos de ejemplo

---

## 🎨 Características

### Card de Información del Alumno
- Correo electrónico
- Nombre completo
- Número de alumno
- Diseño con colores IDECF (#6D0757)

### Secciones Expandibles (Show/Hide)

1. **💳 Registro de Pagos**
   - Shortcode intro: `[elementor-template id="5713"]`
   - Tabla: `[table id=P{CODIGO_ALUMNO} /]`
   - Ejemplo: `[table id=PPDCF001 /]`

2. **📊 Calificación Total**
   - Shortcode: `[elementor-template id="5715"]`
   - Tabla: `[table id=Calificaciones /]`

3. **📝 Calificaciones de Exámenes**
   - Intro: `[elementor-template id="5714"]`
   - Contenido: `[elementor-template id="458"]`

4. **🩺 Registro de Terapia**
   - Shortcode: `[elementor-template id="5716"]`
   - Tabla: `[table id=Terapias /]`

---

## 💻 Uso en Elementor

### Paso 1: Agregar HTML Widget
1. En Elementor, arrastra un widget **HTML**
2. Copia el contenido de `seccion-02-informacion-alumno-idecf.html`
3. Pega en el widget HTML

### Paso 2: Los shortcodes se procesarán automáticamente
- Elementor renderizará los templates automáticamente
- Las tablas se mostrarán según el ID especificado

---

## 📊 Formato CSV

### Estructura del Archivo

```csv
codigo,nombre,email
PDCF001,Juan Pérez García,juan.perez@idecf.com
PDCF002,María González López,maria.gonzalez@idecf.com
```

### Campos Requeridos

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `codigo` | Número de alumno | PDCF001 |
| `nombre` | Nombre completo | Juan Pérez García |
| `email` | Correo electrónico | juan.perez@idecf.com |

---

## 🔧 Configuración Dinámica

### Cargar Datos del Alumno

**Opción 1: Desde JavaScript (datos hardcoded)**
```javascript
const studentData = {
    email: 'juan.perez@idecf.com',
    nombre: 'Juan Pérez García',
    codigo: 'PDCF001'
};
loadStudentData(studentData);
```

**Opción 2: Desde CSV**
```javascript
// Cargar archivo CSV
fetch('alumnos-ejemplo.csv')
    .then(response => response.text())
    .then(csvData => {
        loadFromCSV(csvData);
    });
```

**Opción 3: Desde URL Parameter**
```
https://tudominio.com/dashboard?codigo=PDCF001
```
El código detectará automáticamente el parámetro `codigo` en la URL.

---

## 🎯 Sustitución de Códigos

### Tabla de Pagos
- **Formato:** `P` + código de alumno
- **Ejemplo:** Si el alumno es `PDCF001`, la tabla será `PPDCF001`
- **Shortcode:** `[table id=PPDCF001 /]`

### Tablas Fijas
- **Calificaciones:** `[table id=Calificaciones /]` (sin código)
- **Terapias:** `[table id=Terapias /]` (sin código)

---

## 📱 Responsive Design

- **Desktop (>768px):** Grid de 3 columnas para info del alumno
- **Tablet (≤768px):** Grid de 2 columnas
- **Móvil (≤480px):** 1 columna (stack vertical)

---

## 🎨 Colores IDECF

- **Principal:** `#6D0757` (morado)
- **Secundario:** `#8B0969` (morado claro)
- **Hover:** `#550545` (morado oscuro)

---

## ✅ Funcionalidades JavaScript

### Toggle Sections
- Click en cualquier sección para expandir/colapsar
- Animación suave (0.4s)
- Icono rotativo (▼ → ▲)

### Cargar Datos
- `loadStudentData(data)` - Carga datos del alumno
- `loadFromCSV(csvData)` - Parsea y carga desde CSV
- `getCurrentStudentCode()` - Obtiene código actual

---

## 📝 Notas Importantes

1. **Shortcodes de Elementor** se procesan automáticamente
2. **Tablas** deben existir en TablePress con los IDs especificados
3. **Código de alumno** debe seguir formato: `PDCF###`
4. **CSV** debe usar codificación UTF-8

---

## 🚀 Próximos Pasos

1. Cargar alumnos reales en CSV
2. Configurar tablas en TablePress
3. Crear templates de Elementor (IDs: 5713, 5714, 5715, 5716, 458)
4. Probar con diferentes códigos de alumno
5. Implementar en página de WordPress

---

**Versión:** 1.0  
**Colores:** IDECF (#6D0757)  
**Compatible con:** Elementor, TablePress
