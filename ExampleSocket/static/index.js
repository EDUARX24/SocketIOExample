document.addEventListener("DOMContentLoaded", () =>{
    const socket = io()

    let room;

    const join_button = document.querySelector("#join")

    join_button.onclick() = () => {
        socket.emit("join_room", "WEB50", (res) =>{
            room = res;

            document.querySelector("#root").innerText = `Te has unido
            a la sala ${room}`;
            document.querySelector("#root").innerHTML
 
        })
    }
})