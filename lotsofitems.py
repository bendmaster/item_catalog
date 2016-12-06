from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///item_catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Hockey Items
category1 = Category(user_id=1, name="Hockey")

session.add(category1)
session.commit()

Item0 = Item(user_id=1, name="Hockey Stick", description="Carbon fiber hockey stick",
             price="$98.50", category=category1)

session.add(Item0)
session.commit()


Item1 = Item(user_id=1, name="Gloves", description="Hockey Gloves",
             price="$52.99", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Skates", description="Hockey Skates",
             price="$105.50", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Puck", description="Hockey Puck",
             price="$3.99", category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Helmet", description="Hockey Helmet",
             price="$107.99", category=category1)

session.add(Item4)
session.commit()

Item5 = Item(user_id=1, name="Goal", description="Hockey Goal",
             price="$100.99", category=category1)

session.add(Item5)
session.commit()

Item6 = Item(user_id=1, name="Bag", description="Hockey Bag",
             price="$30.99", category=category1)

session.add(Item6)
session.commit()

Item7 = Item(user_id=1, name="Mouthguard",
             description="Mouthguard", price="$3.49", category=category1)

session.add(Item7)
session.commit()


# Snowboarding Items
category2 = Category(user_id=1, name="Snowboarding")

session.add(category2)
session.commit()


Item1 = Item(user_id=1, name="Goggles", description="Anti Fogging Goggles",
             price="$47.99", category=category2)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Snowboard",
             description="a snowboard", price="$205", category=category2)

session.add(Item2)
session.commit()


# Soccer items
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, name="Ball", description="a soccer ball",
             price="$18.99", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Cleats", description="Soccer Cleats",
             price="$66.99",  category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Socks", description="Soccer socks",
             price="$9.95", category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Shinguards", description="Shinguards",
             price="$6.99", category=category1)

session.add(Item4)
session.commit()


# # Menu for Thyme for that
# category1 = category(user_id=1, name="Thyme for That Vegetarian Cuisine ")

# session.add(category1)
# session.commit()


# Item1 = Item(user_id=1, name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
#                      price="$2.99", category=category1)

# session.add(Item1)
# session.commit()

# Item2 = Item(user_id=1, name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
#                      price="$5.99", category=category1)

# session.add(Item2)
# session.commit()

# Item3 = Item(user_id=1, name="Honey Boba Shaved Snow",
# description="Milk snow layered with honey boba, jasmine tea jelly, grass
# jelly, caramel, cream, and freshly made mochi", price="$4.50",
# category=category1)

# session.add(Item3)
# session.commit()

# Item4 = Item(user_id=1, name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
#                      price="$6.95",  category=category1)

# session.add(Item4)
# session.commit()

# Item5 = Item(user_id=1, name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
#                      price="$7.95", category=category1)

# session.add(Item5)
# session.commit()

# Item2 = Item(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
#                      price="$6.80", category=category1)

# session.add(Item2)
# session.commit()


# # Menu for Tony's Bistro
# category1 = category(user_id=1, name="Tony\'s Bistro ")

# session.add(category1)
# session.commit()


# Item1 = Item(user_id=1, name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
#                      price="$13.95", category=category1)

# session.add(Item1)
# session.commit()

# Item2 = Item(user_id=1, name="Chicken and Rice", description="Chicken... and rice",
#                      price="$4.95", category=category1)

# session.add(Item2)
# session.commit()

# Item3 = Item(user_id=1, name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
#                      price="$6.95", category=category1)

# session.add(Item3)
# session.commit()

# Item4 = Item(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
# description="Milk, cream, salt, ..., Liquid nitrogen magic",
# price="$3.95", category=category1)

# session.add(Item4)
# session.commit()

# Item5 = Item(user_id=1, name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
#                      price="$7.95", category=category1)

# session.add(Item5)
# session.commit()


# # Menu for Andala's
# category1 = category(user_id=1, name="Andala\'s")

# session.add(category1)
# session.commit()


# Item1 = Item(user_id=1, name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
#                      price="$9.95", category=category1)

# session.add(Item1)
# session.commit()

# Item2 = Item(user_id=1, name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
#                      price="$7.95", category=category1)

# session.add(Item2)
# session.commit()

# Item3 = Item(user_id=1, name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
#                      price="$6.50",  category=category1)

# session.add(Item3)
# session.commit()

# Item4 = Item(user_id=1, name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
#                      price="$6.75",  category=category1)

# session.add(Item4)
# session.commit()

# Item2 = Item(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
#                      price="$7.00", category=category1)

# session.add(Item2)
# session.commit()


# # Menu for Auntie Ann's
# category1 = category(user_id=1, name="Auntie Ann\'s Diner' ")

# session.add(category1)
# session.commit()

# Item9 = Item(user_id=1, name="Chicken Fried Steak",
# description="Fresh battered sirloin steak fried and smothered with cream
# gravy", price="$8.99", category=category1)

# session.add(Item9)
# session.commit()


# Item1 = Item(user_id=1, name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
#                      price="$2.99", category=category1)

# session.add(Item1)
# session.commit()

# Item2 = Item(user_id=1, name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
#                      price="$10.95", category=category1)

# session.add(Item2)
# session.commit()

# Item3 = Item(user_id=1, name="Morels on toast (seasonal)",
# description="Wild morel mushrooms fried in butter, served on herbed
# toast slices", price="$7.50",  category=category1)

# session.add(Item3)
# session.commit()

# Item4 = Item(user_id=1, name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
#                      price="$8.95", category=category1)

# session.add(Item4)
# session.commit()

# Item2 = Item(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
#                      price="$9.50", category=category1)

# session.add(Item2)
# session.commit()

# Item10 = Item(user_id=1, name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
#                       price="$1.99", category=category1)

# session.add(Item10)
# session.commit()


# # Menu for Cocina Y Amor
# category1 = category(user_id=1, name="Cocina Y Amor ")

# session.add(category1)
# session.commit()


# Item1 = Item(user_id=1, name="Super Burrito Al Pastor",
# description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa,
# Tortilla", price="$5.95", category=category1)

# session.add(Item1)
# session.commit()

# Item2 = Item(user_id=1, name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
#                      price="$7.99", category=category1)

# session.add(Item2)
# session.commit()


# category1 = category(user_id=1, name="State Bird Provisions")
# session.add(category1)
# session.commit()

# Item1 = Item(user_id=1, name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
#                      price="$5.95",  category=category1)

# session.add(Item1)
# session.commit

# Item1 = Item(user_id=1, name="Guanciale Chawanmushi",
# description="Japanese egg custard served hot with spicey Italian Pork
# Jowl (guanciale)", price="$6.95", category=category1)

# session.add(Item1)
# session.commit()


# Item1 = Item(user_id=1, name="Lemon Curd Ice Cream Sandwich",
# description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with
# cardamom meringue and cashews", price="$4.25", category=category1)

# session.add(Item1)
# session.commit()


print "added items!"
