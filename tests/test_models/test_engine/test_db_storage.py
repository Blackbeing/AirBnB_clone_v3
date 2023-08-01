#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import pep8
import unittest

DBStorage = db_storage.DBStorage
classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(["models/engine/db_storage.py"])
        self.assertEqual(
            result.total_errors,
            0,
            "Found code style errors (and warnings).",
        )

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(
            [
                "tests/test_models/test_engine/\
test_db_storage.py"
            ]
        )
        self.assertEqual(
            result.total_errors,
            0,
            "Found code style errors (and warnings).",
        )

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(
            db_storage.__doc__, None, "db_storage.py needs a docstring"
        )
        self.assertTrue(
            len(db_storage.__doc__) >= 1, "db_storage.py needs a docstring"
        )

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(
            DBStorage.__doc__, None, "DBStorage class needs a docstring"
        )
        self.assertTrue(
            len(DBStorage.__doc__) >= 1, "DBStorage class needs a docstring"
        )

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(
                func[1].__doc__,
                None,
                "{:s} method needs a docstring".format(func[0]),
            )
            self.assertTrue(
                len(func[1].__doc__) >= 1,
                "{:s} method needs a docstring".format(func[0]),
            )


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    @unittest.skipIf(models.storage_t != "db", "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != "db", "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""
        # for k in classes:
        models.storage.new(State(name="Test State"))
        models.storage.new(
            User(name="Test User", email="Test Email", password="pass")
        )
        models.storage.save()
        klasses = {k.__class__.__name__ for k in models.storage.all().values()}
        self.assertTrue(all(klass in klasses for klass in ["User", "State"]))

    @unittest.skipIf(models.storage_t != "db", "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database session"""
        models.storage.new(State(name="Test State"))
        models.storage.new(State(name="Test State2"))
        self.assertEqual(len(models.storage._DBStorage__session.new), 2)

    @unittest.skipIf(models.storage_t != "db", "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to databse"""

        before = len(models.storage.all())
        models.storage.new(State(name="Test State"))
        models.storage.new(State(name="Test State2"))
        models.storage.save()
        after = len(models.storage.all())
        self.assertTrue(after > before)
        self.assertEqual(after - before, 2)

    @unittest.skipIf(models.storage_t != "db", "not testing db storage")
    def test_get(self):
        """Test that get gets object based on object class and id"""

        new_state1 = State(name="State1")
        new_state2 = State(name="State2")
        [models.storage.new(s) for s in [new_state1, new_state2]]
        models.storage.save()
        get_value = models.storage.get(State, new_state2.id)
        self.assertIs(new_state2, get_value)
        # Test get using id with wroing class
        get_value = models.storage.get(User, new_state2.id)
        self.assertIsNone(get_value)

        get_value = models.storage.get(State, "random_id")
        self.assertIsNone(get_value)

    @unittest.skipIf(models.storage_t != "db", "not testing db storage")
    def test_count(self):
        """Test that count returns number of class object"""
        city1 = City()
        city2 = City()
        place1 = Place()
        place2 = Place()
        base1 = BaseModel()
        review = Review()

        objs = [city1, city2, place1, place2, base1, review]

        for obj in objs :
            models.storage.new(obj)

        self.assertIsEqual(models.storage.count(), 6)
        self.assertIsEqual(models.storage.count(City), 2)
        self.assertIsEqual(models.storage.count(Place), 2)
        self.assertIsEqual(models.storage.count(BaseModel), 1)
        self.assertIsEqual(models.storage.count(Review), 1)
        self.assertIsInstance(models.storage.count(), int)
