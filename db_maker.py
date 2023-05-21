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
        place_id="123abc",
        address="123 Main St"
    )

    property2 = Property(
        place_id="456def",
        address="456 Elm St"
    )

    property3 = Property(
        place_id="ChIJH2NCFZ4cbkgRPSlOcvlFOQY",
        address="Talybont South"
    )

    property4 = Property(
        place_id="ChIJY120gL8cbkgReH6",
        address="Senghennydd Court"
    )

    property5 = Property(
        place_id="ChIJFX0bYKIcbkgRNkB9Gp5GFzU",
        address="Aberconway Hall"
    )

    property6 = Property(
        place_id="ChIJH2NCFZ4cbkgRPSlOcvlFOQY",
        address="Aberdare Hall"
    )

    property7 = Property(
        place_id="ChIJVVVV_MgcbkgRab4VyaKDbfI",
        address="Adam Street Gardens"
    )

    property8 = Property(
        place_id="Eh9DYXJ0d3JpZ2h0IEN0LCBDYXJkaWZmIENGMjQsIFVLIi4qLAoUChIJPcb1epQcbkgR2PTuMAxz-rQSFAoSCaVT1up7G25IEcFvu1PUINsQ",
        address="Cartwright Court"
    )

    property9 = Property(
        place_id="ChIJxVKK-Y8cbkgRr99rDdP-e0M",
        address="Clodien House"
    )

    property10 = Property(
        place_id="ChIJmwp6gQYdbkgRHoE22rLIMk0",
        address="Colum Hall"
    )

    property11 = Property(
        place_id="ChIJm6qyorgcbkgRAtERHigpBK0",
        address="Gordon Hall"
    )

    property12 = Property(
        place_id="ChIJeabKs70cbkgRQfJboTxGGY0", 
        address="Hodge Hall"
    )

    property13 = Property(
        place_id="ChIJqcS7530dbkgR5Y654y9ZjgE",
        address="Roy Jenkins Hall"
    )

    property14 = Property(
        place_id="ChIJ1T-7G7kcbkgRannku9nn1lY",
        address="Senghennydd Hall"
    )

    property15 = Property(
        place_id="ChIJi3bs86IcbkgR4m4GXg16tsg",
        address="Student Houses (Colum Road/Place)"
    )

    property16 = Property(
        place_id="EiZMbGFuYmxlZGRpYW4gR2FyZGVucywgQ2FyZGlmZiBDRjI0LCBVSyIuKiwKFAoSCYd66qW-HG5IEXwVlE7EUgvvEhQKEgmlU9bqextuSBHBb7tT1CDbEA",
        address="Student Houses (Village)"
    )

    property17 = Property(
        place_id="ChIJoSyzG58cbkgREaQDN19DTPI",
        address="Talybont Court"
    )

    property18 = Property(
        place_id="ChIJnakuk2MbbkgRq1PH8zLU61c",
        address="Talybont Gate"
    )

    property19 = Property(
        place_id="ChIJuaxNQhkbbkgRs---OHJgm4Q",
        address="Talybont North"
    )

    property20 = Property(
        place_id="ChIJg-W_9fEcbkgRsJuankMUpDo",
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
                        property1, property2, property3, property4, property5, property6, property7, property8, 
                        property9, property10, property11, property12, property13, property14, property15, property16, property17, property18, property19, property20,
                        house1, house2, 
                        talybont_south, senghennydd_court, aberconway_hall, aberdare_hall, adam_street_gardens, cartwright_court, 
                        clodien_house, colum_hall, gordon_hall, hodge_hall, roy_jenkins_hall, senghennydd_hall, student_houses_colum, student_houses_village, talybont_court, talybont_gate, talybont_north, university_hall,
                        estate_agent1, estate_agent2, 
                        user1, user2])
    db.session.commit()