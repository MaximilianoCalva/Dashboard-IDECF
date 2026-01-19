function doGet(e) {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var result = {};

    // 1. OBTENER TODAS LAS HOJAS AUTOMÁTICAMENTE
    var allSheets = ss.getSheets();
    var sheetNames = [];

    // 2. FILTRAR PARA IDECF (DCFG o DTGG + Números)
    // Detecta DCFG01, DTGG01, etc.
    var regex = /^(DCFG|DTGG)\d+$/;

    allSheets.forEach(function (sheet) {
        if (regex.test(sheet.getName())) {
            sheetNames.push(sheet.getName());
        }
    });

    sheetNames.forEach(function (sheetName) {
        var sheet = ss.getSheetByName(sheetName);
        if (sheet) {
            // LEER TODO EL RANGO Y LIMPIAR DATOS
            var data = sheet.getDataRange().getValues();
            var videos = [];

            // Empezar en i = 1 para saltar encabezados
            for (var i = 1; i < data.length; i++) {
                var row = data[i];

                var titulo = row[0];
                var vimeoUrl = row[1];
                var fecha = row[2];
                var profesor = row[3];

                // Validación robusta
                if (titulo && titulo.toString().trim() !== "" && titulo !== "Título del Video") {
                    videos.push({
                        titulo: titulo.toString(),
                        vimeoUrl: vimeoUrl ? vimeoUrl.toString() : "",
                        fecha: formatDate(fecha),
                        profesor: profesor ? profesor.toString() : "Academia"
                    });
                }
            }
            result[sheetName] = videos;
        }
    });

    return ContentService.createTextOutput(JSON.stringify(result))
        .setMimeType(ContentService.MimeType.JSON);
}

function formatDate(date) {
    if (!date) return "";
    if (date instanceof Date) {
        return Utilities.formatDate(date, Session.getScriptTimeZone(), "dd/MM/yyyy");
    }
    return date.toString();
}
