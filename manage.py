from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from employee_directory_flask import db, prepare_app
from employee_directory_flask import parser
from employee_directory_flask.models import Employee

app = prepare_app()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import sys
    import unittest

    prepare_app(environment='testing')
    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    test_result = unittest.TextTestRunner(verbosity=2).run(tests)

    if not test_result.wasSuccessful():
        sys.exit(1)


@manager.command
def dbseed():
    Employee.query.delete()
    json_data = open('employees.json').read()
    employees = parser.parse(json_data)
    for employee in employees:
        db.session.add(employee)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
