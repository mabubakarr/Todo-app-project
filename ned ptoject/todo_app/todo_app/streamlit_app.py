# streamlit_app.py
import streamlit as st
import requests

API_URL = "http://web:8000/todos/"

def get_todos():
    response = requests.get(API_URL)
    return response.json()

def create_todo():
    title = st.text_input("Title")
    description = st.text_area("Description")
    if st.button("Add Todo"):
        todo = {"title": title, "description": description}
        response = requests.post(API_URL, json=todo)
        if response.status_code == 200:
            st.success("Todo added successfully!")
        else:
            st.error("Error adding todo")

def update_todo():
    todos = get_todos()
    todo_ids = [todo['id'] for todo in todos]
    todo_id = st.selectbox("Select Todo to Update", todo_ids)
    todo = next(todo for todo in todos if todo["id"] == todo_id)
    title = st.text_input("Title", value=todo["title"])
    description = st.text_area("Description", value=todo["description"])
    completed = st.checkbox("Completed", value=todo["completed"])
    if st.button("Update Todo"):
        updated_todo = {"title": title, "description": description, "completed": completed}
        response = requests.put(f"{API_URL}{todo_id}", json=updated_todo)
        if response.status_code == 200:
            st.success("Todo updated successfully!")
        else:
            st.error("Error updating todo")

def delete_todo():
    todos = get_todos()
    todo_ids = [todo['id'] for todo in todos]
    todo_id = st.selectbox("Select Todo to Delete", todo_ids)
    if st.button("Delete Todo"):
        response = requests.delete(f"{API_URL}{todo_id}")
        if response.status_code == 200:
            st.success("Todo deleted successfully!")
        else:
            st.error("Error deleting todo")

st.title("ToDo App")
option = st.selectbox("Choose an action", ["Add Todo", "Update Todo", "Delete Todo", "View Todos"])

if option == "Add Todo":
    create_todo()
elif option == "Update Todo":
    update_todo()
elif option == "Delete Todo":
    delete_todo()
elif option == "View Todos":
    todos = get_todos()
    for todo in todos:
        st.write(todo)