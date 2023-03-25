import sys
import python_lib

print("-------1-Ascending OR Descending---------"+"\r\n");
print("Note : Example for input List : 4 5 6 7");

arg = python_lib.get_input("What is your List ? ")
numbers = python_lib.get_list(arg)
print("your List is : " + str(numbers)+"\r\n");
res = python_lib.is_ascending(numbers)
print("Ascending :" + str(res));
res = python_lib.is_descending(numbers)
print("Descending :" + str(res)+"\r\n");

print("-------2-Riffle---------"+"\r\n");
print("Note : Example for input List : bob jack 42 48 ");
arg = python_lib.get_input("What is your List? ")
numbers = python_lib.get_list(arg , str)
print("your List is : " + str(numbers)+"\r\n");

ans = python_lib.get_input("The result be In shuffle? (Yes or No) ")
ans = ans.lower()
if ans == 'yes' :
	out = True
else :
	out = False
res = python_lib.riffle(numbers , out)
print("riffle :" + str(res)+"\r\n");

print("-------3-Only odd digits---------"+"\r\n");

nub = python_lib.get_input("Please enter number : ")
nub = int(nub)
print(python_lib.only_odd_digits(nub));
print("\r\n");

print("-------4-Three summers ago---------"+"\r\n");

goal = python_lib.get_input("What is your Goal? ")
arg = python_lib.get_input("What is your List? ")
numbers = python_lib.get_list(arg)
print(python_lib.three_summers(numbers , int(goal))); 
print("\r\n");


print("-------5-Count all sums and products---------"+"\r\n");

arg = python_lib.get_input("What is your List? ")
numbers = python_lib.get_list(arg)
print(python_lib.count_distinct_sums_and_products(numbers)); 
print("\r\n");


print("-------6- Group equal consecutive elements into sublists---------"+"\r\n");

arg = python_lib.get_input("What is your items list ? ")
itm = python_lib.get_list(arg , str)

print(python_lib.group_equal(itm));
print("\r\n");



print("-------7-Try a spatula---------"+"\r\n");

txt = python_lib.get_input("What is your text ? ")
txt = str(txt)
print(python_lib.pancake_scramble(txt)); 
print("\r\n");

print("-------8-First missing positive integer---------"+"\r\n");

arg = python_lib.get_input("What is your list ? ")
numbers = python_lib.get_list(arg)
print(python_lib.first_missing_positive(numbers)); 
print("\r\n");


print("-------9-Check your permutation---------"+"\r\n");

arg = python_lib.get_input("What is your list ? ")
numbers = python_lib.get_list(arg)
n = python_lib.get_input("What is your permutation ? ")

print(python_lib.is_permutation(numbers , n)); 
print("\r\n");

print("-------10-Tribonacci---------"+"\r\n");

num = python_lib.get_input("What is Number ? ")
start = python_lib.get_input("What is start value list? ")
start = python_lib.get_list(start)
print(python_lib.tribonacci(int(num) , start)); 
print("\r\n");

print("-------11-Keep doubling---------"+"\r\n");

arg = python_lib.get_input("What is your Number ? ")
givup = python_lib.get_input("What is giveup ? ")
print(python_lib.double_until_all_digits(int(arg) , int(givup))); 
print("\r\n");



print("-------12-Remove item after its k:th occurrence---------"+"\r\n");

arg = python_lib.get_input("What is List ? ")
numbers = python_lib.get_list(arg , str)
k = python_lib.get_input("What is k:th occurrence ? ")
print(python_lib.remove_after_kth(numbers , int(k))); 
print("\r\n");


	
print("-------13-And sometimes why--------"+"\r\n");

arg = python_lib.get_input("What is text ? ")
print(python_lib.disemvowel(str(arg))); 
print("\r\n");


print("-------14-Sort array by element frequency---------"+"\r\n");

