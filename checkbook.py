import csv
		
def balance():
	with open('ledger.csv', 'r') as csv_file:
		reader = csv.DictReader(csv_file)
		total = sum(float(row['amount']) for row in reader)
	return total	

def pad_col(col, max_width):
	return col.ljust(max_width)

def welcome():
	print('\n-----Welcome to your terminal checkbook!-----\n')

	print('What would you like to do?\n')

	print('''1. view current balance \n2. record a debit (withdrawal) \n3. record a credit (deposit) \n4. view all transactions \n5. exit \n''')

	print('Your choice?' )
	x = input()
	
	if x == '1':
		print(f'\nYour current balance is {balance()}\n')
		welcome()	
	
	elif x == '2':
		print('How much is the debit?')
		amount = input()
		amount = float(amount)
		print('what was the date of the transaction? Please enter as MM-DD-YYYY')
		transdate = input()
		print('Enter a description for this transaction: ')
		desc = input()
		def debit(amount, transdate, desc):
			with open('ledger.csv', 'a', newline='') as csvfile:
				fieldnames = ['transaction', 'date', 'type', 'desc', 'amount']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				rowcount  = 0

				for row in open('ledger.csv'):
  					rowcount+= 1
			
				#writer.writeheader()
				writer.writerow({'transaction': rowcount, 'date': transdate, 'type':'debit', 'desc':desc, 'amount':(-amount)})
		debit(amount, transdate, desc)	
		print('\nYour transaction has been recorded.\n')
		welcome()
	
	elif x == '3':
		print('How much is the deposit?')
		amount = input()
		amount = float(amount)
		print('What was the date of the transaction? Please enter as MM-DD-YYYY')
		transdate = input()
		print('Enter a description for this transaction: ')
		desc = input()
		def credit(amount, transdate, desc):
			with open('ledger.csv', 'a', newline='') as csvfile:
				fieldnames = ['transaction', 'date', 'type', 'desc', 'amount']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				rowcount  = 0
				for row in open('ledger.csv'):
  					rowcount+= 1
				#writer.writeheader()
				writer.writerow({'transaction':rowcount, 'date': transdate, 'type':'credit', 'desc':desc, 'amount':amount})
		credit(amount, transdate, desc)
		print('\nYour transaction has been recorded.\n')
		welcome()
	
	elif x =='4':
		with open('ledger.csv') as csvfile:
			reader = csv.reader(csvfile)
			all_rows = []
			for row in reader:
				all_rows.append(row)

		max_col_width = [0] * len(all_rows[0])
		for row in all_rows:
			for idx, col in enumerate(row):
				max_col_width[idx] = max(len(col), max_col_width[idx])

		for row in all_rows:
			to_print = ""
			for idx, col in enumerate(row):
				to_print += pad_col(col, max_col_width[idx]) + " | "
			print("-"*len(to_print))
			print(to_print)
		welcome()
	
	elif x == '5':
		print('Thank you, have a nice day!\n')
		exit
		
	else:
		print(f'Invalid choice: {x}\n')
		
		welcome()

welcome()