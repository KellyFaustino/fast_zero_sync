from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='Kelly', email='kelly@teste.com', password='123')

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'kelly@teste.com')
    )

    assert result.username == 'Kelly'
    assert result.email == 'kelly@teste.com'
