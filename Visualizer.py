import tomllib, os

def read_config(config_path):
    with open(config_path, "rb") as f:
        config = tomllib.load(f)
    return config


def get_dependencies(apk_path, max_depth):
    dependencies = {}
    visited = set()
    
    def extract_dependencies(package, depth):
        if depth > max_depth or package in visited:
            return
        visited.add(package)
        
        pkg_dependencies = get_package_metadata(package)
        dependencies[package] = pkg_dependencies
        
        for dep in pkg_dependencies:
            extract_dependencies(dep, depth + 1)

    extract_dependencies(apk_path, 0)
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
    
    # Построение UML-графа
    uml_content = create_text_graph(dependencies)
    
    # Генерация графа
    create_graph(uml_content, output_path, plantuml_path)
    
    print("Граф зависимостей успешно сохранен.")


def read_apkbuild(apkbuild_path):
    with open(apkbuild_path, 'r') as file:
        content = file.read()
        
    makedepends_match = re.search(r'makedepends="([^"]+)"', content)
    if makedepends_match:
        dependencies = makedepends_match.group(1).split()
        return dependencies
    else:
        return []

