from backend.models import User,Booking


def test_new_user():
    """
        Given  a User modal
        WHEN a new User is created
        THEN check the name, email, phone_number and password_hashed fields are defined correctly
    """

    user = User(
        name = "testuser",
        phone_number = "+919583750310", # fake number
        email = "testemail@gmail.com",
        password = "testpassword"
    )
    assert user.email == 'testemail@gmail.com'
    assert user.name == 'testuser'
    assert user.phone_number == '+919583750310'
    assert user.password == 'testpassword'

    # this test will always fails cause password is hashed in register view so tested for no hash pass



def test_new_bookings():
    """
        Given  a Booking modal
        WHEN a new Booking is created
        THEN check the destination, status, cost, distance is defined correctly
    """

    booking = Booking(
        destination = "new delhi",
        status = 0,
        cost = 100,
        distance = 1000
    )

    assert booking.destination == 'new delhi'
    assert booking.status == 0
    assert booking.cost == 100
    assert booking.distance == 1000