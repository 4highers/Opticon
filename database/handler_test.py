from unittest import main, TestCase

from sqlalchemy import Column, Integer, String, select, inspect

from database.handler import db


class TestModel(db.BaseModel):
    __tablename__ = 'test_table'
    __table_args__ = db.default_table_args('Test table.')
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(8))


class HandlerTest(TestCase):

    def test_create_and_drop_all(self):
        inspector = inspect(db._engine)
        self.assertFalse(inspector.has_table('test_table'))
        db.create_all()
        self.assertTrue(inspector.has_table('test_table'))
        db.drop_all()
        self.assertFalse(inspector.has_table('test_table'))

    def test_add(self):
        db.create_all()

        with db.session_scope() as session:
            session.add(TestModel(name="Very Cool"))
            session.commit()

        with db.session_scope() as session:
            query = select(TestModel)
            result: TestModel = session.scalars(query).one()
        self.assertEqual('Very Cool', result.name)

        db.drop_all()


if __name__ == '__main__':
    main()
