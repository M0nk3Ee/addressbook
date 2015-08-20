'''
Created on 4 Oct 2012
update now

@author: illingm01
'''
import sys
import string
import pickle, pprint

AddressBook = []
UnsavedChanges = False
Disk_File = "Contact_DB.pkl"
    
class Contact(object):
	def __init__(self, FirstName=None, LastName=None, Tel=None):
		self.FirstName 	= FirstName
		self.LastName	= LastName 	
		self.Tel	= Tel

	def PrintContact(self):
		print self.FirstName
		print self.LastName
		print self.Tel

def CreateContact(): #Creates and returns the new Contact Object
	global UnsavedChanges
        FirstName       = raw_input("First Name	: ")
        LastName        = raw_input("Last Name	: ")
	Tel		= raw_input("Tel no		: ")
	NewContact = Contact()
        NewContact.FirstName    = FirstName
        NewContact.LastName     = LastName
	NewContact.Tel		= Tel
	UnsavedChanges = True
	return NewContact

def SaveToDisk():
	global UnsavedChanges
	try:	
		output = open(Disk_File, 'wb')
		pickle.dump(AddressBook, output, -1)
		output.close()
		UnsavedChanges = False		
	except IOError:
		print "Error: Can not save to ", Disk_File

def LoadFromDisk():
	global UnsavedChanges
	global AddressBook
	DoALoadFromDisk = True
	UserInput = "None"
	if UnsavedChanges:
		while (UserInput != 'yes') and (UserInput != 'no'):
			UserInput = raw_input("There are Unsaved changes, loading from disk will discard these changes.  Do you want to continue? [yes|no]: ").lower()
		if str(UserInput) == 'no': 	
			DoALoadFromDisk = False
	if DoALoadFromDisk:
		print "Loading from Disk..."			
		try:
			input = open(Disk_File, 'rb')
			AddressBook = pickle.load(input)
			input.close()
			UnsavedChanges = False
		except IOError:
			print "Error: Cannot open ", Disk_File

def SortAddressBook():
	global AddressBook
	print "Sorting AddressBook..."
	AddressBook.sort(key=lambda Contact: (Contact.LastName, Contact.FirstName)) 

def SearchAddressBook(AddressBookToSearch, StringToSearch ):
	Result = 'None'
	print("Searching Object: ", StringToSearch)
	return Result
	
def ExitProgram():
	global UnsavedChanges
	UserInput = "None"
	if UnsavedChanges:
		while (UserInput != 'yes') and (UserInput != 'no'):
			UserInput = raw_input("You have unsaved changes to the Address Book, Would you like to save them now? [yes|no]: ").lower()	
			#print "You Entered: ", UserInput
		if str(UserInput) == 'yes':
			SaveToDisk()
			print "Saved Changes to Disk..."
	print "Bye..."

def RunMenu():
	StayinMenu = True
	while StayinMenu:
		print(" ")
		print("-------------")
		print("Menu")
		print(" ")	
		print("Press 1 to Add A New Contact To Address Book")
		print("Press 2 to Display In Memory Address Book")
		print("Press 4 to Sort Address Book")
		print("Press 5 to Save Address Book To Disk")
		print("Press 6 to Search for Contact")
		print("Press 7 to Load Address Book From Disk")
		print("Press 9 to Quit")
		print(" ")
		print("-------------")
		UserInput = raw_input("Please make a selection: ")
		if UserInput == '1':
			AddressBook.append(CreateContact())
			SortAddressBook()
		elif UserInput == '2':
			print(" ")
			print("Printing Address Book")
			print(" ")
			for index in range(len(AddressBook)):
				print(string.join(['Index No	: ', str(index)]))
				AddressBook[index].PrintContact()
				#print(string.join(['First Name	: ', AddressBook[index].FirstName]))
				#print(string.join(['Last Name	: ', AddressBook[index].LastName]))
				#print(string.join(['Tel no.		: ', AddressBook[index].Tel]))
		elif UserInput == '3':
			for index in range(len(AddressBook)):
				AddressBook[index].PrintContact()		
		elif UserInput == '4':
			SortAddressBook()	
		elif UserInput == '5':
			print("Saving...")
			SaveToDisk()
		elif UserInput == '6':
			StringToSearch = raw_input("Enter your Search String: ")
			Result = SearchAddressBook(AddressBook, StringToSearch)	
			print(str(Result))
		elif UserInput == '7':
			print("Loading...")
			LoadFromDisk()
		elif UserInput == '9':
			print "Calling ExitProgram() "
			ExitProgram()	
			break

LoadFromDisk()
RunMenu()
