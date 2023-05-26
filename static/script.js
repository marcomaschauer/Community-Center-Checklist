addEventListener("change", (event) => {});

onchange = (event) => {
    fetch("https://stardewvalley.marcom.one/", {
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