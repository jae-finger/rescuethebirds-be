function deleteTestPersonRowsInMultipleSheets() {
    const sheetNames = ['Adoption Form', 'Boarding Form', 'Volunteer Form']; // Sheet names
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  
    sheetNames.forEach(sheetName => {
      const sheet = spreadsheet.getSheetByName(sheetName);
      if (!sheet) {
        console.error(`Sheet not found: ${sheetName}`);
        return;
      }
      const data = sheet.getDataRange().getValues();
      const rowsToDelete = data.reduce((acc, row, i) => {
        // Convert both the cell content and the target string to lowercase before comparison
        if (row[1].toString().toLowerCase() === 'test person' || row[1].toString().toLowerCase() === 'string') acc.push(i + 1);
        return acc;
      }, []).reverse();
  
      rowsToDelete.forEach(row => sheet.deleteRow(row));
    });
  }
  

function copyNewRows() {
  const sourceSheetId = '1VchwwZE9x0Tdb_Iy4KetjxdRg4GFTN6P4OXc5e_Y868';
  const destinationSheetId = '1fKw8NIx0hE-W9KZF1VcwlRKXLJT89-wlRsvWr4QGn-0';
  const sourceSheet = SpreadsheetApp.openById(sourceSheetId);
  const destinationSheet = SpreadsheetApp.openById(destinationSheetId);

  const tabs = Math.min(sourceSheet.getNumSheets(), destinationSheet.getNumSheets());
  for (let i = 0; i < tabs; i++) {
    const sourceTab = sourceSheet.getSheets()[i];
    const destinationTab = destinationSheet.getSheets()[i];

    const lastRowSource = sourceTab.getLastRow();
    const lastRowDestination = destinationTab.getLastRow();

    if (lastRowSource <= 1) continue;

    const sourceData = sourceTab.getRange(2, 1, lastRowSource - 1, sourceTab.getLastColumn()).getValues();
    const lastTimestampDestination = lastRowDestination > 1 ? destinationTab.getRange(lastRowDestination, 1).getValue() : new Date(0);

    sourceData.forEach(row => {
      if (row[0] > lastTimestampDestination) {
        destinationTab.appendRow(row);
      }
    });
  }
}

function setUpTrigger() {
  ScriptApp.newTrigger('combinedFunction')
    .timeBased()
    .everyHours(1)
    .create();
}

function combinedFunction() {
  deleteTestPersonRowsInMultipleSheets();
  copyNewRows();
}

function main() {
  setUpTrigger();
  // combinedFunction(); // Uncomment to run immediately
}
