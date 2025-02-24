import mysql.connector

try:
	#database credentials
	db = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd=[REDACTED],
		database="BeautyHive"
		)

	#cursor object to use this database
	mycursor = db.cursor()
except:
	print("Could not connect to the BeautyHive database!")


''' INITIALIZES THE BEAUTYHIVE DATABASE
try:
	mycursor.execute("CREATE DATABASE BeautyHive")
except:
	print("Could not initialize the database, please check your syntax.")
'''

''' INITIALIZE USER TABLE, EXECUTES DESCRIBE COMMAND 
try:
	mycursor.execute("CREATE TABLE User (user_ID VARCHAR(20) PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), user_email VARCHAR(50), user_password VARCHAR(50))")

	mycursor.execute("DESCRIBE User")
	print("Here are the attributes and datatypes for table User:\n")
	for x in mycursor:
		print(x)
except:
	print("Could not initialize the user table, please check your syntax.")
'''

''' INITIALIZE PRODUCT TABLE, EXECUTE DESCRIBE COMMAND
try:
	mycursor.execute("CREATE TABLE Product (product_ID INT AUTO_INCREMENT PRIMARY KEY, product_type VARCHAR(50), product_name VARCHAR(50), brand VARCHAR(50), product_price DECIMAL(10,2))")

	mycursor.execute("DESCRIBE Product")
	print("Here are the attributes and datatypes for table Product:\n")

	for x in mycursor:
		print(x)
except:
	print("Could not initialize product table, please check your syntax.")
'''

''' INITIALIZE REVIEW TABLE, EXECUTE DESCRIBE COMMAND 

try:
	mycursor.execute("CREATE TABLE Review (review_ID INT AUTO_INCREMENT PRIMARY KEY, user_ID VARCHAR(20), product_ID INT, short_response VARCHAR(100), effectiveness INT, CHECK (effectiveness BETWEEN 1 AND 5), value INT, CHECK (value BETWEEN 1 AND 5), phys_properties INT, CHECK (phys_properties BETWEEN 1 AND 5), overall_5rating DECIMAL(3,0) AS ((effectiveness + value + phys_properties) / 3) STORED, FOREIGN KEY (user_ID) REFERENCES User(user_ID), FOREIGN KEY (product_ID) REFERENCES Product(product_ID))")	

	mycursor.execute("DESCRIBE Review")
	print("Here are the attributes and datatypes for table Review:\n")
	
	for x in mycursor:
		print(x)
except:
	print("Could not initialize review table, please check your syntax")
'''	

'''INSERT USERS INTO USER TABLE, AND SELECT * TO SHOW ALL USERS
try:
	mycursor.execute("INSERT INTO User (user_ID, first_name, last_name, user_email, user_password) VALUES (%s, %s, %s, %s, %s)",('Fluffybunny123',[REDACTED],[REDACTED],[REDACTED],'fluffy!!'))
	mycursor.execute("INSERT INTO User (user_ID, first_name, last_name, user_email, user_password) VALUES (%s, %s, %s, %s, %s)",('FunnyCapybara',[REDACTED],[REDACTED],[REDACTED],'Ilovecapybara1234'))
	mycursor.execute("INSERT INTO User (user_ID, first_name, last_name, user_email, user_password) VALUES (%s, %s, %s, %s, %s)",('AstuteWalrus','Homer','Pace','hpace@pace.edu','19061906'))
	db.commit()

	mycursor.execute("SELECT * FROM User")
	print('Here are all the users:\n')
	for x in mycursor:
		print(x)
except:
	print("Could not insert data, please check your syntax.")
'''

'''INSERT PRODUCTS INTO PRODUCT TABLE, AND SELECT * TO SHOW ALL PRODUCTS
try:
	mycursor.execute("INSERT INTO Product (product_type, product_name, brand, product_price) VALUES (%s, %s, %s, %s)",('Makeup', 'Precisely, My Brow Wax', 'Benefit Cosmetics', 27.00))
	mycursor.execute("INSERT INTO Product (product_type, product_name, brand, product_price) VALUES (%s, %s, %s, %s)",('Makeup', 'Major Glow Balm', 'Patrick Ta Beauty', 50.00))
	mycursor.execute("INSERT INTO Product (product_type, product_name, brand, product_price) VALUES (%s, %s, %s, %s)",('Skincare', 'Vanilla Lip Care Duo', 'Laneige', 34.00))
	mycursor.execute("INSERT INTO Product (product_type, product_name, brand, product_price) VALUES (%s, %s, %s, %s)",('Skincare', 'The Silk Serum', 'Tatcha', 98.00))
	db.commit()

	mycursor.execute("SELECT * FROM Product")
	print('Here are all the products:\n')
	for x in mycursor:
		print(x)
except:
	print("Could not insert data, please check your syntax.")
'''

