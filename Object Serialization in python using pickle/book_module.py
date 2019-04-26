class Book(object):
	start_id = 1
	def __init__(self,name,aurthor,price):
		self._id = Book.start_id
		Book.start_id = Book.start_id + 1
		self._name = name
		self._aurthor = aurthor
		self._price = price

	def getId(self):
		return self.id
	def getName(self):
		return self.name
	def getAurthor(self):
		return self.aurthor
	def getPrice(self):
		return self.price

	def __str__(self):
		return 'Book(id={}, name={},aruthor={}, price={})'.format(self._id, self._name, self._aurthor, self._price)

