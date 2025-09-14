import yaml
from fpdf import FPDF

def main() -> None:
    details = yaml_parser('test2.yml')
    generate_resume(details)

def yaml_parser(file_path: str) -> dict:
    details = {}
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

        header = {
            'name'    : data['resume']['header']['name'],
            'phone'   : data['resume']['header']['phone'],
            'email'   : data['resume']['header']['email'],
            'linkedin': data['resume']['header']['linkedin'],
            'github'  : data['resume']['header']['github'],
            'website' : data['resume']['header']['website'],
        }

        details['header'] = header

    return details

def generate_resume(details: dict):

    name = details['header']['name']
    phone = details['header']['phone']
    email = details['header']['email']
    linkedin = details['header']['linkedin']
    github = details['header']['github']
    website = details['header']['website']

    class PDF(FPDF):
        def header(self) -> None:
            self.set_font('helvetica', size=16)
            self.cell(40, 10, name)
            self.ln(20)
            pdf.cell(
                40, 
                10, 
                f'Phone: {phone}\nEmail: {email}\nLinkedin: {linkedin}\ngithub: {github}\nwebsite: {website}\n'
            )



    pdf = PDF(orientation='portrait', unit='mm', format='A4')
    pdf.add_page()
    pdf.output('output')

if __name__ == '__main__':
    main()