arg = python_lib.get_input("What is elems List ? ")
numbers = python_lib.get_list(arg , str)
print(python_lib.frequency_sort(numbers)); 
print("\r\n");


print("-------15-What do you hear, what do you say?---------"+"\r\n");

dig = python_lib.get_input("What is digits? ")
print(python_lib.count_and_say(int(dig))); 
print("\r\n");

print("-------16-Giving back change---------"+"\r\n");

amount = python_lib.get_input("What is amount? ")
arg = python_lib.get_input("What is coins List? ")
coins = python_lib.get_list(arg)
print(python_lib.give_change(int(amount) , coins)); 
print("\r\n");


print("-------17-Sort integers by their digit counts---------"+"\r\n");
arg = python_lib.get_input("What is items List ? ")
ll = python_lib.get_list(arg)
print(python_lib.sort_by_digit_count(ll)); 
print("\r\n");


print("-------18-Scrabble value of a word---------"+"\r\n");

txt = python_lib.get_input("What is text? ")
arg = python_lib.get_input("What is multipliers list? ")
multipliers = python_lib.get_list(arg)
if not multipliers :
	multipliers = None
print(python_lib.scrabble_value(txt , multipliers)); 
print("\r\n");


print("-------19-Create zigzag array---------"+"\r\n");

rows = python_lib.get_input("What is rows? ")
cols = python_lib.get_input("What is cols ? ")
print(python_lib.create_zigzag(int(rows) ,int(cols))); 
print("\r\n");


print("-------20-All cyclic shifts---------"+"\r\n");

txt = python_lib.get_input("What is text? ")
print(python_lib.all_cyclic_shifts(txt)); 
print("\r\n");


print("-------21-Postfix interpreter---------"+"\r\n");
print("ex : 3 3 3 / - ");

arg = python_lib.get_input("What is items list? ")
itm = python_lib.get_list(arg , str)

print(python_lib.postfix_evaluate(itm)); 
print("\r\n");

print("------22-Count consecutive summers---------"+"\r\n");

arg = python_lib.get_input("What is number? ")

print(python_lib.count_consecutive_summers(int(arg))); 
print("\r\n");

print("------23-Running median of three---------"+"\r\n");

arg = python_lib.get_input("What is items list? ")
itm = python_lib.get_list(arg)

print(python_lib.running_median_of_three(itm)); 
print("\r\n");

print("------24-Reverse every ascending sublist--------"+"\r\n");

arg = python_lib.get_input("What is items list? ")
itm = python_lib.get_list(arg)

print(python_lib.reverse_ascending_sublists(itm)); 
print("\r\n");


print("------25-Longest palindrome substring-------"+"\r\n");

arg = python_lib.get_input("What is text? ")

print(python_lib.longest_palindrome(arg)); 
print("\r\n");


print("------26-Iterated removal of consecutive pairs-------"+"\r\n");

arg = python_lib.get_input("What is items list? ")
itm = python_lib.get_list(arg , str)

print(python_lib.iterated_remove_pairs(itm)); 
print("\r\n");


print("------27-Brangelina-------"+"\r\n");

f = python_lib.get_input("What is first name? ")
s = python_lib.get_input("What is second name? ")

print(python_lib.brangelina(f , s)); 
print("\r\n");


print("------28-Collapse positive integer intervals-------"+"\r\n");

arg = python_lib.get_input("What is items list? ")
itm = python_lib.get_list(arg )

print(python_lib.collapse_intervals(itm)); 
print("\r\n");



print("------29-Fulcrum------"+"\r\n");
arg = python_lib.get_input("What is items list? ")
itm = python_lib.get_list(arg)
print(python_lib.can_balance(itm)); 
print("\r\n");



print("------30-Expand positive integer intervals------"+"\r\n");
print("Ex : 1,3-9,12-14,9999 ");

txt = python_lib.get_input("What is intervals? ")

print(python_lib.expand_intervals(txt)); 
print("\r\n");

