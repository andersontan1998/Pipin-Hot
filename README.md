# Pipin' Hot Delivery

The objective of this application is to create an easy-to-use online restaurant service that will provide support for all the major needs of a restaurant, giving restaurants the tools they need to customize and set up their establishment on our system, create menus, prices, handle customer support and staffing, while also providing an interface for customers to quickly, easily, and conveniently order takeout from all of their favorite participating restaurants.

Some packages you may need: (all located in requirements.txt)\
You can use pip install -r requirements.txt

asgiref==3.5.1\
Django==4.0.4\
django-crispy-forms==1.14.0\
django-mathfilters==1.0.0\ 
numpy==1.22.3\ 
pandas==1.4.2\
Pillow==9.1.0\
python-dateutil==2.8.2\
pytz==2022.1\
six==1.16.0\
sqlparse==0.4.2\
tk==0.1.0

System features: 
- [x] 1. Provide a GUI , not necessarily web - based , with pictures to show the descriptions of each dish and price; each registered customer/VIP has a password to login, when they log in, based on the history of their prior choic e s , different registered customer/VIP will have different top 3 listing dishes. For new customers or visitors, the top 3 most popular dishes and top 3 highest rated dishes are listed on the first page. 
- [x] 2. A customer can choose to 1) pick up the dishes in person, or 2) by restaurant delivery. For case 1) s/he can only complain/compliment the chef. 
- [x] 3. A customer can file complaints/compliments to chef of the food s/he purchased and deliver person who delivered the dish or other customers who didn’t behave in the discussion forums. Delivery person can complain/compliment customers s/he delivered dishes, all complaints/compliments are handled by the manager. The complained person has the right to dispute the complaint, the manager made the final call to dismiss the complaint or let the warning stay and inform the impacted parties. Customers/delivery people whose complaints are decided to be without merit by the manager will receive one additional warning. 
- [ ] 4. Registered customers having 3 warnings are de - registered. VIPs having 2 warnings are put back to registered customers (with warnings cleared). The warnings should be displayed in the page when the customer logs in. 
- [x] 5. Every customer should deposit some money to the system. If the price of the order is more expensive than the deposited money in the account, the order is rejected and the custom er receives one warning automatically for being reckless. 
- [ ] 6. Customers who are kicked out of the system or choose to quit the system will be handled by the manager: clear the deposit and close the account. And kicked - out customer is on the blacklist of the restaurant: cannot register any more. 
- [x] 7. The chef whose dishes received consistently low ratings (<2) or 3 complaints, will be demoted (less salary), a chef demoted twice is fired. Conversely, a chef whose dishes receive high ratings (>4) or 3 compliments, will receive a bonus. One compliment can be used to cancel one complaint. The delivery people are handled the same way. 
- [x] 8. The delivery people will compete to deliver the order by bidding, the manager assigns the order from bidding results: the one with lowest delivery price is generally chosen; if the one with higher asking price is chosen, the manager should write a memo in the system as justifications. The delivery person who didn’t deliver any in the past 5 orders will automatically receive one warning. 
- [x] 9. Each team comes up with a creativity feature of the system to make it more exciting , e.g., smart - phone based system, voice - based features, or efficient route planning for delivery , which is worth 10% of overall score of the final project.
- [ ] ______________________________________________________________________________________________________________________________________________________________
Specification 1: Finished
The ‘menu’ app contains the solution for specification 1. So a customer would have the regular menu and top 3 listing menu depending on their purchase history. We look at the rating each customer gave to an item to decide which items to put on the top 3 listing menu.

Specification 2: Finished
The ‘order_system’ app contains the solution for specification 2. That is, a customer can order from the menu and decide if they want delivery or pickup. There is a ‘is_delivery’ on the order model so that the backend can check if the customer is allowed to review the chef’s of the item.

Specification 3: Partially Done
The ‘forum’ app allows a customer to pick which order to review. Once an order is selected, the customer can review each item and its chef. The customer must decide if it is a complaint or compliment. The ‘dashboard’ allows a manager to review the reviews from customers. They can ultimately decide to reject or accept the review. The respective review is then processed and a warning is given to the chef/deliverer. If the review is rejected, then the customer receives a warning.

Specification 4: Partially done
The ‘dashboard’ app allows the user to see the number of warnings. It is a net warning: compliments - complains. So a negative number means that they have warnings.


Specification 5: Finished
The ‘dashboard’ app allows a customer to add funds to their account and see their balance. The ‘order_system’ app checks the the total price and if it’s more than the customer funds it deletes the order and gives the customer a warning.

Specification 6: Unable to do


Specification 7: Unable to do

Specification 8: Partially done

Specification 9: Partially done

We made a home page that makes it easy to navigate the website and the register page features a single page application!
