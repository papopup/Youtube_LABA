import base64

with open("C:\\Users\\Pavel\\Downloads\\vcard\\pavel2.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

"""
This little script can generate a valid .vcf (vCard). It will ask you to fill
in some details and write the vcf-file.
"""

def main():
    print('Please enter contact details:')
    first_name   = input(' - First name       : ')
    last_name    = input(' - Last name        : ')
    email        = input(' - E-mail address   : ')
    company      = input(' - Company          : ')
    title        = input(' - Title            : ')
    phone_number = input(' - Phone number     : ')
    address      = input(' - Address          : ')
    link_main    = input(' - Company Web      : ')
    link_link    = input(' - Linkedin link    : ')
    link_twit    = input(' - Twitter link     : ')

    okay()
    vcf_file = f'{first_name.lower()}.vcf'
    print(f'Will be writing vcard to: {vcf_file}')
    okay()
    vcard = make_vcard(first_name, last_name, company, title, phone_number, address, email, link_main, link_link , link_twit)
    write_vcard(vcf_file, vcard)

def make_vcard(
        first_name,
        last_name,
        company,
        title,
        phone,
        address,
        email,
        link_main,
        link_link,
        link_twit):
    address_formatted = ';'.join([p.strip() for p in address.split(',')])
    return [
        'BEGIN:VCARD',
        'VERSION:4.1',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'ORG:{company}',
        f'TITLE:{title}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;WORK;VOICE:{phone}',
        f'ADR;WORK;PREF:;;{address_formatted}',
        f'URL:{link_main}',
        f'URL:{link_link}',
        f'URL:{link_twit}',
        f'PHOTO;ENCODING=BASE64;TYPE=PNG:{encoded_string}',

        f'REV:1',
        'END:VCARD'
    ]

def write_vcard(f, vcard):
    with open(f, 'w') as f:
        f.writelines([l + '\n' for l in vcard])

def okay():
    okay = input('Okay [yes/no]? ')
    if okay in ['Yes', 'yes', 'YES', 'y', 'Y', 'ok']:
        return True
    else:
        print('Cancelled.')
        exit(1)

if __name__ == "__main__":
    main()

