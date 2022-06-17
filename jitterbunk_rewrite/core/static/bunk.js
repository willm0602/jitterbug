function bunk(sender, recevier)
{
    alert(`${sender} bunked ${recevier}`);
    $.ajax({
        headers: { "X-CSRFToken": csrf },
        url: '/api/bunk',
        data: {
            sender_id: sender,
            receiver_id: recevier
        },
        method: 'POST',
        success: (res) => {
            console.log(res.statusText);
        },
        error: (rej) => {
            console.error(rej.statusText);
        }
    })
}