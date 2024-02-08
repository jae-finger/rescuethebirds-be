// Deletes rows containing "test person" or "string" from specified sheets
function deleteRowsFromSheets() {
    // Define the names of the sheets to check
    const sheetNames = ['Adoption Form', 'Boarding Form', 'Volunteer Form'];
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  
    // Iterate over each sheet name
    sheetNames.forEach(sheetName => {
        const sheet = spreadsheet.getSheetByName(sheetName);
        if (!sheet) {
            console.error(`Sheet not found: ${sheetName}`);
            return;
        }
        // Get all data from the sheet
        const data = sheet.getDataRange().getValues();
        // Determine which rows to delete
        const rowsToDelete = data.reduce((acc, row, index) => {
            if (row[1].toString().toLowerCase() === 'test person' || row[1].toString().toLowerCase() === 'string') acc.push(index + 1);
            return acc;
        }, []).reverse(); // Reverse to delete from the bottom up
  
        // Delete identified rows
        rowsToDelete.forEach(row => sheet.deleteRow(row));
    });
}

// Copies new rows from source to destination sheet if they contain text
function copyNewRowsAndUpdate() {
    const sourceSheetId = '1VchwwZE9x0Tdb_Iy4KetjxdRg4GFTN6P4OXc5e_Y868';
    const destinationSheetId = '1fKw8NIx0hE-W9KZF1VcwlRKXLJT89-wlRsvWr4QGn-0';
    const sourceSheet = SpreadsheetApp.openById(sourceSheetId);
    const destinationSheet = SpreadsheetApp.openById(destinationSheetId);
  
    let newRowsAdded = 0; // Initialize counter for new rows added

    // Determine the number of tabs to process based on the smaller number of sheets
    const tabs = Math.min(sourceSheet.getNumSheets(), destinationSheet.getNumSheets());
    for (let i = 0; i < tabs; i++) {
        const sourceTab = sourceSheet.getSheets()[i];
        const destinationTab = destinationSheet.getSheets()[i];
        const lastRowSource = sourceTab.getLastRow();
        const lastRowDestination = destinationTab.getLastRow();

        if (lastRowSource <= 1) continue; // Skip if source tab has no data rows

        // Retrieve source data excluding headers
        const sourceData = sourceTab.getRange(2, 1, lastRowSource - 1, sourceTab.getLastColumn()).getValues();
        const lastTimestampDestination = lastRowDestination > 1 ? destinationTab.getRange(lastRowDestination, 1).getValue() : new Date(0);

        // Copy rows with a timestamp later than the last destination timestamp and containing text
        sourceData.forEach(row => {
            if (row[0] > lastTimestampDestination && row.join("").trim() !== "") {
                destinationTab.appendRow(row);
                newRowsAdded++; // Increment for each new row added
            }
        });
    }

    return newRowsAdded; // Return the count of new rows added
}

// Sets up a time-based trigger to run combined operations
function setUpTimeTrigger() {
    ScriptApp.newTrigger('runCombinedOperations')
        .timeBased()
        .everyHours(1)
        .create();
}

// Combines deletion, copying, and email notification into a single operation
function runCombinedOperations() {
    deleteRowsFromSheets();
    const newRowsCount = copyNewRowsAndUpdate();

    // Send an email if new rows were added
    if (newRowsCount > 0) {
        const emailAddress = 'jaefinger@gmail.com'; // Define the recipient email address
        const subject = 'Sheet Update: New Rows Added';
        const body = `${newRowsCount} new rows with text were added to the destination sheet.`;
        MailApp.sendEmail(emailAddress, subject, body); // Send the email
    }
}

// Main function to set up the trigger; optionally run combined operations immediately
function main() {
    setUpTimeTrigger();
    // runCombinedOperations(); // Uncomment to run immediately for testing
}
