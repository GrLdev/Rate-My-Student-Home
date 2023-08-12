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
        comment="Great experience!",
        rent=1500
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
        comment="Could be better.",
        rent=2000
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

    cps_roath = EstateAgent(
        name="CPS Homes Roath",
        email="roath@cpshomes.co.uk",
        phone="029-2045-4555",
        website="https://www.cpshomes.co.uk/"
    )

    cps_cathays = EstateAgent(
        name="CPS Homes Cathays",
        email="enquiries@cpshomes.co.uk",
        phone="029-2066-8585",
        website="https://www.cpshomes.co.uk/"
    )

    john_winter = EstateAgent(
        name="John Winter Student Houses",
        email="info@johnwinterhouses.co.uk",
        phone="02920-228-777",
        website="https://johnwinterhouses.co.uk/"
    )

    cardiff_student_letting = EstateAgent(
        name="Cardiff Student Letting",
        email="info@cardiffstudentletting.com",
        phone="02920-781525",
        website="https://www.cardiffstudentletting.com/"
    )

    savills = EstateAgent(
        name="Savills",
        email="westend@savills.com",
        phone="02920-368-900 ",
        website="https://www.savills.co.uk/"
    )

    kingstons = EstateAgent(
        name="Kingstons",
        email="lettings@kingstonscardiff.co.uk",
        phone="029-20409999",
        website="https://www.kingstonscardiff.co.uk/"
    )

    jeffreyross = EstateAgent(
        name="Jeffrey Ross",
        email="info@jeffreyross.co.uk",
        phone="029-2049-9680",
        website="https://www.jeffreyross.co.uk/"
    )

    uniek_residential = EstateAgent(
        name="Uniek Residential",
        email="info@uniekresidential.co.uk",
        phone="029-2022-9357",
        website="https://www.uniekresidential.co.uk/"
    )

    horizon_properties = EstateAgent(
        name="Horizon Properties",
        email="enquiries@horizonproperties.org.uk",
        phone="02920342299",
        website="https://www.horizonproperties.org.uk/"
    )

    james_douglas = EstateAgent(
        name="James Douglas",
        email="info@james-douglas.co.uk",
        phone="02920-456-444",
        website="https://www.james-douglas.co.uk/"
    )

    the_living_room = EstateAgent(
        name="The Living Room Letting Agency",
        email="cardiff@tlrestates.co.uk",
        phone="02920-341077",
        website="https://tlrestates.co.uk/"
    )

    velvet_chase = EstateAgent(
        name="Velvet Chase",
        email="lettings@velvetchase.co.uk",
        phone="029-21992-199",
        website="https://www.velvetchase.co.uk/"
    )

    harry_harper = EstateAgent(
        name="Harry Harper",
        email="info@harryharper.co.uk",
        phone="029-2031-0555",
        website="https://www.harryharper.co.uk/"
    )

    property_direct = EstateAgent(
        name="Property Direct",
        email="info@propertydirectltd.com",
        phone="029-2025-5632",
        website="https://www.propertydirectltd.com/"
    )

    allen_and_harris = EstateAgent(
        name="Allen and Harris Roath",
        email="roath@allenandharris.co.uk",
        phone="029-2046-4744",
        website="https://www.allenandharris.co.uk/estate-agents/roath-cardiff"
    )

    albany_property_services = EstateAgent(
        name="Albany Property Services",
        email="info@albanyproperties.co.uk",
        phone="029-2021-1081",
        website="https://albanypropertyservices.biz/"
    )

    jupiter_property = EstateAgent(
        name="Jupiter Property",
        email="enquiries@jupiter.co.uk",
        phone="029-2066-6623",
        website="https://www.jupiter.co.uk/"
    )

    darlows_albany_road = EstateAgent(
        name="Darlows Albany Road",
        email="albany.road@darlows.co.uk",
        phone="029-2233-8551",
        website="https://www.darlows.co.uk/"
    )

    moginie_james = EstateAgent(
        name="Moginie James",
        email="info@moginiejames.co.uk",
        phone="029-2076-1999",
        website="https://www.moginiejames.co.uk/"
    )

    martin_and_co = EstateAgent(
        name="Martin and Co",
        email="cardiff@martinco.com",
        phone="029-2048-2250",
        website="https://www.martinco.com/"
    )

    let2 = EstateAgent(
        name="2let2",
        email="enquiries@2let2.com",
        phone="029-2022-6222",
        website="https://www.2let2.com/"
    )

    interlet = EstateAgent(
        name="Interlet",
        email="lettings@interletresidential.co.uk",
        phone="02920400000",
        website="https://www.interletgroup.com/"
    )

    amos_estate = EstateAgent(
        name="Amos Estate Agents",
        email="info@amosproperties.co.uk",
        phone="029-22520191",
        website="https://amosproperties.co.uk/"
    )

    isla_alexander = EstateAgent(
        name="Isla Alexander Property",
        email="info@isla-alexander.com",
        phone="0800-058-4488",
        website="https://www.isla-alexander.com/"
    )

    lettings_angels = EstateAgent(
        name="Sales and Lettings Angels",
        email="info@lettingsangels.co.uk",
        phone="029-2233-1425",
        website="https://salesandlettingsangels.co.uk/"
    )

    FourLet = EstateAgent(
        name="4Let",
        email="info@4let.co.uk",
        phone="029-2066-5270",
        website="https://www.4let.co.uk/"
    )

    david_ricketts = EstateAgent(
        name="David Ricketts",
        email="rickettsnco@gmail.com",
        phone="07544-502428",
        website="https://www.davidricketts.co.uk/"
    )

    jnr = EstateAgent(
        name="JNR Properties",
        email="jnr@jnrproperties.co.uk",
        phone="029-2000-2420",
        website="https://www.jnrproperties.co.uk/"
    )

    st_michael_angel = EstateAgent(
        name="St Michael Angel",
        email="joe@stmichaelangelestate.co.uk",
        phone="02920254077",
        website="https://www.stmichaelangelestate.co.uk/"
    )

    peter_mulcahy = EstateAgent(
        name="Peter Mulcahy Estate",
        email="albany@petermulcahy.co.uk",
        phone="029-2049-6452",
        website="https://www.petermulcahy.co.uk/"
    )

    ashi = EstateAgent(
        name="Ashi Properties",
        email="sales@ashiproperties.co.uk",
        phone="029-2034-3430",
        website="https://www.ashiproperties.co.uk/"
    )

    umbrella_homes = EstateAgent(
        name="The Umbrella Homes Limited",
        email="info@theumbrellahomes.co.uk",
        phone="029-2023-0338",
        website="https://www.theumbrellahomes.co.uk/"
    )

    abraham_estates = EstateAgent(
        name="Abraham Estates",
        email="info@abrahamestates.com",
        phone="02920-377226",
        website="https://www.abrahamestates.com/"
    )

    peter_alan = EstateAgent(
        name="Peter Alan Estates",
        email="enquiries@peteralan.co.uk",
        phone="0330-333-4971",
        website="https://www.peteralan.co.uk/"
    )
        
    hensons_homes = EstateAgent(
        name="Hensons Homes",
        email="info@hensonshomes.com",
        phone="02921158696",
        website="https://www.hensonshomes.com/"
    )

    prestige = EstateAgent(
        name="Prestige Lettings",
        email="info@prestigecardiff.co.uk",
        phone="02920-343-865",
        website="https://www.prestigecardiff.co.uk/"
    )

    bah_properties = EstateAgent(
        name="Bah Properties",
        email="info@bahproperties.co.uk",
        phone="029-2240-8022",
        website="https://www.bahproperties.co.uk/"
    )

    imperial_services = EstateAgent(
        name="Imperial Services",
        email="info@imperialservices.co.uk",
        phone="02920303040",
        website="https://www.imperialservices.co.uk/"
    )

    providing_properties = EstateAgent(
        name="Providing Properties",
        email="info@providingproperties.co.uk",
        phone="029-2039-9271",
        website="https://www.providingproperties.co.uk/"
    )

    keylet = EstateAgent(
        name="Keylet",
        email="lettings@keylet.co.uk",
        phone="02920-388399",
        website="https://www.keylet.co.uk/"
    )

    unihomes = EstateAgent(
        name="Unihomes",
        email="hello@unihomes.co.uk",
        phone="0330-822-0266",
        website="https://www.unihomes.co.uk/"
    )

    student_cribs = EstateAgent(
        name="Student Cribs",
        email="customerservice@student-cribs.com",
        phone="0203-758-7000",
        website="https://student-cribs.com/"
    )

    unite_students = EstateAgent(
        name="Unite Students",
        email="customerservices@unitestudents.com",
        phone="0300-303-8642 ",
        website="https://www.unitestudents.com/"
    )

    crm_students = EstateAgent(
        name="CRM Students",
        email="info@crm-students.com",
        phone="02921-040198",
        website="https://www.crm-students.com/"
    )

    collegiate = EstateAgent(
        name="Collegiate",
        email="customerservice@collegiate-ac.com",
        phone="029-2104-0601",
        website="https://www.collegiate-ac.com/"
    )

    herestudents = EstateAgent(
        name="Here Students",
        email="",
        phone="",
        website="https://www.herestudents.com/"
    )

    yugo = EstateAgent(
        name="Yugo",
        email="info@yugo.com",
        phone="02921-040580",
        website="https://www.yugo.co.uk/"
    )

    hellostudent = EstateAgent(
        name="Hello Student",
        email="questions@hellostudent.co.uk",
        phone="02038288700",
        website="https://www.hellostudent.co.uk/"
    )

    vita_student = EstateAgent(
        name="Vita Student",
        email="hello@vitastudent.com",
        phone="0203-096-1717",
        website="https://www.vitastudent.com/"
    )

    prime_student_living = EstateAgent(
        name="Prime Student Living",
        email="howardgardens@primestudentliving.com",
        phone="029-2012-7850",
        website="https://www.primestudentliving.com/"
    )

    thisisfresh = EstateAgent(
        name="This is Fresh",
        email="bridgestreetexchange@thisisfresh.com",
        phone="02920-105655",
        website="https://www.thisisfresh.com/"
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
                        cps_roath, cps_cathays, john_winter, cardiff_student_letting, savills, kingstons, jeffreyross, uniek_residential, horizon_properties, james_douglas, the_living_room, velvet_chase, harry_harper, property_direct, allen_and_harris, albany_property_services, jupiter_property, darlows_albany_road, moginie_james, martin_and_co, let2, interlet, amos_estate, isla_alexander, lettings_angels, FourLet, david_ricketts, jnr, st_michael_angel, peter_mulcahy, ashi, umbrella_homes, abraham_estates, peter_alan, hensons_homes, prestige, bah_properties, imperial_services, providing_properties, keylet, unihomes, student_cribs, unite_students, crm_students, collegiate, herestudents, yugo, hellostudent, vita_student, prime_student_living, thisisfresh,
                        user1, user2])
    db.session.commit()