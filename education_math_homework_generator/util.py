import os
import subprocess


def remove_temporary_files(filename, extensions=('.tex', '.aux', '.log')):
    for extension in extensions:
        if os.path.isfile(filename.replace('.tex', extension)):
            os.unlink(filename.replace('.tex', extension))


def open_pdf(pdf_filename, pdf_viewer='evince'):
    os.system('{} {} & '.format(pdf_viewer, pdf_filename))


def write_latex_data_to_file(filename, contents):
    with open(filename, 'w') as output_file:
        output_file.write(contents)


def convert_latex_to_pdf(filename, command='pdflatex', options='-interaction nonstopmode', contents=None, view=False):
    if contents is not None:
        write_latex_data_to_file(filename, contents)

    full_command_line = '{} {} {}'.format(command, options, filename)
    proc = subprocess.Popen(full_command_line.split())
    proc.communicate()
    pdf_filename = filename.replace('.tex', '.pdf')
    return_code = proc.returncode
    if not return_code == 0:
        os.unlink(pdf_filename)
        raise ValueError('Error {} executing command: {}'.format(return_code, full_command_line))

    if view:
        open_pdf(pdf_filename)
