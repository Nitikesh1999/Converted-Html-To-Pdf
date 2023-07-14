from django.conf import settings
from django.template.loader import get_template
from django.http import HttpResponse
import os
import pdfkit

wkhtml_to_pdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"


def html_to_pdf(request, *args, **kwargs):
    options = {
        'page-size': 'A4',
        'orientation': 'Portrait',
        'dpi': 300,
        'no-outline': None
    }
    template_path = 'resume.html'
    template = get_template(template_path)

    context = {"name": "tree Seher"}
    html = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf=wkhtml_to_pdf)

    temp_html_path = "temp.html"
    with open(temp_html_path, 'w', encoding='utf-8') as temp_file:
        temp_file.write(html)

    # Generate the PDF from the HTML file
    pdf = pdfkit.from_file(temp_html_path, False, configuration=config, options=options)

    # Delete the temporary HTML file
    os.remove(temp_html_path)

    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    # print(response.status_code)
    if response.status_code != 200:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response