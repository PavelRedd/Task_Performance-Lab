import json
import sys

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2)

def build_value_dict(values):
    return {item['id']: item['value'] for item in values}

def fill_values(tests, value_dict):
    for test in tests:
        if 'id' in test and test['id'] in value_dict:
            test['value'] = value_dict[test['id']]
        if 'values' in test:
            fill_values(test['values'], value_dict)

def main():
    if len(sys.argv) < 4:
        path1 = input("Введите путь к файлу values.json: ")
        path2 = input("Введите путь к файлу tests.json: ")
        path3 = input("Введите путь к файлу report.json: ")
    else:
        path1 = sys.argv[1]
        path2 = sys.argv[2]
        path3 = sys.argv[3]
    
    values_data = load_json(path1)
    tests_data = load_json(path2)
    
    value_dict = build_value_dict(values_data['values'])
    
    fill_values(tests_data['tests'], value_dict)
    
    save_json(path3, tests_data)

if __name__ == '__main__':
    main()
