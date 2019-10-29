//初始化每个可展开区域
//运行工厂函数生成每个展开按钮的点击事件函数
onloadRegister(expandInit);
function expandInit() {
    let items = document.getElementsByClassName('etc');
    for (let i = 0; i < items.length; i++) {
        let item = items[i];
        let pNode = item.parentNode;
        while (pNode !== null && pNode.className !== 'cut') {
            pNode = pNode.parentNode;
        }
        if (pNode === null) continue;
        let pHeight = pNode.clientHeight;
        item.onclick = function () {
            let args = {
                'button': item,
                'div': pNode,
                'oriHeight': pNode.clientHeight,
                'limitHeight': limitHight,
                'isExpand': false
            };
            return function () {
                expand(args);
            };
        }();
        if (pNode.clientHeight > limitHight) {
            pNode.style.height = "" + limitHight + "px";
            item.style.visibility = "visible";
            item.innerHTML = "<span class=\"border_button\">展开</span>";
        } else {
            item.style.visibility = "hidden";
            item.innerHTML = ""
        }
    }
}

limitHight = 400;

function expand(args) {
    let item = args.button;
    let pNode = args.div;
    let limitHeight = args.limitHeight;
    if (!args.isExpand) {
        //展开
        pNode.style.height = "" + (args.oriHeight + 50) + "px";
        item.innerHTML = "<span class=\"border_button\">收起</span>";
        args.isExpand = true;
    } else {
        //收起
        pNode.style.height = "" + limitHeight + "px";
        item.innerHTML = "<span class=\"border_button\">展开</span>";
        args.isExpand = false;
    }
}

