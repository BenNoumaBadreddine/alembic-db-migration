# Import all the orm, so that Base has them before being
# imported by Alembic
import sys
sys.path.insert(0, '/Users/badr/github_projects/common-codes')
from src.src.databases_util.databases_schema import *  # noqa
