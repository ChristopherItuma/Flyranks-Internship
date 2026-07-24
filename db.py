from sqlmodel import SQLModel, Field, create_engine, Session

#Create a table schema for the database

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    done: bool = Field(default=False)


# configure the database connection and create the tables
sqlite_file_name = "tasks.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

# Create the database tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

#insert 3 sample tasks only when the database is empty
def insert_sample_tasks():
    with Session(engine) as session:
        task_count = session.query(Task).count()
        if task_count == 0:
            sample_tasks = [
                Task(title="Buy groceries"),
                Task(title="Clean the house"),
                Task(title="Submit the assignment")
            ]
            session.add_all(sample_tasks)
            session.commit()

#get all tasks from the database
def get_all_tasks():
    with Session(engine) as session:
        tasks = session.query(Task).all()
        return tasks

# get single task by id
def get_task_by_id(task_id: int):
    with Session(engine) as session:
        task = session.query(Task).filter(Task.id == task_id).first()
        return task