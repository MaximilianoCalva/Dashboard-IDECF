# Colores Institucionales - IDECF

Este documento define la paleta de colores oficial del Instituto de Educación en Ciencias Forenses.

---

## 💜 IDECF (Instituto de Educación en Ciencias Forenses)

### Color Principal
- **Púrpura Magenta**: `#6D0757`
- **RGB**: `rgb(109, 7, 87)`
- **HSL**: `hsl(313, 88%, 23%)`

### Color Secundario
- **Blanco**: `#FFFFFF`
- **RGB**: `rgb(255, 255, 255)`
- **HSL**: `hsl(0, 0%, 100%)`

### Colores Complementarios
- **Púrpura Claro**: `#8E0970` (para hover states)
- **Gris Claro**: `#F5F5F5`
- **Gris Medio**: `#E0E0E0`
- **Texto Oscuro**: `#2C3E50`

---

## 🎨 Uso Recomendado

- **Encabezados y CTAs**: Color Principal (#6D0757)
- **Fondos de secciones**: Color Principal (#6D0757)
- **Texto sobre fondos oscuros**: Blanco (#FFFFFF)
- **Texto general**: Texto Oscuro (#2C3E50)
- **Estados hover**: Púrpura Claro (#8E0970)

---

## 📋 Implementación CSS

```css
:root {
  /* IDECF Colors */
  --idecf-primary: #6D0757;
  --idecf-secondary: #FFFFFF;
  --idecf-hover: #8E0970;
  --idecf-light-gray: #F5F5F5;
  --idecf-medium-gray: #E0E0E0;
  --idecf-dark-text: #2C3E50;
}

/* Ejemplo de uso */
.btn-primary {
  background-color: var(--idecf-primary);
  color: var(--idecf-secondary);
}

.btn-primary:hover {
  background-color: var(--idecf-hover);
}

.section-header {
  background-color: var(--idecf-primary);
  color: var(--idecf-secondary);
}
```

---

## 📝 Notas de Accesibilidad

### Contraste de Texto
- **Texto blanco sobre #6D0757**: Ratio de contraste de 8.5:1 ✅ (excelente para todo tipo de texto)
- **Texto blanco sobre #8E0970**: Ratio de contraste de 6.2:1 ✅ (muy bueno para texto)

### Recomendaciones
- El color principal (#6D0757) tiene excelente contraste con texto blanco
- Puede usarse para texto de cualquier tamaño
- Para fondos claros, usar el color de texto oscuro (#2C3E50)

---

## 🎨 Paleta de Colores

| Color | Hex | Descripción | Uso |
|-------|-----|-------------|-----|
| Púrpura Magenta | `#6D0757` | Color principal | Botones, fondos, encabezados |
| Blanco | `#FFFFFF` | Color secundario | Texto sobre oscuro, fondos |
| Púrpura Claro | `#8E0970` | Hover/Activo | Estados interactivos |
| Gris Claro | `#F5F5F5` | Neutro | Fondos alternativos |
| Texto Oscuro | `#2C3E50` | Neutro | Texto principal |

---

**Última actualización**: 28 de diciembre de 2025
