from unittest import main, TestCase

from sqlalchemy import Column, String, select, inspect

from opticon.database.handler import db


class TestModel(db.BaseModel):
    __comment__ = 'Test table.'
    name = Column(String(8))


class ModelTest(TestCase):

    def test_table_args(self):
        self.assertDictEqual(
            {
                'comment': 'Test table.',
                'mysql_engine': 'innodb',
                'mysql_charset': 'utf8mb4',
            }, TestModel.__table_args__[0])


class HandlerTest(TestCase):

    def test_create_and_drop_all(self):
        inspector = inspect(db.engine)
        self.assertFalse(inspector.has_table('test_model'))
        db.create_all()
        self.assertTrue(inspector.has_table('test_model'))
        db.drop_all()
        self.assertFalse(inspector.has_table('test_model'))

    def test_add(self):
        db.create_all()

        with db.session_scope() as session:
            session.add(TestModel(name='Very Cool'))
            session.commit()

        with db.session_scope() as session:
            query = select(TestModel)
            result: TestModel = session.scalars(query).one()
        self.assertEqual('Very Cool', result.name)

        db.drop_all()


if __name__ == '__main__':
    main()
