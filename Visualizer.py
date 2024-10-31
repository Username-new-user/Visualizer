import tomllib, os, re

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


def get_dependencies(apk_path, max_depth):
    dependencies = []
    queue = [(apk_path, 0)]
    
    while queue:
        apk_path, depth = queue.pop(0)
        dependencies += read_apkbuild(apk_path)
        
        if depth < max_depth:
            for dependency in read_apkbuild(apk_path):
                queue.append((dependency, depth + 1))
                
    return dependencies


def get_package_metadata(package):
    return ['dep1', 'dep2', 'dep3']

def create_text_graph(dependencies):
    pass

def create_graph(uml_content, output_path, plantuml_path):
    pass

def main(config_path):
    config = read_config(config_path)

    apk_path = config['apk']['path']
    output_path = config['output']['path']
    plantuml_path = config['plantuml']['path']
    max_depth = config['analysis']['max_depth']
    
    # Извлечение зависимостей
    dependencies = get_dependencies(apk_path, max_depth)
    print('here')
    
    # Построение UML-графа
    uml_content = create_text_graph(dependencies)
    
    # Генерация графа
    create_graph(uml_content, output_path, plantuml_path)
    
    print("Граф зависимостей успешно сохранен.")


main('config.toml')