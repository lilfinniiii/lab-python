import json
import jsonschema

def task1(json_file_path, age_threshold):
    names_above_age = []

    with open(json_file_path, 'r') as file:
        data = json.load(file)

        for person in data:
            if person.get('age') and person['age'] > age_threshold:
                names_above_age.append(person['name'])

    return names_above_age



def task2(data_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json_data = json.dumps(data_list, ensure_ascii=False, indent=4)
        file.write(json_data)

    return json_data



def task3(schema, file_paths):
    invalid_files = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        try:
            jsonschema.validate(instance=json_data, schema=schema)
        except jsonschema.exceptions.ValidationError:
            invalid_files.append(file_path)
    return invalid_files


def task4(json_data, key):
    results = []

    if isinstance(json_data, dict):
        if key in json_data:
            results.append(json_data[key])
        for k, v in json_data.items():
            results.extend(task4(v, key))
    elif isinstance(json_data, list):
        for item in json_data:
            results.extend(task4(item, key))

    return results


def task5(file_path, category, update_function):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    for item in json_data:
        if item.get('category') == category:
            update_function(item)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)
    print("Update data:")
    print(json.dumps(json_data, indent=4))
    item['price'] += 10 
