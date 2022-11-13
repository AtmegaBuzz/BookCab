from backend import create_app


def test_login_page():
    """
        Given  a Flask application configured for tesing 
        WHEN the auth/login page is requested (GET)
        THEN check if the response is contains email and password fields

        WHEN the auth/register page is requested (POST)
        THEN check if the user is created 
    """

    flask_app = create_app(testing=True)

    with flask_app.test_client() as test_client:

        response = test_client.get('/auth/login')

        assert response.status_code == 200 
        assert b'Login' in response.data
        assert b'Email' in response.data
        assert b'Password' in response.data


