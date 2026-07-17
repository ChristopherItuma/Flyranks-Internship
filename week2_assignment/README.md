# Task API

## What this is

This project is a small FastAPI application that exposes a simple task management API. It lets you list tasks, retrieve a task by ID, create a new task, update an existing task, and delete a task.

## Install and run

Use the following one-line command from the project folder to install the required packages and start the API:

```bash
pip install fastapi uvicorn && uvicorn main:app --reload
```

Once the server starts, open the Swagger UI at:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | Returns API metadata and available endpoints |
| GET | `/health` | Returns the health status of the API |
| GET | `/tasks` | Returns all tasks |
| GET | `/tasks/{task_id}` | Returns a single task by its ID |
| POST | `/tasks` | Creates a new task |
| PUT | `/tasks/{task_id}` | Updates an existing task |
| DELETE | `/tasks/{task_id}` | Deletes a task by its ID |

## Example `curl -i` output

```bash
curl -i http://127.0.0.1:8000/tasks/999
```

```text
HTTP/1.1 404 Not Found
content-type: application/json

{"detail":"Task not found"}
```

## Swagger screenshot

C:\Users\CHRIS\Desktop\flyranks_internship\week2_assignment\screenshot.png
