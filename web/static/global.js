function isEmpty(obj) {
    return typeof obj == "undefined" || obj == null || obj === "";
}


function getUrlRelativePath() {
    let url = document.location.toString();
    let arrUrl = url.split("//");

    let start = arrUrl[1].indexOf("/");
    let relUrl = arrUrl[1].substring(start);//stop省略，截取从start开始到结尾的所有字符

    if (relUrl.indexOf("?") !== -1) {
        relUrl = relUrl.split("?")[0];
    }
    return relUrl;
}

// 返回url的最后那部分
function getUrlFileName() {
    let url = getUrlRelativePath();
    let foo = url.split('/');
    return foo[foo.length - 1];
}

function getUrlParam(paraName) {
    let url = document.location.toString();
    let arrObj = url.split("?");

    if (arrObj.length > 1) {
        let arrPara = arrObj[1].split("&");
        let arr;

        for (let i = 0; i < arrPara.length; i++) {
            arr = arrPara[i].split("=");

            if (arr != null && arr[0] === paraName) {
                return arr[1];
            }
        }
        return "";
    } else {
        return "";
    }
}