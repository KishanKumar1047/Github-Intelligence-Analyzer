async function analyze(){

let username = document.getElementById("username").value.trim()

if(!username){
alert("Enter a GitHub username")
return
}

username = username.replace("/analyze/","")

const loading = document.getElementById("loading")
const result = document.getElementById("result")

loading.classList.remove("hidden")
result.textContent = ""

try{

const response = await fetch(
`https://github-intelligence-analyzer.onrender.com/analyze/${username}`
)

const data = await response.json()

result.textContent = JSON.stringify(data,null,2)

}catch(error){

result.textContent = "Error analyzing profile"

}

loading.classList.add("hidden")

}