import os

def preparedMakeFile():
	# Read the Makefile 
	f = open('submittion/Makefile', 'r')
	lines = f.readlines()
	f.close()
	# Replace the line Makefile 'INCLUDES = includes/' by libft.h
	f = open('submittion/Makefile', 'w')
	for i in range(len(lines)):
		if lines[i].startswith('INCLUDES'):
			lines[i] = 'INCLUDES = .\n'
	f.writelines(lines)
	f.close()
	print('Makefile is ready')

def main():
	os.system('rm -rf submittion')
	git_repo = raw_input('Enter the git repository: ')
	# Check if the folder 'submittion' exists
	if not os.path.exists('submittion'):
		os.makedirs('submittion')


	# Copy all files in the folder 'src' to the folder 'submittion'
	for file in os.listdir('src'):
		os.system('cp src/' + file + ' submittion/' + file)
	
	# Copy all files in the folder 'includes' to the folder 'submittion'
	for file in os.listdir('includes'):
		os.system('cp includes/' + file + ' submittion/' + file)
	
	os.system('cp Makefile submittion/Makefile')
	preparedMakeFile()
	os.system('cp UpdateMakeFile.py submittion/UpdateMakeFile.py')
	os.system('cp Header.py submittion/Header.py')
	os.system('cd submittion && python UpdateMakeFile.py && rm UpdateMakeFile.py')
	os.system('cd submittion && python3 Header.py && rm Header.py')
	os.system('cd submittion && /Users/ekarpawi/francinette/tester.sh')
	you_fine = raw_input('Are you fine with the result? (y/n) ')
	if you_fine != "y":
		os.system('rm -rf submittion')
		exit()
	os.system('cd submittion && git init && git add . && git commit -m "submit" && git remote add origin ' + git_repo + ' && git push -f origin master')

if __name__ == '__main__':
	main()