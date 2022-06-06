$(document).ready(() => {
    $(".like-btn").click((e) => {
        e.preventDefault()
        id = $(".like-btn").attr("value")
        alert(id)
        section = $("#picture-section")
        $.ajax({
            "url": "/ajax/like/",
            "type": "POST",
            "data": { "id": id, "csrfmiddlewaretoken": '{{csrf_token}}' },
            "dataType": "json",
            "success": function (res) {
                $("#likes-icon").html(res["likes"])
            }
        })
    })
}) 