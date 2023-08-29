from stack import Stack
open_element= ["[","{","("]
close_element = ["]","}",")"]


def balance_elements(elements):
    s = Stack(len(elements))
    if  elements[0] in close_element or len(elements)%2 != 0:
        print("Баланс напрочь отсутствует")
    else:
        for i in elements:
            if i in open_element:
                s.push(i)
            elif i in close_element:
                pos = close_element.index(i)
                if open_element[pos] == s.peek():
                    s.pop()
            else:
                print("Баланс напрочь отсутствует")
        if s.isEmpty():
            print("Есть баланс")
        else:
            print("Баланс напрочь отсутствует")

if __name__ == '__main__':
    elements = '(((([{}]))))'
    balance_elements(elements)

    elements1 = '[[{())}]'
    balance_elements(elements1)



