var MyChart = function () {
    this.domElement = null;
    this.chart = null;
    this.url = "";
    this.title = "";
    this.option = {};
    this.aspectRatio = 9/16;

    this.resize = function() {
        let graph = this.domElement;
        let graphWidth = graph.clientWidth;
        graph.style.height = "" + (this.aspectRatio * graphWidth).toFixed(0) + "px";
        this.chart.resize()
    };

    this.calcPointList = function (data) {
        throw "没有处理数据的函数"
    };

    this.init = function() {
        $(window).resize(this.resize.bind(this));
        if (this.domElement === null)
            this.domElement = document.getElementById('hot_graph');
        this.chart = echarts.init(this.domElement);
        $.get(this.url, function (data, status) {
            if (status !== "success")
                return;
            let pointList = this.calcPointList(data);
            this.drawGraph({"pointList": pointList})
        }.bind(this));

    };

    this.drawGraph=function(data) {

        if(!('title' in this.option))
            this.option.title = {};
        this.option['title']['text'] = this.title;
        if('x' in data.pointList) {
            if(!('xAxis' in this.option))
                this.option.xAxis = {};
            this.option['xAxis']['data'] = data.pointList.x;
        }
        if(!("series" in this.option)) {
            this.option.series = [];
            this.option.series.push({});
        }
        this.option['series'][0]['data'] = data.pointList.y;
        this.resize();
        this.chart.setOption(this.option);

    };




    //$(this.init);
};