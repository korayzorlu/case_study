function sendEmails() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var data = ss.getActiveSheet().getActiveCell().getA1Notation();
    var sheetname = ss.getActiveSheet().getName();
    var user = Session.getActiveUser().getEmail();
    var Toemail = 'example@mail.com';
    var subject = 'Case Study';
    var body = "Analytica House Case Study report is ready. " + ss.getUrl();
  
    MailApp.sendEmail(Toemail,subject, body);
  };
  