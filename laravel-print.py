from flask import Flask, request
import win32print

app = Flask(__name__)

@app.route('/print', methods=['POST'])
def print_receipt():
    try:
        # Ambil data dari Laravel
        content = request.json  # Laravel mengirimkan JSON
        text = content.get('text', '')

        # Konfigurasi printer
        printer_name = win32print.GetDefaultPrinter()
        hprinter = win32print.OpenPrinter(printer_name)
        win32print.StartDocPrinter(hprinter, 1, ("Print Job", None, "RAW"))
        win32print.StartPagePrinter(hprinter)
        win32print.WritePrinter(hprinter, text.encode('utf-8'))
        win32print.EndPagePrinter(hprinter)
        win32print.EndDocPrinter(hprinter)
        win32print.ClosePrinter(hprinter)

        return {"status": "success", "message": "Printed successfully"}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8004)
