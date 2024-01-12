# 연습문제 - 중위 표기법 --> 후위 표기법
from stack import ArrayStack as Stack

def splitTokens(exprStr):
	tokens = []
	val = 0
	valProcessing = False
	for c in exprStr:
		if c == ' ':
			continue
		if c in '0123456789':
			val = val * 10 + int(c)
			valProcessing = True
		else:
			if valProcessing:
				tokens.append(val)
				val = 0
			valProcessing = False
			tokens.append(c)
	if valProcessing:
		tokens.append(val)

	return tokens

def infixToPostfix(tokenList):
	prec = {
		'*': 3,
		'/': 3,
		'+': 2,
		'-': 2,
		'(': 1,
	}

	opStack = Stack() # 연산자를 담아둘 스택
	postfixList = [] # 최종 반환할 후위 표기법 리스트
	
	for token in tokenList:
		if type(token) is int: # 토큰이 피연산자라면 리스트에 넣는다
			postfixList.append(token)
		elif token == '(': # 토큰이 여는 괄호라면 스택에 넣는다
			opStack.push(token)
		elif token == ')': # 토큰이 닫는 괄호라면 그동안 쌓인 연산자를 스택에 넣는다
			while opStack.peek() != '(':
				postfixList.append(opStack.pop())
			opStack.pop() # 닫는 괄호를 지운다
		else: # 토큰이 연산자라면 스택에 넣되, 우선순위를 고려한다
			if opStack.isEmpty(): # 스택이 비어있다면 스택에 넣는다
				opStack.push(token)
			else: # 스택에 연산자가 있고, 토큰보다 우선순위가 높다면(prec 값이 크다면) 리스트에 pop한다
				while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
					postfixList.append(opStack.pop())
				opStack.push(token)
			
	while not opStack.isEmpty(): # 남은 연산자를 모두 리스트에 넣는다
		postfixList.append(opStack.pop())
	
	return postfixList

def postfixEval(tokenList):
	valStack = Stack()

	for token in tokenList:
		if type(token) is int: # 피연산자라면 스택에 push
			valStack.push(token)
		elif token == '*': # +, * 연산자는 순서 상관없음
			second = valStack.pop()
			first = valStack.pop()
			valStack.push(first * second)
		elif token == '/': # -, / 연산자는 순서 상관있음
			second = valStack.pop()
			first = valStack.pop()
			valStack.push(first / second)
		elif token == '+':
			second = valStack.pop()
			first = valStack.pop()
			valStack.push(first + second)
		elif token == '-':
			second = valStack.pop()
			first = valStack.pop()
			valStack.push(first - second)

	return valStack.pop()

def solution(expr):
	tokens = splitTokens(expr)
	postfix = infixToPostfix(tokens)
	val = postfixEval(postfix)
	return val