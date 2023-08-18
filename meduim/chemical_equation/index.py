import numpy as np

def parse_molecule(molecule):
    """
    Parse the molecule string and extract the elements and their counts.
    """
    elements = {}
    current_element = ""
    current_count = 0

    for char in molecule:
        if char.isupper():
            if current_element != "":
                if current_element in elements:
                    elements[current_element] += current_count or 1
                else:
                    elements[current_element] = current_count or 1
                current_count = 0
            current_element = char
        elif char.islower():
            current_element += char
        elif char.isdigit():
            current_count = current_count * 10 + int(char)

    if current_element != "":
        if current_element in elements:
            elements[current_element] += current_count or 1
        else:
            elements[current_element] = current_count or 1

    return elements

def balance_equation(equation):
    """
    Balance the given chemical equation.
    """
    reactants, products = equation.split("->")
    reactant_molecules = reactants.strip().split("+")
    product_molecules = products.strip().split("+")

    all_elements = set()
    for molecule in reactant_molecules + product_molecules:
        elements = parse_molecule(molecule)
        all_elements.update(elements.keys())

    num_elements = len(all_elements)
    num_molecules = len(reactant_molecules) + len(product_molecules)

    matrix = np.zeros((num_elements, num_molecules))
    equation_values = np.zeros(num_elements)

    # Populate the matrix
    equation_index = 0
    for molecule_index, molecule in enumerate(reactant_molecules + product_molecules):
        elements = parse_molecule(molecule)
        for element, count in elements.items():
            element_index = list(all_elements).index(element)
            matrix[element_index][molecule_index] = -count if equation_index < len(reactant_molecules) else count
        equation_index += 1

    # Perform matrix balancing
    coefficients = np.linalg.lstsq(matrix, equation_values)[0]
    coefficients = np.round(coefficients / np.gcd.reduce(coefficients))
    coefficients = coefficients.astype(int)

    # Format the balanced equation
    balanced_equation = ""
    for molecule_index, molecule in enumerate(reactant_molecules + product_molecules):
        coefficient = coefficients[molecule_index]
        if balanced_equation != "":
            balanced_equation += " + "
        balanced_equation += f"{coefficient}{molecule}"

    return balanced_equation


# Test the function
equation = "H2 + O2 -> H2O"
balanced_equation = balance_equation(equation)
print(balanced_equation)
