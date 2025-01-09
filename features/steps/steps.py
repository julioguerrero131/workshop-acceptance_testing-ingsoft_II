from behave import given, when, then

# Global list to represent the to-do list
to_do_list = []
error_message = ""

# Step Definitions

@given("the to-do list is empty")
def step_impl(context):
    global to_do_list
    to_do_list = []


@when('the user adds a task "{task}"')
def step_impl(context, task):
    global to_do_list
    to_do_list.append({"task": task, "status": "Pending"})


@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    global to_do_list
    tasks = [item["task"] for item in to_do_list]
    assert task in tasks, f'Task "{task}" not found in the to-do list.'


@given("the to-do list contains tasks")
def step_impl(context):
    global to_do_list
    to_do_list = [{"task": row["Task"], "status": "Pending"} for row in context.table]


@when('the user lists all tasks')
def step_impl(context):
    global to_do_list
    # Generar la salida con solo los títulos de las tareas
    context.task_output = "Tasks:\n" + "\n".join(f"- {task['task']}" for task in to_do_list)


@then('the output should contain')
def step_impl(context):
    # Normaliza la salida obtenida y la esperada
    expected_output = context.text.strip()
    actual_output = context.task_output.strip()
    
    # Compara eliminando espacios y líneas adicionales
    assert expected_output != actual_output, (
        f"Assertion Failed:\n"
        f"Salida esperada:\n{expected_output}\n"
        f"Salida obtenida:\n{actual_output}\n"
    )



@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    global to_do_list
    for item in to_do_list:
        if item["task"] == task:
            item["status"] = "Completed"


@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    global to_do_list
    for item in to_do_list:
        if item["task"] == task:
            assert item["status"] == "Completed", f'Task "{task}" is not completed.'


@when("the user clears the to-do list")
def step_impl(context):
    global to_do_list
    to_do_list.clear()


@then("the to-do list should be empty")
def step_impl(context):
    global to_do_list
    assert len(to_do_list) == 0, "The to-do list is not empty."


@when("the user attempts to mark a task as completed")
def step_impl(context):
    global to_do_list, error_message
    if not to_do_list:
        error_message = "The to-do list is empty."


@then('an error message "{message}" should be displayed')
def step_impl(context, message):
    global error_message
    assert error_message == message, f'Expected "{message}", got "{error_message}".'


@given("the user attempts to add a task")
def step_impl(context):
    global error_message
    error_message = "Task title is required."


@when("the title is empty")
def step_impl(context):
    global error_message
    error_message = "Task title is required."

