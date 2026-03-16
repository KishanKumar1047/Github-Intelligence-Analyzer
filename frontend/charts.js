function drawStackChart(stack){

const ctx = document.getElementById('stackChart')

new Chart(ctx,{
type:'bar',
data:{
labels:Object.keys(stack),
datasets:[{
data:Object.values(stack)
}]
}
})

}