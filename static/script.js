addEventListener("change", (event) => {});

onchange = (event) => {
    fetch("http://127.0.0.1:5000/", {
        method: "POST",
        body: JSON.stringify({
            //filter: document.getElementById("filter-select").value,
            item_name: event.target.id,
            item_checked: event.target.checked
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });


};