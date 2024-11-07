import tomllib, os, re
from plantuml import PlantUML

def read_config(config_path):
    with open(config_path, "rb") as f:
        config = tomllib.load(f)
    return config


def read_apkbuild(apkbuild_path):
    with open(apkbuild_path, 'r') as file:
        content = file.read()
        
    makedepends_match = re.search(r'makedepends="([^"]+)"', content)
    if makedepends_match:
        dependencies = makedepends_match.group(1).split()
        return dependencies
    else:
        return []

def generate_plantuml(dependencies):
    plantuml_code = "@startuml\n"
    for dep in dependencies:
        plantuml_code += f"package --> {dep}\n"
    plantuml_code += "@enduml\n"
    return plantuml_code

def write_plantuml(output_file, plantuml_code):
    with open(output_file, 'w') as file:
        file.write(plantuml_code)

def create_graph(uml_content, output_path, plantuml_path):
    os.system(f"{plantuml_path} {output_path}")

def main(config_path):
    config = read_config(config_path)

    apk_path = config['apk']['path']
    output_path = config['output']['path']
    plantuml_path = config['plantuml']['path']
    max_depth = config['analysis']['max_depth']
    
    # Извлечение зависимостей
    dependencies = read_apkbuild(apk_path)
    
    plantuml_code = generate_plantuml(dependencies)
    
    write_plantuml(output_path, plantuml_code)
    
    print(plantuml_code)

    plantuml_server = PlantUML(url='http://www.plantuml.com/plantuml/png/')

    with open('graph.png', 'wb') as f:
        f.write(plantuml_server.processes(plantuml_code))
    
    #output_image_path = os.path.dirname(output_path)
    print(f"Сохранение PlantUML кода в файл {output_path}")
    # Генерация графа
    #create_graph(plantuml_code, output_path, plantuml_path)
    
    print("Граф зависимостей успешно сохранен.")


main('config.toml')
