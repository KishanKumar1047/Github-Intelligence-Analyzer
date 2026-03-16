async function analyze(){

const username = document.getElementById("username").value

const response = await fetch(`https://github-intelligence-analyzer.onrender.com/analyze/${username}`)

const data = await response.json()

document.getElementById("result").textContent =
JSON.stringify(data, null, 2)

}
