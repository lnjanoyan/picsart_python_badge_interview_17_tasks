!!!!!While using these solutions don't forget to check file path!!!!!!!!

Here are tasks 

1)	Crossword cheater: When working on a crossword puzzle, often you will have a word where you know several of the letters, but not all of them. You can write a computer program to help you. For the program, the user should be able to input a word with the letters they know filled in and asterisks for those they don’t know. The program should print out a list of all words that fit that description. For example, the input th***ly should return all the words that could work, namely thickly and thirdly.


2)	Write a Python program that allows users to analyze a text file and extract useful information. The program should prompt the user to enter the name of the file to analyze, and then offer several analysis options:
•	Word Count: The program should count the total number of words in the file.
•	Character Count: The program should count the total number of characters (including spaces) in the file.
•	Line Count: The program should count the total number of lines in the file.
•	Most Frequent Words: The program should display the 10 most frequent words in the file, along with their frequencies.
•	Word Search: The program should prompt the user to enter a word to search for in the file, and then display all instances of that word, along with the line numbers where they occur.           
                                      
                                                                        

3)	Hangman Games writes a Python program that allows users to play a game of hangman. The program should generate a random word from a predefined list of words, and then prompt the user to guess letters in the word. The user should be allowed to make a limited number of incorrect guesses before they lose the game.
•	The program should use a pre-defined list of words, stored in a separate text file, with one word per line.
•	The program should display the number of letters in the word, with each unknown letter represented by an underscore (_).
•	The user should be allowed to guess one letter at a time. The program should display the letters that have already been guessed, along with the remaining number of guesses.
•	If the user correctly guesses a letter, the program should update the display to show the letter in the correct position(s).
•	If the user makes an incorrect guess, the program should decrement the remaining number of guesses and display a hangman graphic.
•	If the user correctly guesses all of the letters in the word before running out of guesses, the program should display a message indicating that they won the game.
•	If the user runs out of guesses before correctly guessing all of the letters in the word, the program should display a message indicating that they lost the game, and reveal the word.

4)	Password Strength Checker
Write a Python program that allows users to check the strength of a password. The program should prompt the user to enter a password, and then analyze it based on the following criteria:
Length: The password should be at least 8 characters long.
Complexity: The password should include a combination of uppercase and lowercase letters, numbers, and special characters.
Dictionary Words: The password should not include common dictionary words or phrases.
The program should then provide feedback to the user on the strength of their password, and suggest ways to improve it if necessary.
Here are some additional specifications for the program:
•	The program should use a predefined list of common dictionary words, stored in a separate text file, with one word or phrase per line.
•	The program should handle input errors gracefully, and provide helpful error messages if the user enters invalid input.
•	The program should allow the user to specify custom criteria for password strength, such 
•	as minimum length or required character types.

5)	File Encryption and Decryption
Write a Python program that allows users to encrypt and decrypt files using a symmetric-key algorithm. The program should prompt the user to specify the name of the file to encrypt or decrypt, along with the key to use for encryption or decryption.
•	The program should use a symmetric-key algorithm, such as AES or DES, to encrypt and decrypt files. You can use a third-party library such as PyCryptodome or cryptography to implement the algorithm.
•	The program should handle input errors gracefully, and provide helpful error messages if the file cannot be found or if the user enters invalid input.
•	The program should create a new file with the encrypted or decrypted data, leaving the original file unchanged.
•	The program should use a secure method for storing the encryption key, such as a password-protected file or a keyfile protected by a master password.
•	The program should allow the user to specify custom options for encryption or decryption, such as the mode of operation or the padding scheme.


6)	An acronym is an abbreviation that uses the first letter of each word in a phrase. We see them everywhere. For instance, NCAA for National Collegiate Athletic Association or NBC for National Broadcasting Company. Write a program where the user enters an acronym and the program randomly selects words from a wordlist such that the words would fit the acronym. Below is some typical output generated when I ran the program:
Enter acronym: ABC ['addressed', 'better', 'common']
Enter acronym: BRIAN ['bank', 'regarding', 'intending', 'army', 'naive']

7)	You are given a file namelist.txt that contains a bunch of names. Print out all the names in the list in which the vowels a, e, i, o, and u appear in order (with repeats possible). The first vowel in the name must be a and after the first u, it is okay for there to be other vowels. An example is Ace Elvin Coulson.


8)	File Compression: Write a Python program that compresses a text file by replacing repeated characters with a single character and a count of the number of repetitions. For example, the string "aaabbbcccc" should be compressed to "a3b3c4". Your program should prompt the user to enter the name of the input file and the name of the output file


