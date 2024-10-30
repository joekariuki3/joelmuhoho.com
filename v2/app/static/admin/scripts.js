// adminbase script
function toggleMenu() {
  const navMenu = document.getElementById("nav-menu");
  navMenu.classList.toggle("hidden");
}

// toggle projects in dashboard
function toggleProjects(categoryId) {
  const projectList = document.getElementById(`projects-list-${categoryId}`);
  projectList.classList.toggle("hidden");
}

// Function to show the delete modal for a project or category
function showDeleteModal(projectId) {
  const modal = document.getElementById("delete-modal");
  const form = document.getElementById("delete-form");
  form.action = `/admin/delete_project/${projectId}`; // Update form action
  modal.classList.remove("hidden"); // Show the modal
}

function hideDeleteModal() {
  const modal = document.getElementById("delete-modal");
  modal.classList.add("hidden"); // Hide the modal
}

// Function to show the delete modal
function showDeleteModal(entityType, entityId, entityName = null) {
  const modal = document.getElementById("delete-modal");
  const form = document.getElementById("delete-form");
  const message = document.getElementById("delete-message");

  // Update the form action dynamically based on the entity type
  form.action = `/admin/delete_${entityType}/${entityId}`;

  // Update confirmation message if entityName is provided
  if (entityName) {
    message.textContent = `Are you sure you want to permanently delete the ${entityType} "${entityName}"? This action cannot be undone.`;
  } else {
    message.textContent = `Are you sure you want to permanently delete this ${entityType}? This action cannot be undone.`;
  }

  modal.classList.remove("hidden"); // Show the modal
}

// Function to hide the delete modal
function hideDeleteModal() {
  const modal = document.getElementById("delete-modal");
  modal.classList.add("hidden"); // Hide the modal
}
