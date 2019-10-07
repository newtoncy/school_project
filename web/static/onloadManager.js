// 这个函数用于管理onload事件

let onloadList = [];


function _onload() {
    for(let i=0;i<onloadList.length;i++){
        let f = onloadList[i];
        f();
    }
}

function onloadRegister(func) {
    onloadList.push(func);
}

window.onload = _onload;