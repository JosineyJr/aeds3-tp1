from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def generate_pdf(analysis_data, sizes_qty):
    data = [
        ["Tam.", "Tipo Arquivo", "Tipo Busca", "Sequencial", "",
         "Árvore Binária", "", "AVL", ""],
        ["", "", "", "No Comp.", "Tempo", "No Comp.", "Tempo", "No Comp.", "Tempo"],
    ]

    data += analysis_data

    doc = SimpleDocTemplate("tabela_resultados.pdf",
                            pagesize=landscape(letter))

    table = Table(data)

    sizes_to_merge = [('SPAN', (0, 2 + (index * 3 + index*1)), (0, 5 + (index * 3 + index*1)))
                      for index in range(sizes_qty)]

    file_types_to_merge = [('SPAN', (1, 2 + (index*2)), (1, 3 + (index*2)))
                           for index in range(len(analysis_data))]

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 1), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 1), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 1), 12),
        ('BACKGROUND', (0, 2), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN', (0, 0), (0, 1)),
        ('SPAN', (1, 0), (1, 1)),
        ('SPAN', (2, 0), (2, 1)),
        ('SPAN', (3, 0), (4, 0)),
        ('SPAN', (5, 0), (6, 0)),
        ('SPAN', (7, 0), (8, 0)),
    ] + sizes_to_merge + file_types_to_merge)

    table.setStyle(table_style)

    elements = []
    elements.append(table)
    doc.build(elements)
