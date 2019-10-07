// 这个js用于改变条条的大小，让其成为柱状图
onloadRegister(resizeBar);
function resizeBar() {
    let rows = document.getElementsByClassName('bar_row');
    let maxWeight = 0;
    // 先遍历一遍取得权重的最大值
    for(let i=0;i<rows.length;i++){
        let row = rows[i];
        let weight = row.getElementsByClassName('weight')[0];
        weight = parseFloat(weight.innerHTML);
        if (weight > maxWeight){
            maxWeight = weight
        }
    }
    // 再遍历一遍来计算条子的长度
    for(let i=0;i<rows.length;i++) {
        let row = rows[i];
        let weight = row.getElementsByClassName('weight')[0];
        weight = parseFloat(weight.innerHTML);
        let percent = (weight/maxWeight*100).toFixed(0);
        let bar = row.getElementsByClassName('bar')[0];
        bar.style.width = ""+percent+"%";
    }

}