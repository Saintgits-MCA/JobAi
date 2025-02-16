// script.js

// Function to filter jobs based on the search input
function filterJobs() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const rows = document.querySelectorAll('#jobTable tbody tr');

    rows.forEach(row => {
        const jobTitle = row.cells[0].textContent.toLowerCase();
        const company = row.cells[1].textContent.toLowerCase();
        const location = row.cells[2].textContent.toLowerCase();

        if (jobTitle.includes(searchInput) || company.includes(searchInput) || location.includes(searchInput)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

// Sorting functionality for table columns
document.querySelectorAll('th').forEach((header, index) => {
    header.addEventListener('click', () => {
        sortTable(index);
    });
});

function sortTable(columnIndex) {
    const table = document.getElementById('jobTable');
    const rows = Array.from(table.rows).slice(1);
    const isAscending = table.querySelector(`th:nth-child(${columnIndex + 1})`).classList.contains('ascending');

    rows.sort((a, b) => {
        const aText = a.cells[columnIndex].textContent.trim();
        const bText = b.cells[columnIndex].textContent.trim();

        if (columnIndex === 3) {  // If sorting by date
            return isAscending ? new Date(aText) - new Date(bText) : new Date(bText) - new Date(aText);
        }

        return isAscending ? aText.localeCompare(bText) : bText.localeCompare(aText);
    });

    rows.forEach(row => table.appendChild(row)); // Reorder the rows

    // Toggle the sorting state (ascending or descending)
    table.querySelectorAll('th').forEach(th => th.classList.remove('ascending', 'descending'));
    table.querySelector(`th:nth-child(${columnIndex + 1})`).classList.toggle('ascending', !isAscending);
    table.querySelector(`th:nth-child(${columnIndex + 1})`).classList.toggle('descending', isAscending);
}
