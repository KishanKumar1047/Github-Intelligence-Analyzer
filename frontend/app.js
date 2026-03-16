async function analyze(){

const username = document.getElementById("username").value

const response = await fetch(`http://127.0.0.1:8000/analyze/${username}`)

const data = await response.json()

document.getElementById("result").textContent =
JSON.stringify(data, null, 2)

}
