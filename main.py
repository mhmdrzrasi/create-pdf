from fpdf import FPDF

# create landscape A4 page
pdf = FPDF(orientation='L', unit='mm', format='A4')

# add font
pdf.add_font('OpenSans B', '', "OpenSans-Bold.ttf", uni=True)
pdf.set_font('OpenSans B', '', 10)

# add page
pdf.add_page()

# add background
pdf.image(name= 'A4.jpg', x=0, y=0, w=297, h=210, type='jpg')

pdf.output('q.pdf')