import sys

def get_input(q):
	if(sys.version_info > (3, 0)) :
		arg = input(q)
	else :
		arg = raw_input(q)
	return arg;

def get_list(arg , type = int):
	if(sys.version_info > (3, 0)) :
		numbers = list(map(type, arg.split()))
	else :
		numbers = map(type, arg.split())
	return numbers;

		
def is_ascending(lst):
    ascending = True
    for i in range(len(lst) - 1): 
        if lst[i] >= lst[i+1] :
            ascending = False
    return ascending
	

def is_descending(lst):
    descending = True
    for i in range(len(lst) - 1): 
        if lst[i] <= lst[i+1] :
            descending = False
    return descending

def interleave(lst1, lst2):
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    return lst1[0:1] + interleave(lst2, lst1[1:])
	

def riffle(lst, out = False):
	ln = len(lst)
	ln = int(ln)
	if ln % 2 == 0 :
		if out == True :
			lst1 = lst[:ln//2]
			lst2 = lst[ln//2:]
		else : 
			lst1 = lst[ln//2:]
			lst2 = lst[:ln//2]

		return interleave(lst1, lst2)
	else :
		return "Your list must have even  length"


def Division(n):
	return n//10;
	
def remainig(n):
	return n%10;

def only_odd_digits(n):
	i = 1
	isodd = True
	while i!=0 :
		x = remainig(n);
		if x % 2 == 0:
			isodd = False
			i = 0
		else :
			n = Division(n);
			if n == 0:
				i = 0
	return isodd;
	


def three_summers(items, goal):
	items.sort()
	if len(items) < 3 :
		return "Min length three items"
	elif len(items) == 3 :
		x = sum(items)
		if x == goal:
			return True;
		else:
			return False;
	else :
		i = 0
		j = 1
		res = False
		while j < len(items):
			
			x = items[i] + items[j]
		
			for r in range(len(items)):
				
				if r == i : continue
				if r == j : continue
				
				sm = x + items[r]
				
				if sm == goal:
					res = True
					j = len(items)
				else:
					i +=1
					j +=1
		return res;


def count_distinct_sums_and_products(items):
	items.sort()
	i = 0
	j=0
	allres = []
	for x in range(len(items)):
		for i in range(len(items)):
			allres.append(items[x]+items[i])
			allres.append(items[x]*items[i])
		i +=1
		
	result = sorted(set(allres));		
	return 	len(result)


def group_equal(items):
	master_list = []
	section = []

	if len(items) == 1:
		return [items]

	for i, item in enumerate(items):
		if i == 0:
			section.append(item)
			continue

		if item == section[0]:
			section.append(item)

		else:
			master_list.append(section)
			section = [item]

		if i == len(items) - 1:
			master_list.append(section)
	
	return master_list


def pancake_scramble(text):
	words = list(text)
	cnt = len(words)
	j = 1
	i = 1
	while j < cnt :
		newword = ''
		z = j
		k = j+1
		for z in reversed(range(k)) :
			newword += words[z]
		for q in range(cnt):
			if q<k :
				continue
			newword += words[q]
		j +=1
		words = list(newword)
	return newword
		


def first_missing_positive(items):
	items.sort()
	for i in range(len(items)):
		existval = int(items[i])
		chval = existval + 1
		if chval not in items:
			return chval


def is_permutation(items, n):
	
	result = sorted(set(items));
	x = 1
	for i in range(len(items)):
		if x not in items:
			return False
		x +=1
	return True
	


def tribonacci(n, start):
	if n >2 :
		j =3
		while j < n+1 :
			
			sum = start[0] + start[1] + start[2]
			start = [start[1], start[2] , sum]
			j +=1
			
	else:
		return start[n]
	return start[2]
	

def double_until_all_digits(n, giveup = 1000):
	i = 0
	while i < giveup:
		if len(set(str(n))) == 10:
			return i
		n *= 2
		i += 1
	return -1
	


def remove_after_kth(items, k = 1):
	result = []
	if k == 0 :
		return result;
		
	for i in items:
		q = 1
		for j in result:
			if i == j :
				q +=1
		if q <= k :
			result.append(i)
	return result
		


def disemvowel(text):
	text = text.lower()
	txtlist = text.split(" ")
	vowels = ['a','e','i','o','u']
	for i in range(len(txtlist)):
		charlist = list(str(txtlist[i]))
		newstr =''
		for j in range(len(charlist)) :
			char = str(charlist[j])
			if j > 0 :
				pchar = str(charlist[j-1])
				if char == 'y' and pchar not in vowels :
					newstr += char
			if char not in vowels and char != 'y':
				newstr += char
		txtlist[i] = newstr
	return ' '.join(txtlist)

def frequency_sort(elems):
	d = {}
	ordered = sorted(elems)
	for elem in elems:
		d.setdefault(elem, 0)
		d[elem] += 1
	return sorted(ordered, key=lambda x: d[x], reverse=True)


def count_and_say(digits):
	diglist = [int(i) for i in str(digits)]
	t = len(diglist)
	c = 0
	newval = ''
	for i in range(t):
		if i!=0:
			if diglist[i] == diglist[i-1]:
				c += 1
			else:
				newval += str(c)+str(diglist[i-1])
				c = 1
		else:
			c +=1
	return newval+str(c)+str(diglist[i])
	

def give_change(amount, coins):
	coins.sort(reverse = True) 
	current_coin = 0
	change = []

	while sum(change) != amount:
		change.append(coins[current_coin])
		if sum(change) > amount:
			change.pop(-1)
			current_coin += 1
	return change



def sort_by_digit_count(items):
	import functools

	def is_larger_digit(item1, item2):
		item1_dict = {i: 0 for i in range(0, 10)}
		item2_dict = {i: 0 for i in range(0, 10)}

		for i in str(item1):
			item1_dict[int(i)] += 1

		for i in str(item2):
			item2_dict[int(i)] += 1

		for n in range(9, 0, -1):
			if item1_dict[n] > item2_dict[n]:
				return 1
			elif item2_dict[n] > item1_dict[n]:
				return -1

		if item1 > item2:
			return 1
		else:
			return -1

	return sorted(items, key=functools.cmp_to_key(is_larger_digit))

def scrabble_value(word, multipliers = None):
	scrabble_dict = {"a":1, "b":3, "c":3, "d":2, "e":1, "f":4, "g":2, "h":4, "i":1, "j":8, "k":5, "l":1, "m":3, 
					 "n":1, "o":1, "p":3, "q":10, "r":1, "s":1, "t":1, "u":1, "v":4, "w":4, "x":8, "y":4, "z":10}
	
	value = 0
	b = 0
	for i, letter in enumerate(word):
		if multipliers is None :
			b =1
		else:
			b = multipliers[i]
		value  = value + scrabble_dict.get(letter) * b

	return value



def create_zigzag(rows, cols, start = 1):
	zigzag = [[start + col + row * cols for col in range(cols)] for row in range(rows)]

	for i in range(len(zigzag)):
		if i % 2 != 0:
			zigzag[i] = zigzag[i][::-1]

	return zigzag


def all_cyclic_shifts(text):
	cyclic_shifts = [text]
	for _ in range(len(text)-1):
		text = text[1:] + text[0]
		if text not in cyclic_shifts:
			cyclic_shifts.append(text)
	return sorted(cyclic_shifts)


def postfix_evaluate(items):
	i = 0
	while True:
		if items[i] in ('*', '+', '-', '/'):

			operator = items.pop(i)
			num2 = items.pop(i - 1)
			num2 = int(num2)
			num1 = items.pop(i - 2)
			num1 = int(num1)

			if operator == '+':
				answer = num1 + num2
			elif operator == '-':
				answer = num1 - num2
			elif operator == '*':
				answer = num1 * num2
			else:
				if num2 == 0:
					answer = 0
				else:
					answer = num1 // num2
			
			items.insert(i-2, answer)
			i = -1

			if len(items) == 1:
				return items[0]

		i += 1

def count_consecutive_summers(n):
	count = 1
	for i in range(1, n):

		summ = i

		while summ < n:
			i += 1
			summ += i
			if summ == n:
				count += 1
				break
			if summ > n:
				break
	return count

def running_median_of_three(items):
	return_list = items[:2]

	if len(items) < 2:
		return return_list

	for i in range(len(items) - 2):
		mini_list = [items[n] for n in range(i, i+3)]
		mini_list.remove(max(mini_list))
		mini_list.remove(min(mini_list))
		return_list.append(mini_list[0])

	return return_list

def reverse_ascending_sublists(items):
	
	sublists = []
	sublist = [items[0]]

	for item in items[1:]:
		if sublist[-1] < item:
			sublist.append(item)
		else:
			sublists.append(sublist)
			sublist = [item]

	sublists.append(sublist)

	return [n for i in list(map(reversed, sublists)) for n in i]

def longest_palindrome(text):
	longest = ''
	
	for end in range(len(text), -1, -1):
		for start in range(0, end):
			section = text[start:end+1]
			
			if section == section[::-1] and len(section) >= len(longest):
				longest = section

	return longest

def iterated_remove_pairs(items):
	while True:
		changed = False
		for i in range(len(items) - 1):
			
			if items[i] == items[i + 1]:
				items.pop(i+1)
				items.pop(i)
				changed = True
				break

		if not changed:
			return items


def words_with_given_shape(words, shape):
	matches = []
	for word in words:
		sh = []
		for i in range(len(word) - 1):
			if ord(word[i]) < ord(word[i + 1]):
				sh.append(1)
			elif ord(word[i]) == ord(word[i + 1]):
				sh.append(0)
			else:
				sh.append(-1)
		if sh == shape:
			matches.append(word)
	return matches

def collapse_intervals(items):
	output = ''
	sublists = []

	if len(items) == 0:
		return ''

	if len(items) == 1:
		return str(items[0])

	current = [items[0]]

	for i in range(1, len(items)):

		if current[-1] + 1 == items[i]:
			current.append(items[i])

		else:
			sublists.append(current)
			current = [items[i]]

	sublists.append(current)

	for i in range(len(sublists)):

		if len(sublists[i]) == 1:
			output += str(sublists[i][0])

		else:
			output += str(sublists[i][0]) + '-' + str(sublists[i][-1])

		if i != len(sublists) - 1:
			output += ','

	return output


def expand_intervals(intervals):

	intervals = intervals.split(',')
	
	master = []

	for interval in intervals:
		try:
			lower, higher = map(int, interval.split('-'))
			master +=  [n for n in range(lower, higher + 1)]
		
		except:
			master += [int(interval)]

	return master
	
def can_balance(items):
	for index in range(len(items)):
		
		sumLeft = 0
		sumRight = 0
		
		for n, i in enumerate(items):
			if n < index:
				sumLeft += i * (index - n)

			if n > index:
				sumRight += i * (n - index)

		if sumLeft == sumRight:
			return index
	return -1
	
def brangelina(first, second):
	import re

	pattern = re.compile(r'[aeiou]+')

	first_vowel_group = [match.regs[0] for match in pattern.finditer(first)]

	if len(first_vowel_group) == 1:
		pos = first_vowel_group[0][1] - 1
		first = first[:pos]

	else:
		pos = first_vowel_group[-2][1] - 1
		first = first[:pos]

	while second[0] not in ('a', 'e', 'i', 'o', 'u'):
		second = second[1:]
	
	return first + second
