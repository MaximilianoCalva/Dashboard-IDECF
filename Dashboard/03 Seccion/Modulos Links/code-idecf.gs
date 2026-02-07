function doGet(e) {
  // CORS Layout
  var headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type"
  };

  // Get parameters
  var type = e.parameter.type; // 'aulatv', 'material'
  var module = e.parameter.module; // '1', '2', etc.
  var course = e.parameter.course; // 'constelaciones1', 'constelaciones2', 'gestalt'

  // Map courses to Spreadsheet IDs
  // USER: FILL THESE IDS WITH YOUR GOOGLE SHEET IDS
  var sheetIds = {
    'constelaciones1': '1hEsyyTPVU3w4VTcGOOVGPpWjr8xKSFMbr1Dh-ipaaPg',
    'constelaciones2': '14wl2W8kjLad8BBwIDaiidM9rridOUErGJXPwESsJE3Q',
    'gestalt': '17v9SOXL-aaXk1gE73Sd9Y-0YcS4tHmjQxibK-WbNdjM'
  };

  var spreadsheetId = sheetIds[course];

  if (!spreadsheetId || spreadsheetId.includes('REPLACE')) {
    return ContentService.createTextOutput(JSON.stringify({ 
      error: 'Spreadsheet ID not configured for course: ' + course 
    }))
    .setMimeType(ContentService.MimeType.JSON);
  }

  // Determine Sheet Name (Tab) based on type and module
  // Convention: "Aula TV M1", "Material M1"
  var sheetName = "";
  if (type === 'aulatv') {
    sheetName = "AulaTV M" + module;
  } else if (type === 'material') {
    sheetName = "Material M" + module;
  }

  // Fetch Data
  try {
    var ss = SpreadsheetApp.openById(spreadsheetId);
    var sheet = ss.getSheetByName(sheetName);

    if (!sheet) {
      return ContentService.createTextOutput(JSON.stringify({ error: 'Sheet not found: ' + sheetName }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    var data = sheet.getDataRange().getValues();
    var headersRow = data[0];
    var rows = data.slice(1);

    var result = rows.map(function(row) {
      var obj = {};
      headersRow.forEach(function(header, index) {
        obj[header] = row[index];
      });
      return obj;
    });

    return ContentService.createTextOutput(JSON.stringify(result))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
