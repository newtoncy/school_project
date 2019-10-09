onloadRegister(hotGraphInit);
function hotGraphInit() {
    let graph = document.getElementById('hot_graph');
    let xhr = new XMLHttpRequest();
    xhr.open('get',graph.innerHTML);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            drawGraph(xhr.responseText)
        }
    };
    xhr.send(null);
    this.myChart = echarts.init(graph);
    resize();

}
window.onresize = resize;
function resize() {
    let graph = document.getElementById('hot_graph');
    let graphWidth = graph.clientWidth;
    graph.style.height = ""+((9/16)*graphWidth).toFixed(0)+"px";
    this.myChart.resize()
}

function drawGraph(data){
    let json = eval('(' + data + ')');
    let title = document.getElementsByTagName('title')[0].innerHTML
        +"的热度趋势";
    let option = {
        title:{
          text: title
        },
        xAxis: {
            name:"日期：日",
            type: 'category',
            data: json.pointList.x
        },
        yAxis: {
            name:"频数：次",
            type: 'value'
        },
        series: [{
            data: json.pointList.y,
            type: 'line',
            smooth: true
        }]
    };


    this.myChart.setOption(option);

}

