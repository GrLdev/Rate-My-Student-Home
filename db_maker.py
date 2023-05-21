from datetime import datetime
from app import db
from app.models import Review, Property, House, Halls, EstateAgent, User

db.drop_all()
db.create_all()

review1 = Review(
    user_id=1,
    property_id=1,
    estate_agent_id=1,
    overall_rating=4,
    condition_rating=5,
    security_rating=3,
    landlord_rating=4,
    date=datetime.now(),
    comment="Great experience!"
)

review2 = Review(
    user_id=2,
    property_id=2,
    estate_agent_id=1,
    overall_rating=3,
    condition_rating=4,
    security_rating=2,
    landlord_rating=3,
    date=datetime.now(),
    comment="Could be better."
)

property1 = Property(
    place_id="123abc",
    address="123 Main St"
)

property2 = Property(
    place_id="456def",
    address="456 Elm St"
)

house1 = House(
    property_id=1,
    bedrooms=3,
    bathrooms=2,
    rent=1500
)

house2 = House(
    property_id=2,
    bedrooms=4,
    bathrooms=3,
    rent=2000
)

halls1 = Halls(
    property_id=1,
    rent=1000
)

halls2 = Halls(
    property_id=2,
    rent=1200
)

estate_agent1 = EstateAgent(
    name="ABC Realty",
    email="abc@example.com",
    phone="123-456-7890",
    website="http://www.abc-realty.com"
)

estate_agent2 = EstateAgent(
    name="XYZ Properties",
    email="xyz@example.com",
    phone="987-654-3210",
    website="http://www.xyz-properties.com"
)

user1 = User(
    name="John Doe",
    email="john@example.com",
    university="University of ABC"
)

user2 = User(
    name="Jane Smith",
    email="jane@example.com",
    university="University of XYZ"
)

db.session.add_all([review1, review2, property1, property2, house1, house2, halls1, halls2, estate_agent1, estate_agent2, user1, user2])
db.session.commit()