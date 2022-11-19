# Migrations
    
    In order to manage the model migrations using alembic, it is required to import the model file into `store/migrations/env.py`, somesthing like:

    ```python
    from app.models import products
    ```

    After that, if the data model changed it is required to generate the migration file using something like:

    ```
        make db-migrate MESSAGE="define product table"
    ```

    Last, to upgrade the database definition to the last version it is required to execute:

    ```
        make db-upgrade
    ```