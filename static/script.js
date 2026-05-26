const taskList = document.getElementById("taskList");
const taskForm = document.getElementById("taskForm");
const taskInput = document.getElementById("taskInput");

async function loadTasks() {
  const response = await fetch("/api/tasks");
  const tasks = await response.json();

  taskList.innerHTML = "";

  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.className = "task-item";

    li.innerHTML = `
      <span class="task-title ${task.completed ? "completed" : ""}">
        ${task.title}
      </span>
      <div class="actions">
        <button class="done-btn">${task.completed ? "Undo" : "Done"}</button>
        <button class="delete-btn">Delete</button>
      </div>
    `;

    li.querySelector(".done-btn").addEventListener("click", async () => {
      await fetch(`/api/tasks/${task.id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ completed: !task.completed })
      });

      loadTasks();
    });

    li.querySelector(".delete-btn").addEventListener("click", async () => {
      await fetch(`/api/tasks/${task.id}`, {
        method: "DELETE"
      });

      loadTasks();
    });

    taskList.appendChild(li);
  });
}

taskForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const title = taskInput.value.trim();

  if (!title) {
    return;
  }

  await fetch("/api/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  });

  taskInput.value = "";
  loadTasks();
});

loadTasks();
