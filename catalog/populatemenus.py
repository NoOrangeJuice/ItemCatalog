from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem, User

engine = create_engine('postgresql:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

## Dummy User. ##
user1 = User(name="Calvin Ellington", email="calvinje@gmail.com")
session.add(user1)
session.commit()

restaurant1 = Restaurant(user = user1, name="Chaotic Neutral Cafe")
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(user = user1, name="The Atrium")
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(user = user1, name="Zero Point Espresso")
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(user = user1, name="Cafe Orange Juice")
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(user = user1, name="Shannon's house of waffles")
session.add(restaurant5)
session.commit()

menuItem1 = MenuItem(user = user1, name="Pitch Black Cold Brew",
                     description="Darker than Asphalt, stronger than the sun.",
                     price="$2.75",
                     restaurant=restaurant1)


menuItem2 = MenuItem(user = user1, name="Espresso the Terrible",
                     description="This isn't your mom's frappuccino.",
                     price="$2.25",
                     restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user = user1, name="Lascivious Latte",
                     description="You touch it you buy it, got it friendo?",
                     price="$4.50",
                     restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user = user1, name="Dirty Dan's Dirty Chai",
                     description="Don't ask whats in it.. Or who Dan is.",
                     price="$2.75",
                     restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user = user1, name="Large Macchiato",
                     description="Get out.",
                     price="$125.99",
                     restaurant=restaurant1)

session.add(menuItem5)
session.commit()


menuItem1 = MenuItem(user = user1, name="Bagel for your Trouble",
                     description="Toasted whole wheat bagel, with cream cheese, for free.",
                     price="$0.00",
                     restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user = user1, name="Confusion Caprese",
                     description="Mozarella with fresh tomatoes and basil on sourdough without any sense of meaning.",
                     price="$7.75",
                     restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user = user1, name="Paradox Parfait",
                     description="It's yogurt and fruit.. Or is it?",
                     price="$4.50",
                     restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user = user1, name="The Nutella Nietzsche ",
                     description="Because lets face it, he was a nut.",
                     price="$8.75",
                     restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user = user1, name="B.L.T.",
                     description="Fresh cut bacon with lettuce and time enough to wonder why?",
                     price="$5.99",
                     restaurant=restaurant2)

session.add(menuItem5)
session.commit()


menuItem1 = MenuItem(user = user1, name="House Blend",
                     description="A blend of the coffee I found at my friends house.",
                     price="$2.75",
                     restaurant=restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user = user1, name="Green Espresso",
                     description="100 percent post consumer content.",
                     price="$2.25",
                     restaurant=restaurant3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user = user1, name="Matcha Man",
                     description="Green tea with steamed milk and a good attitude.",
                     price="$4.50",
                     restaurant=restaurant3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user = user1, name="Flat White",
                     description="It's from Australia not Starbucks.",
                     price="$4.75",
                     restaurant=restaurant3)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user = user1, name="Macchiato",
                     description="Come in!",
                     price="$0.25",
                     restaurant=restaurant3)

session.add(menuItem5)
session.commit()

menuItem1 = MenuItem(user = user1, name="Small cup of OJ",
                     description="A small cup of OJ",
                     price="$2.75",
                     restaurant=restaurant4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user = user1, name="Large cup of OJ",
                     description="A large cup of OJ",
                     price="$4.25",
                     restaurant=restaurant4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user = user1, name="One Gallon of OJ",
                     description="One Gallon of OJ",
                     price="$10.50",
                     restaurant=restaurant4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user = user1, name="Fruit bearing orange tree",
                     description="One fruit bearing orange tree",
                     price="$100.75",
                     restaurant=restaurant4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user = user1, name="Small Grove",
                     description="A small grove of orange trees",
                     price="$500.99",
                     restaurant=restaurant4)

session.add(menuItem5)
session.commit()

menuItem1 = MenuItem(user = user1, name="Eggs and hashbrowns",
                     description="Any way you like em hon",
                     price="$4.75",
                     restaurant=restaurant5)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user = user1, name="Endless Coffee",
                     description="You've got to leave by the time we close sugar",
                     price="$4.25",
                     restaurant=restaurant5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user = user1, name="Country Ham with Mashed Potatoes",
                     description="Fried with love and mashed with a purpose",
                     price="$9.50",
                     restaurant=restaurant5)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user = user1, name="Waffle STACK",
                     description="A whole stack sweetie, no catch",
                     price="$7.75",
                     restaurant=restaurant5)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user = user1, name="French Toast",
                     description="French Toast with fresh fruit and sweet cream",
                     price="$9.99",
                     restaurant=restaurant5)

session.add(menuItem5)
session.commit()

print "added some really great food!"