9)	Phone Book
Implement a program, that allows to register a contact information (name, surname, phone number, address).
The program should provide a console interface , where the user is able to add a new contact , edit the contact information of the already existing one and remove one of the contacts.
All the registered information should be kept in a text file, so that it is not lost after closing the program. After any change of the contact information it should be saved in the existing file. During the time the program runs it should be able to read from the text file where all the information is kept.


10)	JSON Editor
Write a program that takes as an input argument a text file in JSON format. The program should be able to decode the content of the JSON file and allow to make changes directly on the file. For example you have a file with the following content:
{“name”: “Angela”, “age”:23, “address”: {“street”: “halabyan”}}
When passing the file to the program it decodes the content and allows the user to make changes on a file, for example, the user enters the following command:
name=Jonny
in the result the program should change the JSON file to:
{“name”: “Jonny”, “age”:23, “address”: {“street”: “halabyan”}}
Another example, the user enters the following command:
address.street=tumanyan
in the result the program should change the JSON file to:
{“name”: “Jonny”, “age”:23, “address”: {“street”: “tumanyan”}}
Write a program that allows to work with any depth of a JSON file. You can find more information on a JSON file format here -> JSON 

11)	
Data Validator
Write a program that performs checking on the entered data, specifically it should check whether the following types of data are entered correctly:
1.	Email
2.	Website URL
3.	Date
4.	Number
5.	Credit Card Number
6.	Mobile Phone Number
The program asks the user to choose one of the above mentioned types of data and then enters the data he/she wants to check. For example the user chooses an Email option and then enters wrong@email . The program should check the format of the email and should tell the user that it is not a valid email. This applies to all the types of data.

12)	Text Analyzer
Write a program that works with a text file. The aim of the program is to read a text from the text file and analyze it. Specifically it should count and print:
1.	the number of words
2.	the number of letters
3.	the number of sentences
4.	the most used letter in a text
5.	the most used word in a text
For example if out text file contains this text:
“Hello from C++ world”
the program should give the following output:
Words: 4
Letters: 15 (special characters and space are not counted)
Sentences: 1
Letter frequency: o (both o and l are used 3 times so any of the letters is considered as a right answer)
Word frequency: 0 (there is no word that is used more than once)
The result should be kept in a separate text file.


13)	The Library Management System is a program that allows users to manage a library collection of books. The system provides the following functionalities:
•	Add Books: The user is allowed to enter the full name of the author, the name of the book and its publication date. The list of all the books should be kept in a text file.
•	Remove Books: The user is allowed to remove a book from the list by using its name.
•	View All Books: The user can see the list of all the books in the library.
•	Sort Books Alphabetically: The user can make the sorted list of all the books in the library. The system should store the library's book collection in a text file. When the program starts, it should read the file and load the books into memory. When the user makes changes to the library, such as adding or removing a book, the program should update the file accordingly. To implement this system, you can use Python's built-in file handling capabilities to read and write to the file that stores the library collection. You can also use Python's data structures like lists and dictionaries to store the book collection in memory and provide the necessary functionalities like sorting and removing books.

14)	ToDo List
Write a task organizing program.
The aim of the program is to provide a console interface, with the help of which the user can see his/her daily tasks. Each task should be only one sentence.
The user should be able to add tasks, see all the tasks, mark if the task is done or not and remove the task from the list if necessary.
For the actions (mentioned above) to be performed the program should provide a list of commands that correspond to those actions.
The tasks should be kept in a separate text file, so that they are not lost when the user closes the program.


15)	The digital root of a number n is obtained as follows: Add up the digits n to get a new number. Add up the digits of that to get another new number. Keep doing this until you get a number that has only one digit. That number is the digital root. For example, if n = 45893, we add up the digits to get 4 + 5 + 8 + 9 + 3 = 29. We then add up the digits of 29 target 2+9=11. We then add up the digits of 11toget 1+1=2. Since 2 has only one digit, 2 is our digital root.


16)	Write a function that is given a 9 × 9 potentially solved Sudoku and returns True if it is solved correctly and False if there is a mistake. The Sudoku is correctly solved if there are no repeated numbers in any row or any column or in any of the nine “blocks.”


17)	 You are given a file called students.txt.
A typical line in the file looks like:
walter melon melon@email.msmary.edu 555-3141
There is a name, an email address, and a phone number, each separated by tabs. Write a program that reads through the file line-by-line, and for each line, capitalizes the first letter of the first and last name and adds the area code 301 to the phone number. Your program should write this to a new file called students2.txt. Here is what the first line of the new file should look like:
 Walter Melon        melon@email.msmary.edu        301-555-3141 can you generate students.txt














