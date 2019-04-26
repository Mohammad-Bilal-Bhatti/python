# Imporing the Book Class From book_module
from book_module import Book
# Importing the pickle library for reading and writing objects.
# If Module not found Error is occurd try the following command in the cmd and run the script agein.
# pip install pickle
import pickle

# Globally defining the file_name as "Object.data"
# We can specify any  file_name with what ever the extersion(e.g: .data, .db, .obj, etc)
file_name = 'Object.data'

def readObject():
	'''
	Read the Object stored in the file
	Return Object what ever stored in the file
	On Exception return None if file Not found or something else occurs.
	'''
	try:
		# Opening the File accociated with file_name in read binary mode.
		with open(file_name,'rb') as object_file:			
			return pickle.load(object_file)			# Load the Object previously Stored In File and Return it.
	except Exception as e:							# On any Exception like File Not Found It returns None.
		return None

def writeObject(object):
	'''
	Write the Object in the associated file
	Return True on Success and False on Failure.
	'''
	try:
		# Opening the File accociated with file_name in write binary mode.
		with open(file_name,'wb') as object_file:
			pickle.dump(object,object_file)			# Write the Object passed as the function argument in the file.	
			return True								# Return True on Success. 
	except Exception as e:							# Returns False on Failure.
		return False





def main():

	# Uncomment the Below lines For Stroing the Object to the File.

	# --------------WRITING-OBJECT---------------------

	# Creating Book 1 Object.
	# book1 = Book('Java The Complete Reference','Tahir Magsi',1000)
	
	# Creating Book 2 Object.
	# book2 = Book('Introduction To Java','Deniel Liang',1500)

	# Printing The Object.
	# print(book1)
	# print(book2)

	# Making The List Of Books.
	# book_list = [book1, book2]

	# Write the list of books to the File and Print the status returned.
	# print(writeObject(book_list))

	# --------------READING-OBJECT---------------------

	# Reading the Stored Object to book_list
	book_list = readObject()

	# Now printing the list Iteratively.
	for book in book_list:
		print(book)



if __name__ == '__main__':
	main()