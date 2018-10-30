def get_input(msg, options=None):
	if options:
		while True:
			user_input = input(msg + ' Options: ' +  ','.join(options) + '\n>> ')
			options = list(map(lambda opt: opt.lower(), options))
			if user_input.lower() in options:
				return user_input.lower()
			else:
				print('Opção inválida!')
	else:
		return input(msg + '\n>> ')


def print_board(board):
	print('\n'*100)
	print('\t\t    Tic Tac Toe em Python\n\n')
	print('\t\t\t ' + board[1] + ' | ' + board[2]  + ' | ' + board[3])
	print('\t\t\t-----------')
	print('\t\t\t ' + board[4] + ' | ' + board[5]  + ' | ' + board[6])
	print('\t\t\t-----------')
	print('\t\t\t ' + board[7] + ' | ' + board[8]  + ' | ' + board[9])
	print('\n'*10)

def validate(user_input, board):
	if user_input not in '123456789' or len(user_input) <= 0:
		print(f'Inputted value "{user_input}" is invalid!')
		return False

	if int(user_input) < 0 or int(user_input) > 9:
		print(f'Inputted value "{user_input}" is out of range!')
		return False

	if board[int(user_input)] != ' ':
		print(f'Place number {user_input} is not available!')
		return False

	return True

def is_final_state(board):
	result = (False, board[0])
	if board[1] == board[2] == board[3] != ' ':
		return (True, board[0])
	if board[4] == board[5] == board[6] != ' ':
		return (True, board[0])
	if board[7] == board[8] == board[9] != ' ':
		return (True, board[0])
	if board[1] == board[4] == board[7] != ' ':
		return (True, board[0])
	if board[2] == board[5] == board[8] != ' ':
		return (True, board[0])
	if board[3] == board[6] == board[9] != ' ':
		return (True, board[0])
	if board[1] == board[5] == board[9] != ' ':
		return (True, board[0])
	if board[3] == board[5] == board[7] != ' ':
		return (True, board[0])
	return (False, board[0])


p1_name = 'Player One'
p2_name = 'Player Two'
p1_marker = 'X'
p2_marker = 'O'
p_turn = 'p1'
p_turn_name = ''
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
user_input = ''

while True:
	p1_name = get_input('Player one, what is your name?')
	p1_marker = get_input(f'{p1_name}: Would you like to play with X or O ?', ['X', 'Y']).upper()
	p2_name = get_input('Player two, what is your name?')
	if(p1_marker == 'X'):
		p2_marker = 'O'
	else:
		p2_marker = 'X'

	print(f'>> {p1_name}, you will play with: {p1_marker}!')
	print(f'>> {p2_name}, you will play with: {p2_marker}!')
	print('>> Press a number from 1 to 9 to place your marker on the board!\n\n')
	print_board(board)

	while True:
		if p_turn == 'p1':
			p_turn_name = p1_name
			board[0] = p1_marker
		else: 
			p_turn_name = p2_name
			board[0] = p2_marker

		user_input = get_input(f"{p_turn_name}, it's your turn: \n>> ")
		if validate(user_input, board):
			board[int(user_input)] = board[0]
			print_board(board)
			ended, winner = is_final_state(board)

			if ended:
				if winner == p1_marker:
					winner = p1_name
				else:
					winner = p2_name

				print(f'The end! {winner} won the game!')
				break
			else:
				if p_turn == 'p1':
					p_turn = 'p2'
				else:
					p_turn = 'p1'

	play_again = get_input('Would you like to play again? Y or N\n>> ', ['Y', 'N']).upper()
