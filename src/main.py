import sys

from PyQt4.QtGui import * 
from PyQt4.QtCore import *

sys.path.insert(0, './dataFill/')

from fill_table_class import FillTable

sys.path.insert(0, './test/model/mongodbtest2/')

from DaoMaster import DaoMaster
from DaoSession import DaoSession
from Users import Users
from UsersDao import UsersDao


if __name__ == "__main__":
	dao_master = DaoMaster()
	dao_session = dao_master.getSession()
	users_dao = dao_session.getUsersDao()
	
	fill_table = FillTable()
	fill_table.addField('Name', 'Nombre')
	fill_table.addField('LastName', 'Apellido')
	fill_table.addField('Age', 'Edad')
	fill_table.setData(users_dao.getAll())
	
	app 	= QApplication(sys.argv)
	table 	= QTableWidget()
	tableItem 	= QTableWidgetItem()

	# initiate table
	#table.setWindowTitle("QTableWidget Example @pythonspot.com")
	table.resize(400, 250)
	#table.setRowCount(4)
	#table.setColumnCount(2)

	## set data
	#table.setItem(0,0, QTableWidgetItem("Item (1,1)"))
	#table.setItem(0,1, QTableWidgetItem("Item (1,2)"))
	#table.setItem(1,0, QTableWidgetItem("Item (2,1)"))
	#table.setItem(1,1, QTableWidgetItem("Item (2,2)"))
	#table.setItem(2,0, QTableWidgetItem("Item (3,1)"))
	#table.setItem(2,1, QTableWidgetItem("Item (3,2)"))
	#table.setItem(3,0, QTableWidgetItem("Item (4,1)"))
	#table.setItem(3,1, QTableWidgetItem("Item (4,2)"))
	
	fill_table.setTable(table)
	fill_table.fill()

	#show table
	table.show()
	app.exec_()
