from fpdf import FPDF

# text of the question1
question1 = input()
while '.........' in question1:
    question1 = question1.replace('.........', '........')
while '……………' in question1:
    question1 = question1.replace('……………', '………')
question1 = question1.split(' ')
lines = []

def lines_of_question1(pdf, lines):
    line = ''
    for word in question1:
        if pdf.get_string_width(line + word) <= 117:
            line += (word + ' ')
            if word == question1[-1]:
                lines.append(line)
        else:
            lines.append(line)
            line = word + ' '
    return lines

# question1 switchs
q1_switch1 = 'A) anything so beal' # must be taken from the entrance
q1_switch2 = 'B) so beautiful anyt11111111' # must be taken from the entrance
q1_switch3 = 'C) so beautiful e' # must be taken from the entrance
q1_switch4 = 'D) anything was ' # must be taken from the entrance

# code1
q1_code = 'Code: 123456789' # must be taken from the entrance

# coordinates of the question1
question1_x = 0
question1_y = 0

# text of the question2
# question2 switchs
# code2
# coordinates of the question2
question2_x = 149
question2_y = 0


# text of the question3
# question3 switchs
# code3
# coordinates of the question3
question3_x = 0
question3_y = 106


# text of the question4
# question4 switchs
# code4
# coordinates of the question4
question4_x = 149
question4_y = 106


# create landscape A4 page
pdf = FPDF(orientation='L', unit='mm', format='A4')
pdf.set_auto_page_break(False)

# add font
pdf.add_font('OpenSans B', '', "OpenSans-Bold.ttf", uni=True)
pdf.set_font('OpenSans B', '', 14)

# add page
pdf.add_page()

# add background
pdf.image(name= 'A4.jpg', x=0, y=0, w=297, h=210, type='jpg')

# 1111111111111111111

pdf.set_xy(x=question1_x + 10, y=question1_y + 23)

lines = lines_of_question1(pdf=pdf, lines=lines)
for line in lines:
    pdf.cell(w=10, h=6, txt=line, ln=2, align='L')
pdf.dashed_line(x1=pdf.get_x()+1, y1=pdf.get_y()+1.7, x2=pdf.get_x()+122, y2=pdf.get_y()+1.7, dash_length=1, space_length=1)

pdf.set_xy(x=question1_x + 10, y=question1_y + 23 + (len(lines) + 1) * 6 - 2)

if pdf.get_string_width(q1_switch1) <= 58 and pdf.get_string_width(q1_switch2) <= 58 and pdf.get_string_width(q1_switch3) <= 58 and pdf.get_string_width(q1_switch4) <= 58:
    pdf.cell(w=59, h=6, txt=q1_switch1, ln=0, align='L')
    pdf.cell(w=58, h=6, txt=q1_switch2, ln=0, align='L')
    pdf.set_xy(x=question1_x + 10, y=question1_y + 23 + (len(lines) + 2) * 6 - 2)
    pdf.cell(w=59, h=6, txt=q1_switch3, ln=0, align='L')
    pdf.cell(w=58, h=6, txt=q1_switch4, ln=0, align='L')
else:
    pdf.cell(w=59, h=6, txt=q1_switch1, ln=2, align='L')
    pdf.cell(w=58, h=6, txt=q1_switch2, ln=2, align='L')
    pdf.cell(w=59, h=6, txt=q1_switch3, ln=2, align='L')
    pdf.cell(w=58, h=6, txt=q1_switch4, ln=2, align='L')

pdf.set_xy(x=question1_x + 10 , y=question1_y + 88)
pdf.cell(w=59, h=6, txt=q1_code, ln=0, align='L')

pdf.output('q.pdf')