var hotSpecialityGraph = function () {
    let domElement = null;
    let chart = null;

    function resize() {
        let graph = domElement;
        let graphWidth = graph.clientWidth;
        graph.style.height = "" + ((9 / 16) * graphWidth).toFixed(0) + "px";
        chart.resize()
    }

    function init() {
        window.onresize = resize;
        domElement = document.getElementById('hot_graph');
        chart = echarts.init(domElement);
        let pointList = {};
        pointList.x = [];
        pointList.y = [];
        $.get("/api/speciality/?json=true", function (data, status) {
            if (status !== "success")
                return;
            let json = $.parseJSON(data);
            let items = json['speciality'];
            for (let i = 0; i < items.length; i++) {
                let item = items[i];
                if (item.name !== "__none__") {
                    pointList.x.push(item.name);
                    pointList.y.push(item.frequency);
                }
            }
            drawGraph({"pointList": pointList})
        });

    }

    function drawGraph(data) {
        let title = "热门专业排行";
        let option = {
            title: {
                text: title
            },
            xAxis: {
                name: "专业",
                data: data.pointList.x,
                axisLabel: {
                    interval: 0
                }
            },
            yAxis: {
                name: "热度"
            },
            series: [{
                data: data.pointList.y,
                type: 'bar'
            }],
            dataZoom: [
                {
                    show: true,
                    realtime: true,
                    start: 0,
                    end: 35
                }
            ]

        };
        resize();
        chart.setOption(option);

    }

    $(init);
    return {
        "resize": resize,
        "setDomElement": function (_domElement) {
            domElement = _domElement
        },
        "init": init
    }
}();