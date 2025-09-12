import yaml

def main() -> None:
    details = yaml_parser('test.yml')
    print(details)

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


if __name__ == '__main__':
    main()
