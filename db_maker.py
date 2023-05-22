from datetime import datetime
from app import db, app
from app.models import Review, Property, House, Halls, EstateAgent, User

with app.app_context():
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
        lat=51.49,
        lng=-3.18,
        address="123 Main St"
    )

    property2 = Property(
        lat=51.48,
        lng=-3.17,
        address="456 Elm St"
    )

    property3 = Property(
        lat=51.4967629,
        lng=-3.1971658,
        address="Talybont South"
    )

    property4 = Property(
        lat=51.4858228,
        lng=-3.1723673,
        address="Senghennydd Court"
    )

    property5 = Property(
        lat=51.49181986467401,
        lng=-3.185855195185478,
        address="Aberconway Hall"
    )

    property6 = Property(
        lat=51.48911313048784,
        lng=-3.1838519077663965,
        address="Aberdare Hall"
    )

    property7 = Property(
        lat=51.48076023130313,
        lng=-3.1657288496028064,
        address="Adam Street Gardens"
    )

    property8 = Property(
        lat=51.49750794691082,
        lng=-3.174525130331824,
        address="Cartwright Court"
    )

    property9 = Property(
        lat=51.50427489262149,
        lng=-3.1840767045009524,
        address="Clodien House"
    )

    property10 = Property(
        lat=51.49150917424132,
        lng=-3.1866835266264557,
        address="Colum Hall"
    )

    property11 = Property(
        lat=51.48685458791538,
        lng=-3.1708970597283526,
        address="Gordon Hall"
    )

    property12 = Property(
        lat=51.490742640482644,
        lng=-3.177956727966567,
        address="Hodge Hall"
    )

    property13 = Property(
        lat=51.495507674603935,
        lng=-3.17865270699747,
        address="Roy Jenkins Hall"
    )

    property14 = Property(
        lat=51.486328699297175,
        lng=-3.173701264781204,
        address="Senghennydd Hall"
    )

    property15 = Property(
        lat=51.49130849578401,
        lng=-3.185648980077052,
        address="Student Houses (Colum Road/Place)"
    )

    property16 = Property(
        lat=51.48863414176451,
        lng=-3.1759052969870987,
        address="Student Houses (Village)"
    )

    property17 = Property(
        lat=51.49446523907291,
        lng=-3.1911491294088616,
        address="Talybont Court"
    )

    property18 = Property(
        lat=51.49895159552787,
        lng=-3.2012141761878095,
        address="Talybont Gate"
    )

    property19 = Property(
        lat=51.4991788202768,
        lng=-3.1985997256895624,
        address="Talybont North"
    )

    property20 = Property(
        lat=51.504909686036314,
        lng=-3.1669502574258854,
        address="University Hall"
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

    talybont_south = Halls(
        property_id=3,
        rent=61819
    )

    senghennydd_court = Halls(
        property_id=4,
        rent=53356
    )

    aberconway_hall = Halls(
        property_id=5,
        rent=57724
    )

    aberdare_hall = Halls(
        property_id=6,
        rent=53356
    )

    adam_street_gardens = Halls(
        property_id=7,
        rent=69333
    )

    cartwright_court = Halls(
        property_id=8,
        rent=53356
    )

    clodien_house = Halls(
        property_id=9,
        rent=68033
    )

    colum_hall = Halls(
        property_id=10,
        rent=61819
    )

    gordon_hall = Halls(
        property_id=11,
        rent=60575
    )

    hodge_hall = Halls(
        property_id=12,
        rent=57724
    )

    roy_jenkins_hall = Halls(
        property_id=13,
        rent=53356
    )

    senghennydd_hall = Halls(
        property_id=14,
        rent=69342
    )

    student_houses_colum = Halls(
        property_id=15,
        rent=48958
    )

    student_houses_village = Halls(
        property_id=16,
        rent=48958
    )

    talybont_court = Halls(
        property_id=17,
        rent=62759
    )

    talybont_gate = Halls(
        property_id=18,
        rent=62759
    )

    talybont_north = Halls(
        property_id=19,
        rent=53356
    )

    university_hall = Halls(
        property_id=20,
        rent=53356
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

    db.session.add_all([review1, review2, 
                        property1, property2, property3, property4, property5, property6, property7, property8, property9, property10, property11, property12, property13, property14, property15, property16, property17, property18, property19, property20,
                        house1, house2, 
                        talybont_south, senghennydd_court, aberconway_hall, aberdare_hall, adam_street_gardens, cartwright_court, clodien_house, colum_hall, gordon_hall, hodge_hall, roy_jenkins_hall, senghennydd_hall, student_houses_colum, student_houses_village, talybont_court, talybont_gate, talybont_north, university_hall,
                        estate_agent1, estate_agent2, 
                        user1, user2])
    db.session.commit()