# OPERAÇÕES
# as operações podem ser feitas utilizando "+, -, *, /, **, // e %"
# ** = exponenciação     // = quociente     % = sobra da divisão

# TEXTO
# para gerar texto pode-se usar  'texto' ou "texto"
# o texto gerado é chamado de string
# quando precisa usar apostrofo ou citaçao dentro da string, usa-se a barra invertida "\" antes para evitar
# que a string acabe

# para gerar novas linhas dentro da string, usa-se "\n"
# pode-se gerar novas linhas colocando 3 citações ao inves de 1 e dando ctrl + enter para gerar as linhas
# para dar a funçao de tab na string, usa-se "\t"
# para concatenar duas ou mais strings, usa-se o "+" entre elas
# é possível multiplicar as strings usando "*" antes ou após ela, geralmente a string vem antes

# VARIAVEIS
# servem para atribuir uma qualidade a um nome, ex: idade, nome, cor o que vc quiser
# os nomes so podem conter letras, numeros e underlines e nao podem começar com numeros
# tendo a variavel feita, ela pode ser usada com o print pois tera um valor/atributo atribuido a ela
# a variavel pode ser mudada quantas vezes quiser, nao é fixa

# o input abre uma string para o usuario responder. a resposta (string) sera associada a um nome. pode-se entao
# printar o nome e sairá a resposta do usuário. é possivel associar essa resposta a uma string, gerando uma frase
# caso o input seja um numero, é possivel converte-lo de string para numero usando "int" antes do "input"
# para converter um numero para string, usa-se "str". é necessario para concatenar strings, pois nao e possivel
# concatenar strings e numeros
# para transformar o numero em float, usa-se "float()"
# pode-se usar varios inputs numa string

# IN-PLACE OPERATORS
# usa-se para realizar funções como "x = x-3" de forma mais simples, como "x -=3". mas primeiro deve-se atribuir
# um valor/atributo a x
# pode-se usar com "-, +, *, /, %, **, //"

# BOOLEANS
# Existem dois values de Boolean : True ou False
# Eles podem ser criados comparando values, por exemplo, utilizando o operador de igual '=='
# print(2==3) dará um value False por exemplo
# Outro operador de comparaçao é o operador not equal '!='
# Ele dará True se o valor for diferente e False se for igual
# por exemplo print(1 != 1) resultará em False
# Comparison operators are also called Relational operators

# Python also has operators that determine whether one number (float or integer);
# is greater than or smaller than another. These operators are '>' and '<' respectively
# The greater than or equal to, and smaller than or equal to operators are '>=' and '<='

# Greater than and smaller than operators can also be used to compare strings lexicographically;
# (the alphabetical order of words is based on the alphabetical order of their component letters)

# if Statements

# You can use if statements to run code if a certain condition holds
# If an expression evaluates to True, some statements are carried out. Otherwise, they aren't carried out.
# an if statement looks like this:
if expression: "if 10>5:"
   statements  "print(10 is greater than 5)"

# Python uses indentation (white space at the beginning of a line) to delimit blocks of code
# To perform more complex checks, if statements can be nested, one inside the other
# This means that the inner if statement is the statement part of the outer one

# else Statement

# The if statement allows you to check a condition and run some statements, if the condition is True
# The else statement can be used to run some statements when the condition of the if statement is False
# Every if condition block can have only one else statement
# In order to make multiple checks, you can chain if and else statements
if expression: "if x==5:"
    statements "print('yes')"
else:
    statements "print('no')"

# elif Statements

# The elif (short for else if) statement is a shortcut to use when chaining if and else statements
# exemplo num=3
if num == 1:
    print('one')
elif num == 2:
    print('two')
elif num==3:
    print('three')
else:
    print('something else')
# As you can see in the example above, a series of if elif statements can have a final else block;
# which is called if none of the if or elif expressions is True
# fazer isso evita indentações em excesso

# Boolean logic

# Boolean logic is used to make more complicated conditions for if statements that rely on more than one condition
# Python's Boolean operators are and, or, and not

# Boolean "and"
# The and operator takes two arguments, and evaluates as True if, and only if, both of its arguments are True;
# Otherwise, it evaluates to False.
# ex: print(1==1 and 2==2) -> True / print(1==1 and 2==3) -> False
# Boolean operators can be used in expression as many times as needed.

# Boolean "or"
# The or operator also takes two arguments. It evaluates to True if either (or both) of its arguments are True,
# and False if both arguments are False
# ex: print(1==1 or 2==2) -> True / print(1==1 or 2==1) -> True / print(1==2 or 2==3) -> False
# Besides values, you can also compare variables.

# Boolean "not"
# Unlike other operators we've seen so far, not only takes one argument, and inverts it.
# The result of not True is False, and not False goes to True
# ex: print(not 1==1) -> False / print(not 1>7) -> True
# You can chain multiple conditional statements in an if statement using the Boolean operators.

# Operator precedence

