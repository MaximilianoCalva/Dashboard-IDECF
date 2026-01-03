# Notas de Implementación - Datos Reales

## 📊 Datos Cargados

Se ha creado el archivo `alumnos-constelaciones-gen01.csv` con **14 alumnos** de la Generación 01 del Diplomado en Constelaciones Familiares.

---

## 🔑 Formatos de Código Detectados

Los códigos de alumno tienen diferentes prefijos:

| Prefijo | Cantidad | Ejemplos |
|---------|----------|----------|
| **CF** | 7 | CFP101, CFB103, CFD104, CFG107, CFE108, CFL110, CFF112 |
| **D** | 7 | DS109, DR243, DM295, DT515, DT803, DM793, DG700 |

---

## 💳 Códigos de Tabla de Pagos

El sistema automáticamente genera el código de pagos agregando **P** al inicio:

### Ejemplos de Conversión

| Código Alumno | Código Tabla Pagos | Shortcode |
|---------------|-------------------|-----------|
| DS109 | **PDS109** | `[table id=PDS109 /]` |
| CFP101 | **PCFP101** | `[table id=PCFP101 /]` |
| DR243 | **PDR243** | `[table id=PDR243 /]` |
| DM295 | **PDM295** | `[table id=PDM295 /]` |
| CFB103 | **PCFB103** | `[table id=PCFB103 /]` |

---

## 📝 Tablas Requeridas en TablePress

### Tablas Individuales (Pagos)
Debes crear una tabla para cada alumno con el formato `P{CODIGO}`:

```
PDS109
PCFP101
PDR243
PDM295
PDT515
PCFB103
PCFD104
PDT803
PDM793
PCFG107
PCFE108
PDG700
PCFL110
PCFF112
```

### Tablas Compartidas
Estas tablas son las mismas para todos los alumnos:
- `Calificaciones`
- `Terapias`

---

## 🚀 Cómo Usar con Datos Reales

### Opción 1: Cargar desde CSV

```javascript
// Cargar el archivo CSV
fetch('alumnos-constelaciones-gen01.csv')
    .then(response => response.text())
    .then(csvData => {
        loadFromCSV(csvData);
    });
```

### Opción 2: URL con Parámetro

```
https://tudominio.com/dashboard?codigo=DS109
https://tudominio.com/dashboard?codigo=CFP101
https://tudominio.com/dashboard?codigo=DR243
```

### Opción 3: Hardcode para Pruebas

```javascript
loadStudentData({
    email: 'gaby_170802@hotmail.com',
    nombre: 'SANDRA GABRIELA LEÓN COVARRUBIAS',
    codigo: 'DS109'
});
```

---

## ✅ Checklist de Implementación

### 1. Preparar TablePress
- [ ] Crear 14 tablas de pagos (una por alumno)
- [ ] Crear tabla `Calificaciones` (compartida)
- [ ] Crear tabla `Terapias` (compartida)

### 2. Crear Templates de Elementor
- [ ] Template 5713 - Intro registro de pagos
- [ ] Template 5714 - Intro calificaciones exámenes
- [ ] Template 5715 - Intro calificación total
- [ ] Template 5716 - Intro registro terapia
- [ ] Template 458 - Contenido exámenes

### 3. Configurar Acceso
- [ ] Definir cómo identificar al alumno actual
- [ ] Configurar parámetro URL o sesión WordPress
- [ ] Probar con diferentes códigos

### 4. Poblar Datos
- [ ] Cargar datos de pagos para cada alumno
- [ ] Cargar calificaciones generales
- [ ] Cargar registros de terapia

---

## 🔧 Ejemplo de Prueba

Para probar con **SANDRA GABRIELA LEÓN COVARRUBIAS (DS109)**:

1. **URL:** `?codigo=DS109`
2. **Tabla de pagos:** `PDS109`
3. **Email mostrado:** `gaby_170802@hotmail.com`
4. **Nombre mostrado:** `SANDRA GABRIELA LEÓN COVARRUBIAS`

---

## 📋 Lista de Alumnos para Referencia

1. DS109 - SANDRA GABRIELA LEÓN COVARRUBIAS
2. CFP101 - Paulina Zamudio
3. DR243 - María del Rosario Hernández Mendoza
4. DM295 - Marianella Eudocia Dioses Dioses
5. DT515 - Tatiana Anita Lans Montferrier
6. CFB103 - Brenda Sagrario Muñoz
7. CFD104 - Dennisse Cecilia Tovar
8. DT803 - Thelma Abrego Villareal
9. DM793 - Ana Verónica Salgado (Flaitz)
10. CFG107 - Gabriela Luna Diaz
11. CFE108 - Erika Arisbey Velazquez Ortega
12. DG700 - Gladis Macias Salazar
13. CFL110 - Lorena Noemí Lucero
14. CFF112 - Fabiola Rubío Sánchez

---

**Total de alumnos:** 14  
**Archivo CSV:** `alumnos-constelaciones-gen01.csv`  
**Componente:** `seccion-02-informacion-alumno-idecf.html`
