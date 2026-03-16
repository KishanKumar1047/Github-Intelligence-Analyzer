console.log("JS Loaded")
async function analyze(){

let username = document.getElementById("username").value.trim()

const loading = document.getElementById("loading")
const result = document.getElementById("result")

loading.classList.remove("hidden")
result.textContent = ""

try{

const response = await fetch(
`https://github-intelligence-analyzer.onrender.com/analyze/${username}`
)

const data = await response.json()

console.log(data)

result.textContent = JSON.stringify(data,null,2)

}catch(error){

result.textContent = "Server waking up... try again in a few seconds."

}

loading.classList.add("hidden")

}