from functions import salary,hello_who

assert hello_who('Max')=='Hello,Max', 'Helllo who error'
assert hello_who('Leo')=='Hello,Leo', 'Hello who error'
assert hello_who('Nikita')=='Hello,Nikita','Hello who error'
assert salary(2, 1)==4
assert salary(2, 2)==8