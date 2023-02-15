from fpdf import FPDF

def question(pdf):
    # text of the question
    question = input('Q: ')
    while '.........' in question:
        question = question.replace('.........', '........')
    while '……………' in question:
        question = question.replace('……………', '………')
    question = question.split(' ')

    lines = []
    line = ''
    for word in question:
        if pdf.get_string_width(line + word) <= 117:
            line += (word + ' ')
            if word == question[-1]:
                lines.append(line)
        else:
            lines.append(line)
            line = word + ' '
    # return lines

    # question switchs
    q_switch1 = 'A) ' + input('A) ')
    q_switch2 = 'B) ' + input('B) ')
    q_switch3 = 'C) ' + input('C) ')
    q_switch4 = 'D) ' + input('D) ')

    if q_switch4 == 'D)' or q_switch4 == 'D) ':
        q_switch4 = ''

    # code1
    q_code = 'Code: ' + input('code: ')

    # coordinates of the question
    question_x = 0
    question_y = 0

    return {"lines" : lines, "q_switch1" : q_switch1, "q_switch2" : q_switch2, "q_switch3" : q_switch3, "q_switch4" : q_switch4, "q_code" : q_code, "question_x" : question_x, "question_y" : question_y}


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

for i in range(1,5):
    q = question(pdf=pdf)

    if i == 1:
        q['question_x'] = 0
        q['question_y'] = 0
    elif i == 2:
        q['question_x'] = 149
        q['question_y'] = 0
    elif i == 3:
        q['question_x'] = 0
        q['question_y'] = 106
    elif i == 4:
        q['question_x'] = 149
        q['question_y'] = 106
    else:
        print("err", '******************')

    pdf.set_xy(x=q["question_x"] + 10, y=q["question_y"] + 23)

    for line in q["lines"]:
        pdf.cell(w=10, h=6, txt=line, ln=2, align='L')
    pdf.dashed_line(x1=pdf.get_x()+1, y1=pdf.get_y()+1.7, x2=pdf.get_x()+122, y2=pdf.get_y()+1.7, dash_length=1, space_length=1)

    pdf.set_xy(x=q["question_x"] + 10, y=q["question_y"] + 23 + (len(q["lines"]) + 1) * 6 - 2)

    if pdf.get_string_width(q["q_switch1"]) <= 58 and pdf.get_string_width(q["q_switch2"]) <= 58 and pdf.get_string_width(q["q_switch3"]) <= 58 and pdf.get_string_width(q["q_switch4"]) <= 58:
        pdf.cell(w=59, h=6, txt=q["q_switch1"], ln=0, align='L')
        pdf.cell(w=58, h=6, txt=q["q_switch2"], ln=0, align='L')
        pdf.set_xy(x=q["question_x"] + 10, y=q["question_y"] + 23 + (len(q["lines"]) + 2) * 6 - 2)
        pdf.cell(w=59, h=6, txt=q["q_switch3"], ln=0, align='L')
        pdf.cell(w=58, h=6, txt=q["q_switch4"], ln=0, align='L')
    else:
        pdf.cell(w=59, h=6, txt=q["q_switch1"], ln=2, align='L')
        pdf.cell(w=58, h=6, txt=q["q_switch2"], ln=2, align='L')
        pdf.cell(w=59, h=6, txt=q["q_switch3"], ln=2, align='L')
        pdf.cell(w=58, h=6, txt=q["q_switch4"], ln=2, align='L')

    pdf.set_xy(x=q["question_x"] + 10 + 62 , y=q["question_y"] + 88)
    pdf.cell(w=59, h=6, txt=q["q_code"], ln=0, align='L')

check = input('check (y/n?) :')
if check == 'y' or check == 'Y':
    num = input('return your page number :')
    pdf.output('p' + str(num) + '.pdf')
else:
    pass