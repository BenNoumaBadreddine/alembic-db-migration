# alembic db migration
alembic db migration template

## Alembic utilities:
### Why alembic:

* Easier to maintain multiple database environments.
* Easier to set up local environment for developers.
* Easier to migrate schemas from one database to another
* No complex SQL statements
* Easily integrable with CI-CD
* No need to share credentials with developers

### What is alembic?

* Alembic is a lightweight database schema migration tool for usage with SQLAlchemy Database toolkit for python.
* Provides both upgrade and rollback functionality
* Easy to use python friendly way
* Alembic works by managing change management scripts by maintaining the ID of the last revision in the database.
### General directory structure
    database-schema-migration ---------> demo_db ---------> test_schema
                                                 ---------> test_schema_1
                              ---------> demo_1_db ---------> schema1
                                                   ---------> schema2


## Get started
### Create database migration project folder:
We create a folder, and we name it, for example: database-schema-migration

Open a terminal and _cd_ to the project directory then write:
```bash
  mkdir database-schema-migration
```
### Create two files:
* environment.yaml : this file will be used to create the virtual environment
* readme.md : this file will describe how and why to use this alembic.

### Create the virtual environment:
```bash
  cd database-schema-migration
  conda env create -f environment.yml 
  conda activate database-schema-migration
```
### Create a folder for each database and cd that folder, for example:
```bash
  mkdir demo_db
  cd demo_db
```
### init alembic
After cd the database folder, execute the ```init alembic``` for each database schema, for example:
```bash
  alembic init test_schema
```
![img.png](images/db_schemas.png)

After executing init command few files (alembic.ini) and folder (test_schema) are created inside the demo_db folder.
        
        demo_db/test_schema ...  done
        demo_db/test_schema/versions ...  done
        demo_db/test_schema/script.py.mako ...  done
        demo_db/test_schema/env.py ...  done
        demo_db/test_schema/README ...  done
        demo_db/alembic.ini ...  done

### Add db_base folder
Add ```db_bases``` folder. That folder has two main files: ```base.py``` and ```base_class.py```.
### Create database credentials file
Create ```demo_db_config.py``` file. That file will have the credentials to your database.
### modify file content
Modify the 'env.py':
* Add ```get_url``` function
* Modify ```run_migrations_offline``` by specifying:
``` python
    url=get_url(),
```
* Add the target metadata 
``` python
from base import DemoBase
target_metadata = DemoBase.metadata
```
* modify ```run_migrations_online``` by specifying:

``` python
print(f'Starting online migration ...')
configuration = config.get_section(config.config_ini_section)
print(f'ini configuration {configuration}')
configuration["sqlalchemy.url"] = get_url()
print(f'After modification of ini configuration {configuration}')
connectable = engine_from_config(
       configuration,
       prefix="sqlalchemy.",
       poolclass=pool.NullPool,)
```


### create revision
```bash
  alembic revision -m "create test schema"
```
### Modify file content

Modify the file ```4cb84c335871_create_test_schema.py```: modify ```upgrade``` and ```downgrade``` by 
adding your SQL statement.

### alembic upgrades
```sh
    alembic upgrade head --sql
or
    alembic upgrade head
```

![img.png](images/alembic_upgrade_sh_execution.png)

### alembic downgrade
```sh
    alembic downgrade -1
```

![img.png](images/alembic_downgrade_sh_execution.png)