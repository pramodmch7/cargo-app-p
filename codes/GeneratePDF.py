from flask import current_app as app
import os
from fpdf import FPDF, HTMLMixin
import num2words
import time


class PDF(FPDF, HTMLMixin):

    def SerialNumber(self, serialNo, date):
        title_w = self.get_string_width(serialNo) + 3
        doc_w = self.w
        self.set_x(140)
        self.set_line_width(0.1)
        self.cell(34, 6, serialNo, border=1, ln=0, align='C')
        self.cell(32, 6, date.strftime('%d/%m/%Y'),
                  border=1, ln=0, align='C')

    def header(self):
        self.set_font('helvetica', '', 12)
        # self.cell(0, 0, 'KOMITLA TRANSLINES', border=0, ln=1, align='L')
        self.set_font('helvetica', 'B', 16)
        self.image('pdfAsset/HLogo1.png', 10, 5, 50)
        self.ln(16)
        self.set_y(9)
        self.cell(0, 0, 'Luggage Slip', border=0, ln=1, align='C')
        self.ln(10)
        self.set_y(24.1)
        self.set_font('helvetica', '', 12)
        self.cell(0, -1, '# 21/2, TSP Road, Kalasipalyam,',
                  ln=1, align='L')
        self.cell(0, 10, 'Opp Bus Statnd, Bangalore - 560002. ', ln=1, align='L')
        self.image('pdfAsset/loc.png', x=82, y=24, w=5,
                   link='https://www.google.com/maps/place/Komitla+Tours+%26+Travels/@12.9587294,77.5775428,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae15e4470e34f5:0x748f9d1982699eef!8m2!3d12.9587073!4d77.5775449')
        self.set_y(29)
        self.cell(
            0, 7, 'Ph: 95133 81025 / 93416 50777 / ', ln=1, align='L')
        self.cell(
            0, 2, '       93437 82777 ', ln=1, align='L')
        self.set_y(32)

        self.line(0, 40, 210, 40)

    def footer(self):
        # Set position of the footer
        self.line(0, 133, 210, 133)
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'B', 9)
        self.cell(
            0, 5, '* No Compensation for Misplacement or Damage.', align='L', ln=1)

        self.cell(0, 5, '* Condition overleaf read & accepted.', align='L', ln=1)

    def addDetails(self, data):
        # print(data)
        self.set_x(10)
        self.set_y(67)

        self.set_font('helvetica', 'B', 12)
        self.cell(3, 5, data['PName'][1], ln=0, align='L')
        self.set_font('helvetica', '', 12)
        self.cell(15, 5, f'{"Weight"}', ln=0, align='L')
        self.cell(20, 5, f"{data['PWeight'][1]} kg", ln=0, align='L')
        self.cell(25, 5, f"{data['PArricle'][0]}", ln=0, align='L')
        self.cell(15, 5, f"{data['PArricle'][1]}", ln=0, align='L')

    def addInfo(self, data):
        self.set_font('helvetica', 'B', 12)
        self.set_x(200)
        self.set_y(40)
        self.cell(60, 7, f"{data['CName'][0]}", ln=1, align='L')
        self.set_font('helvetica', '', 12)
        self.cell(
            60, 5, f"{data['CName'][1]}", ln=1, align='L')
        self.cell(
            60, 5, f"{data['CPhone'][1]}", ln=1, align='L')
        self.cell(
            60, 5, f"{data['CLocation'][1]}", ln=1, align='L')
        self.set_y(63)

        self.set_font('helvetica', 'B', 12)
        # self.set_x(200)
        self.set_y(40)
        self.cell(190, 7, f"{data['DName'][0]}", ln=1, align='R')
        self.set_font('helvetica', '', 12)
        self.cell(
            190, 5, f"{data['DName'][1]}", ln=1, align='R')
        self.cell(
            190, 5, f"{data['DPhone'][1]}", ln=1, align='R')
        self.cell(
            190, 5, f"{data['DLocation'][1]}", ln=1, align='R')
        self.set_y(63)

        self.line(0, 63, 210, 63)
        self.line(200, 93, 124, 93)
        self.line(200, 109, 124, 109)

        # <p><B>To,</B></p>
        # <p>{data['CName'][0]} {data['CName'][1]}</p>
        # <p align='left'>{data['CPhone'][1]}</p>
        # <p align='left'>{''}</p>
        # <p align='left'>{data['MName'][1]}</p>

    def addTable(self, data):
        # print(data)
        self.set_font('helvetica', '', 12)
        self.set_y(67)
        self.write_html(f"""

    <table  width = 100% align="center" border="1">
      <thead>
        <tr>
          <th align="left" width="60%">Particulars</th>
          <th align="left" width="20%"> </th>
          <th align="left" width="20%">Price</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td align="left">{data['TC'][0]}</td>
          <td align="right">{data['TC'][1]}</td>
          <td> </td>
        </tr>
        <tr>
          <td align="left">{data['LC'][0]}</td>
          <td align="right">{data['LC'][1]}</td>
          <td> </td>
        </tr>
        <tr>
          <td align="right">{data['TO'][0]}</td>
          <td> </td>
          <td align="left">{data['TO'][1]}</td>
        </tr>
        <tr>
          <td align="left">{data['AP'][0]}</td>
          <td align="right">{data['AP'][1]}</td>
          <td> </td>
        </tr>


        <tr>
          <td> </td>
          <td> </td>
          <td> </td>
        </tr>

        <tr>
          <td align="right"><B>{data['TP'][0]}</B></td>
          <td> </td>
          <td> <img src='pdfAsset/Rupee.png' width='12'/><B>  {data['TP'][1]}</B></td>
        </tr>

      </tbody>
    </table>
</section>
""")

    def addWordRupieeAttand(self, data):
        self.set_font('helvetica', '', 12)
        self.set_y(130)
        self.cell(34, 7, 'Rupees in words: ', ln=0, align='L')
        self.set_font('helvetica', '', 12)
        self.cell(
            0, 7, f"{num2words.num2words(data['TP'][1], lang='en_IN').replace('-',' ').title()} Only.", ln=1, align='L')

        self.set_x(130)
        self.set_font('helvetica', '', 12)
        self.set_y(-75)
        self.cell(
            0, 7, f"{data['UD'][0]} {data['UD'][1]}", ln=1, align='R')
        # self.set_x(127)
        self.image('pdfAsset/pho.png', w=5, y=230, x=169,
                   link=f"tel:+91{data['UD'][3]}")
        # self.set_y(-77)
        # self.set_x(135)
        self.cell(0, 7, f"{data['UD'][3]}", ln=0, align='R')
        self.line(10, 123, 200, 123)


def GenPDF(serialNo, date, data, FileId):

    Pdf = PDF('P', 'mm', (210, 148.5))
    # Pdf = PDF('P', 'mm', (210, 297))
    # Pdf = PDF('P', 'mm', 'A4')

    Pdf.add_page()
    Pdf.set_font('helvetica', '', 16)
    Pdf.SerialNumber(serialNo, date)
    Pdf.addInfo(data)
    Pdf.addTable(data)
    Pdf.addDetails(data)
    # Pdf.addWordRupieeAttand(data)
    # if data['ABeka']:
    #     Pdf.AccList(data)
    # if data['FBeka']:
    #     Pdf.FinanceDetails(data)

    # Pdf.cell(10, 10, 'HanU')

    # pdfName = f"{data['CName'][1]}-{data['CPhone'][1]}-{time.time()}.pdf"

    # pdfName = f"pdfAsset\\CRecip\\{data['CName'][1]}-{data['CPhone'][1]}-{FileId}"
    # pdfName = f"pdfAsset\\CRecip\\{FileId}"
    pdfName = os.path.join(app.config['upload_path'], FileId)

    Pdf.output(pdfName)
    return(pdfName)
