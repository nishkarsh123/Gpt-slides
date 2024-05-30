
document.addEventListener("DOMContentLoaded", function () {
    fetch('/list-ppt')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            updateTable(data);
        })
        .catch(error => console.error(error));

const list = document.querySelector('.table tbody');
const intervalTime = 5000;

function updateTable(data) {
    list.innerHTML = '';
    data.forEach((item,index) => {
        const row = document.createElement('tr');
        const id = document.createElement('td');
        id.textContent = index+1;
        row.appendChild(id);
        const status = document.createElement('td');
        status.textContent = item.status;
        row.appendChild(status);
        const createdAt = document.createElement('td');
        createdAt.textContent = item.created_at;
        row.appendChild(createdAt);
        const url = document.createElement('td');
        const viewButton = document.createElement('a');
        viewButton.disabled = !item.ppt_modified;
        if (!item.ppt_modified) {
            viewButton.style.backgroundColor = 'grey';
        }
        //console.log(item.ppt_modified,item.ppt_modified.split('/'),`media/ppt_modified/${item.ppt_modified.split('/')[item.ppt_modified.split('/').length-1]}`)
        viewButton.href = item.ppt_modified;
        viewButton.textContent = 'View';
        viewButton.classList.add('btn', 'btn-primary');
        url.appendChild(viewButton);
        row.appendChild(url);
        list.appendChild(row);
    });
}
setInterval(() => {
    fetch('/list-ppt')
        .then(response => response.json())
        .then(data => {
            updateTable(data);
        });
}, intervalTime);
});