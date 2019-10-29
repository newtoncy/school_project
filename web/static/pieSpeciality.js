var pieSpeciality = function () {
    let myChart = new MyChart();
    let option = {

        title: {
            text: 'Customized Pie',
            left: 'center',
            top: 20,
            textStyle: {
                color: '#000'
            }
        },

        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },

        visualMap: {
            show: false,
            min: 80,
            max: 600,
            inRange: {
                colorLightness: [0, 1]
            }
        },
        series: [
            {
                name: '访问来源',
                type: 'pie',
                radius: '55%',
                center: ['50%', '50%'],
                data: [
                    {value: 335, name: '直接访问'},
                    {value: 310, name: '邮件营销'},
                    {value: 274, name: '联盟广告'},
                    {value: 235, name: '视频广告'},
                    {value: 400, name: '搜索引擎'}
                ].sort(function (a, b) {
                    return a.value - b.value;
                }),
                roseType: 'radius',
                label: {
                    normal: {
                        textStyle: {
                            color: 'rgba(55, 55, 55, 1)'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        lineStyle: {
                            color: 'rgba(55, 55, 55, 1)'
                        },
                        smooth: 0.2,
                        length: 10,
                        length2: 20
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#c23531',
                        shadowBlur: 100,
                        shadowColor: 'rgba(0, 0, 0, 0.2)'
                    }
                },

                animationType: 'scale',
                animationEasing: 'elasticOut',
                animationDelay: function (idx) {
                    return Math.random() * 200;
                }
            }
        ]
    };
    $(init);
    function init() {
        myChart.domElement = document.getElementById("pie_chart");
        myChart.url = document.location.toString()+"?json=true";
        myChart.title = "相关专业";
        myChart.option = option;
        myChart.calcPointList = calcPointList;
        myChart.init()
    }
    
    function calcPointList(data) {
        data = JSON.parse(data);
        let pointList = {};
        pointList.y = [];
        let items = data["speciality"];
        if(items.length>5)
            items = items.slice(0,5);
        for(let i = 0;i< items.length;i++){
            let item = items[i];
            if(item.name ==="__none__")
                item.name = "任何专业";
            pointList.y.push({"name":item.name,"value":item.frequency})
        }
        return pointList;
    }
    return {"init":init,"myChart":myChart};
}();