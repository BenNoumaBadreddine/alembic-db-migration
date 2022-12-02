# Import all the orm, so that Base has them before being
# imported by Alembic
from base_class import NpmLogBase
import sys
sys.path.insert(0, '/Users/badr/github_projects/common-codes')
from databases_util.databases_schema.db_dbname_schema import *  # noqa
