from os import system

system("cls")
cant_de_var = 0
minterms = []


def prime_to_function(prime_terms):
    f = ""
    for term in prime_terms:
        c = 0
        for i in term:
            match i:
                case "0":
                    f += f"{chr(65 + c)}'"
                case "1":
                    f += f"{chr(65 + c)}"
                case "X":
                    pass
            c += 1
        if prime_terms.index(term) != len(prime_terms) - 1:
            f += " + "
    return f


def simplify_prime_terms(prime_terms, minterms):
    simplified_terms = {}

    for minterm in minterms:
        simplified_terms[minterm] = []

    for minterm in minterms:
        for prime_term in prime_terms:
            n = 0
            term = ""
            for char in prime_term:
                if char == "X":
                    term += minterm[n]
                else:
                    term += char
                n += 1
            if "X" not in term and term == minterm:
                simplified_terms[minterm].append(prime_term)

    for minterm in minterms:
        if len(simplified_terms[minterm]) == 1:
            index = prime_terms.index(simplified_terms[minterm])
            prime_terms.pop(index)

    return prime_terms



def input_minterms():
    n = int(input("Cuántos mintérminos tienes?"))
    for i in range(n):
        minterms.append(input(f"Introduce el mintérmino No. {i}\n>"))


def simplify(terms):
    simplified_terms = []
    for term1, term2 in terms:
        implicant = ""
        current_char = 0
        for char1 in term1:
            if char1 == term2[current_char]:
                implicant += char1
            else:
                implicant += "X"
            current_char += 1
        if implicant not in simplified_terms:
            simplified_terms.append(implicant)
    return simplified_terms


def combine(minterms):
    res = []
    for minterm in minterms:
        for term in minterms:
            n = 0  # Character
            c = 0  # Number of changes
            for char in term:
                if char is not minterm[n]:
                    c += 1  # Add 1 to the change count
                n += 1  # Current character
            if c == 1:
                res.append((term, minterm))
    return res


def get_prime_tenms(new_terms, original_terms):
    new_terms = set([i[0] for i in new_terms])
    prime_terms = []
    for i in original_terms:
        if i not in new_terms and i not in prime_terms:
            prime_terms.append(i)
    return prime_terms


if __name__ == '__main__':
    input_minterms()
    combinedterms = combine(minterms)
    prime_terms = get_prime_tenms(combinedterms, minterms)
    implicants = simplify(combinedterms)

    while combinedterms:
        combinedterms = combine(implicants)
        prime_terms += get_prime_tenms(combinedterms, implicants)
        implicants = simplify(combinedterms)
        print(f"Combined Terms: {combinedterms}")
        print(f"Prime Terms: {prime_terms}")
        print(f"Implicants: {implicants}")

    print(f"F = {prime_to_function(prime_terms)}")

    simplified_function = prime_to_function(simplify_prime_terms(prime_terms, minterms))
    print(f"Simplified Terms: {simplified_function}")