'''INSERTS REVIEWS INTO REVIEW TABLE, AND SELECT * TO SHOW ALL PRODUCTS
try:
	mycursor.execute("INSERT INTO Review(user_ID, product_ID, short_response, effectiveness, value, phys_properties) VALUES (%s, %s, %s, %s, %s, %s)", ('Fluffybunny123',1,'Product keeps my eyebrows in place all day!', 5, 5, 4))
	mycursor.execute("INSERT INTO Review(user_ID, product_ID, short_response, effectiveness, value, phys_properties) VALUES (%s, %s, %s, %s, %s, %s)", ('AstuteWalrus',1,'I like this product a lot, just wish the packaging was less ugly.', 5, 5, 2))
	mycursor.execute("INSERT INTO Review(user_ID, product_ID, short_response, effectiveness, value, phys_properties) VALUES (%s, %s, %s, %s, %s, %s)", ('Fluffybunny123',1,'Product keeps my eyebrows in place all day!', 5, 5, 4))
	mycursor.execute("INSERT INTO Review(user_ID, product_ID, short_response, effectiveness, value, phys_properties) VALUES (%s, %s, %s, %s, %s, %s)", ('FunnyCapybara',2,'This product is a little out of my budget, but works very well!', 5, 2, 4))
	mycursor.execute("INSERT INTO Review(user_ID, product_ID, short_response, effectiveness, value, phys_properties) VALUES (%s, %s, %s, %s, %s, %s)", ('Fluffybunny123',4,'This product is my holy grail', 5, 5, 5))
	mycursor.execute("INSERT INTO Review(user_ID, product_ID, short_response, effectiveness, value, phys_properties) VALUES (%s, %s, %s, %s, %s, %s)", ('AstuteWalrus',3,'Keeps my lips super smooth all day long.', 5, 5, 5))
	mycursor.execute("INSERT INTO Review(user_ID, product_ID, short_response, effectiveness, value, phys_properties) VALUES (%s, %s, %s, %s, %s, %s)", ('AstuteWalrus',2,'This product is way too overpriced, did not work for my skin.', 1, 1, 1))
	mycursor.execute("INSERT INTO Review(user_ID, product_ID, short_response, effectiveness, value, phys_properties) VALUES (%s, %s, %s, %s, %s, %s)", ('Fluffybunny123',3,'I hate the taste and smell of this product. Never buying it again', 1, 3, 1))
	db.commit()
	
	mycursor.execute("SELECT * FROM Review")
	print('Here are all the reviews:\n')
	for x in mycursor:
		print(x)
except:
	print("Could not insert data, please check your syntax.")
'''

''' PERFORM SOME READ OPERATIONS
try:
	mycursor.execute("SELECT * FROM Review WHERE overall_5rating < 3")
	print("Here are all of the reviews where the overall rating is less than 3:\n")
	for x in mycursor:
		print(x)

	mycursor.execute("SELECT p.product_name, p.brand, p.product_price, r.short_response, r.overall_5rating FROM Product as p, Review as r WHERE p.product_ID = r.product_ID")
	print("\nHere are the short responses and overall ratings for all the available products on the platform:\n")
	for x in mycursor:
		print(x)
except:
	print("Could not read data, please check your syntax.")
'''

'''PERFORMS AN UPDATE ON THE REVIEW TABLE
try:
	#Updates the short response and numerical ratings for the review where product ID = 2 and User_ID = AstuteWalrus
	mycursor.execute("UPDATE Review SET short_response = 'I retried this product, and I take back what I said before.', effectiveness = 5, value = 5, phys_properties= 5 WHERE user_ID = 'AstuteWalrus' AND product_ID = 2")

	mycursor.execute("SELECT * FROM Review")
	print('Here are all the reviews:\n')

	for x in mycursor:
		print(x)
except:
	print("Could not update data, please check your syntax.")
'''

'''PERFORMS A DELETE ON THE REVIEW TABLE
try:
	mycursor.execute("DELETE FROM Review WHERE review_ID = 8")

	mycursor.execute("SELECT * FROM Review")
	print('Here are all the reviews:\n')

	for x in mycursor:
		print(x)
except:
	print("Could not delete data, please check your syntax.")
'''

''' selects all reviews for the products and sort in descending order
try:
	mycursor.execute("SELECT p.product_name, p.brand, p.product_price, r.short_response, r.overall_5rating FROM Product as p, Review as r WHERE p.product_ID = r.product_ID ORDER BY r.overall_5rating DESC")

	print('Here are all the reviews:\n')

	for x in mycursor:
		print(x)
except:
	print("Could not select data, please check your syntax.")
'''


''' selects and groups products by product name, taking the average of all overall_5ratings for that product
try:
	mycursor.execute("SELECT p.product_name, AVG(r.overall_5rating) FROM Product as p, Review as r WHERE p.product_ID = r.product_ID GROUP BY p.product_name")

	print('Here are all of the product names, each with the average 5-star rating for each product:\n')

	for x in mycursor:
		print(x)
except:
	print("Could not select data, please check your syntax.")
'''

''' DELETES DUPLICATE OBSERVATION
mycursor.execute("DELETE FROM Review WHERE review_ID = 3")
db.commit()

mycursor.execute("SELECT * FROM Review")
for x in mycursor:
		print(x)
'''
#ensures that there is only one review, per person, per product
#mycursor.execute("ALTER TABLE Review ADD CONSTRAINT OneReview_PerPerson_PerProduct UNIQUE (user_ID, product_ID)")

#code to test unique constraint, tries to add an observation that violates the unique constraint
try:
	mycursor.execute("INSERT INTO Review(user_ID, product_ID, short_response, effectiveness, value, phys_properties) VALUES (%s, %s, %s, %s, %s, %s)", ('Fluffybunny123',1,'Product keeps my eyebrows in place all day!', 5, 5, 4))

except:
	print("You have already made a review for this product! Please consider updating your review instead.")