# Operator precedence is a very important concept in programming. It is an extension of the mathematical
# idea of order of operations (multiplication being performed before addition, etc.) to include other operators,
# such as those in Boolean logic.
# The below code shows that == has a higher precedence than or
# ex: print(False == False or True) -> True / print(False == (False or True)) -> False /
# print((False==False)or True) -> True

# Chaining multiple conditions

# You can chain multiple conditional statements in an if statement using the Boolean operators.
# For example, we can check if the value of a grade is between 70 and 100:
grade = 88
if (grade>= 70 and grade <= 100):
    print('Passed!')
# You can use multiple and, or, not operators to chain multiple conditions together.

# Lists

# Lists are used to store items.
# A list is created using square brackets with commas separating items.
# ex: words = ["Hello", "world", "!"]
# In the example above the words list contains three string items.
# A certain item in the list can be accessed by using its index in square brackets.
# print(words[0]) -> Hello
# The first list item's index is 0, rather than 1, as might be expected.

# Sometimes you need to create an empty list and populate it later during the program.
# For example, if you are creating a queue management program, the queue is going to be empty in the beginning
# and get populated with people data later.
# An empty list is created with an empty pair of square brackets.
# ex: empty_list = []
#     print(empty_list)

# Typically a list will contain items of a single item type, but it is also possible to include several different types
# Lists can also be nested within other lists.
# ex:
things = ['string', 0, [1,2], 4.56]
# Nested lists can be used to represent 2D grids, such as matrices.
# A matrix-like structure can be used in cases where you need to store data in row-column format
# ex:
 m = [
     [1,2,3],
     [4,5,6]
     ]

# Some types, such as strings, can be indexed like lists.
# Indexing strings behaves as though you are indexing a list containing each character in the string.
# ex:
str = "Hello world"
print(str[6])  -> o resultado será o sétimo caractere = "w"
# Space (" ") is also a symbol and has an index / espaço conta como caractere

# List Operations

# The item at a certain index in a list can be reassigned.
# ex:
nums = [7,7,7,7,7]
nums[2]=5
print(nums)   -> "[7,7,5,7,7]"
# You can replace the item with an item of a different type.

# Lists can be added and multiplied in the same way as strings.
# ex:
nums = [1,2,3]
print(nums + [4,5,6])  -> "[1,2,3,4,5,6]"
print(nums*3)  -> "[1,2,3,1,2,3,1,2,3]"

# Lists and strings are similar in many ways - strings can be thought of as lists of characters that can't be changed
# For example, the string "Hello" can be thought of as a list, where each character is an item in the list;
# The first item is "H", the second item is "e", and so on.

# To check if an item is in a list, the "in" operator can be used.
# It returns True if the item occurs one or more times in the list, and False if it doesn't.
# ex:
words = ["spam", "eggs", "spam", "sausage"]
print("spam" in words)   -> "True"
print("eggs" in words)    -> "True"
print("tomato" in words) -> "False"
# The in operator is also used to determine whether or not a string is a substring of another string.

# To check if an item is not in a list, you can use the not operator in one of the following ways:
nums = [1, 2, 3]
print(not 4 in nums) -> 'True'
print(4 not in nums) -> 'True'
print(not 3 in nums) -> 'False'
print(3 not in nums) -> 'False'

# List Functions

# The append method adds an item to the end of an existing list.
# ex:
nums = [1, 2, 3]
nums.append(4)
print(nums) -> '[1,2,3,4]'
# The dot before append is there because it is a method of the list class

# To get the number of items in a list, you can use the len function.
nums = [1,3,5,2,4]
print(len(nums)) -> 5
# Unlike the index of the items, len does not start with 0;
# So, the list above contains 5 items, meaning len will return 5.
# len is written before the list it is being called on, without a dot.

# The insert method is similar to append, except that it allows you to insert a new item at any
# position in the list as opposed to just at the end.
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)
# Elements, that are after the inserted item, are shifted to the right.

# The index method finds the first occurrence of a list item and returns its index.
# If the item isn't in the list, it raises a ValueError.
letters = ['p','q','r','s','p','u']
print(letters.index('r')) -> 2
print(letters.index('p')) -> 0
print(letters.index('z')) -> ValueError

# There are a few more useful functions and methods for lists.
# max(list): Returns the list item with the maximum value
max(letters) -> u
# min(list): Returns the list item with minimum value
min(letters) -> p
# list.count(item): Returns a count of how many times an item occurs in a list
letters.count('u') -> 1
# list.remove(item): Removes an object from a list
letters.remove('q') -> letters = ['p','r','s','p','u']
# list.reverse(): Reverses items in a list.
letters.reverse() -> letters = ['u','p','s','r','p']

# while Loops

# A while loop is used to repeat a block of code multiple times.
# For example, let's say we need to process multiple user inputs, so that each time the user inputs something;
# the same block of code needs to execute.
# Below is a while loop containing a variable that counts up from 1 to 5, at which point the loop terminates.
i = 1
while i <= 5:
    print(i)
    i = i + 1

print('Finished')
# The code in the body of a while loop is executed repeatedly. This is called iteration.
# During each loop iteration, the i variable will get incremented by one, until it reaches 5.
# So, the loop will execute the print statement 5 times.