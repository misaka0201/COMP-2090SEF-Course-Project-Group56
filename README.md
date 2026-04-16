# COMP-2090SEF-Course-Project Task 1 
Chen Man Ho 14257154 Chen Chun Tao 14252183 Li Feng Quan 14258022
##  Application: online shopping system
1. Class: Product is a class, and Product(1, "Apple", 5.5) creates a specific product object. The code defines multiple classes like Product, User, Staff
2. Inheritance: Person, Staff and User
Both Staff and User automatically possess the "name" and "password" attributes of the Person class.
3. Encapsulation: in the Product class, the stock attribute cannot be modified directly from outside. It must be changed through methods like add_stock() (for restocking) or sell() (for selling).
4. Polymorphism: __str__ method behaves in Product class: displays product information.
In User class: shows only the username.
In Staff class: shows name and staff ID.
Although the method name is the same, each class implements it in its own way.
5. Class Method: marked with @classmethod. For example, Product.get_total() can be called directly through the class name without creating an object, to get the total number of product types
6. Static Method: marked with @staticmethod. For example, Product.to_money() is a utility function that converts numbers to currency format.
7. Composition: the User class has a self.cart list that stores tuples of Product objects and their quantities.<br>
`The language of the program output is English, but the comments are Chinese`
## `User Guide`
### Staff Functions
Staff can log in to manage products and view sales data.

Staff Login: Select 1, enter username and password<br>
Staff Registration: Select 4, register a new staff account<br>
After login, you can:<br>
Add Product: Enter product name, price, stock quantity<br>
Delete Product: Enter product ID and confirm deletion<br>
Edit Product: Modify price or stock (press Enter to skip)<br>
View Products: Display all products list<br>
Sales Records: View all sales history<br>
Sales Report: Statistics on total products, inventory value, sales amount<br>
### User Functions
Users can shop and view purchase history.

User Login: Select 2, enter username and password
User Registration: Select 3, register a new account

After login, you can:<br>
Browse Product: View all available products<br>
Search Products: Enter keywords to find products<br>
Shopping Cart: View items added to cart<br>
Add to Cart: Enter product ID and quantity<br>
Checkout: Confirm cart contents and pay<br>
Purchase History: View last 10 purchase records<br>
### File Description
The program automatically creates 4 text files to store data:

products.txt: Product data

users.txt: User data

staff.txt: Staff data

history.txt: Sales records

Introduction video:
https://youtu.be/stsT9_9EVHY
