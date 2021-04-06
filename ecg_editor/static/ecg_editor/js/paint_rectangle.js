let canvas = document.getElementById("paint");
let ctx = canvas.getContext("2d");
const width = canvas.width, height = canvas.height;
let canvas_data = {"pencil": [], "line": [], "rectangle": [], "circle": [], "eraser": []};

let image = document.getElementById('source');

let I_start_x;
let I_start_y;
let I_end_x;
let I_end_y;

let II_start_x;
let II_start_y;
let II_end_x;
let II_end_y;

let III_start_x;
let III_start_y;
let III_end_x;
let III_end_y;

let aVR_start_x;
let aVR_start_y;
let aVR_end_x;
let aVR_end_y;

let aVL_start_x;
let aVL_start_y;
let aVL_end_x;
let aVL_end_y;

let aVF_start_x;
let aVF_start_y;
let aVF_end_x;
let aVF_end_y;

let V1_start_x;
let V1_start_y;
let V1_end_x;
let V1_end_y;

let V2_start_x;
let V2_start_y;
let V2_end_x;
let V2_end_y;

let V3_start_x;
let V3_start_y;
let V3_end_x;
let V3_end_y;

let V4_start_x;
let V4_start_y;
let V4_end_x;
let V4_end_y;

let V5_start_x;
let V5_start_y;
let V5_end_x;
let V5_end_y;

let V6_start_x;
let V6_start_y;
let V6_end_x;
let V6_end_y;

let startX;
let startY;
let endX;
let endY;
let curX;
let curY;

let is_I = false;
let is_II = false;
let is_III = false;
let is_aVR = false;
let is_aVL = false;
let is_aVF = false;
let is_V1 = false;
let is_V2 = false;
let is_V3 = false;
let is_V4 = false;
let is_V5 = false;
let is_V6 = false;

ctx.drawImage(image, 0, 0);

function rectangle() {
    canvas.onmousedown = function (e) {
        ctx.drawImage(image, 0, 0);
        img = ctx.getImageData(0, 0, width, height);
        startX = e.offsetX;
        startY = e.offsetY;
        hold = true;
    };

    canvas.onmousemove = function (e) {
        if (hold) {
            ctx.putImageData(img, 0, 0);
            curX = e.offsetX - startX;
            curY = e.offsetY - startY;
            endX = e.offsetX;
            endY = e.offsetY;
            ctx.strokeRect(startX, startY, curX, curY);
            canvas_data.rectangle.push({
                "starx": startX, "stary": startY, "width": curX, "height": curY,
                "thick": ctx.lineWidth, "stroke": stroke_value, "stroke_color": ctx.strokeStyle, "fill": fill_value,
                "fill_color": ctx.fillStyle
            });

        }
    };

    canvas.onmouseup = function (e) {
        hold = false;
    };

    canvas.onmouseout = function (e) {
        hold = false;
    };
}

function print_I() {
    I_start_x = Math.min(endX, startX);
    I_end_x = Math.max(endX, startX);

    I_start_y = Math.min(endY, startY);
    I_end_y = Math.max(endY, startY);
    if (!isAreaChosen(I_end_x, I_start_x, I_end_y, I_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option1').style.backgroundColor = '#55ff75'
    document.getElementById('option1').style.color = '#ffffff'
    is_I = true;
}

function print_II() {
    II_start_x = Math.min(endX, startX);
    II_end_x = Math.max(endX, startX);

    II_start_y = Math.min(endY, startY);
    II_end_y = Math.max(endY, startY);
    if (!isAreaChosen(II_end_x, II_start_x, II_end_y, II_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option2').style.backgroundColor = '#55ff75'
    document.getElementById('option2').style.color = '#ffffff'

    is_II = true;
}

function print_III() {
    III_start_x = Math.min(endX, startX);
    III_end_x = Math.max(endX, startX);

    III_start_y = Math.min(endY, startY);
    III_end_y = Math.max(endY, startY);
    if (!isAreaChosen(III_end_x, III_start_x, III_end_y, III_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option3').style.backgroundColor = '#55ff75'
    document.getElementById('option3').style.color = '#ffffff'

    is_III = true;
}

function print_aVR() {
    aVR_start_x = Math.min(endX, startX);
    aVR_end_x = Math.max(endX, startX);

    aVR_start_y = Math.min(endY, startY);
    aVR_end_y = Math.max(endY, startY);
    if (!isAreaChosen(aVR_end_x, aVR_start_x, aVR_end_y, aVR_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option4').style.backgroundColor = '#55ff75'
    document.getElementById('option4').style.color = '#ffffff'

    is_aVR = true;
}

function print_aVL() {
    aVL_start_x = Math.min(endX, startX);
    aVL_end_x = Math.max(endX, startX);

    aVL_start_y = Math.min(endY, startY);
    aVL_end_y = Math.max(endY, startY);
    if (!isAreaChosen(aVL_end_x, aVL_start_x, aVL_end_y, aVL_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option5').style.backgroundColor = '#55ff75'
    document.getElementById('option5').style.color = '#ffffff'

    is_aVL = true;
}

function print_aVF() {
    aVF_start_x = Math.min(endX, startX);
    aVF_end_x = Math.max(endX, startX);

    aVF_start_y = Math.min(endY, startY);
    aVF_end_y = Math.max(endY, startY);
    if (!isAreaChosen(aVF_end_x, aVF_start_x, aVF_end_y, aVF_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option6').style.backgroundColor = '#55ff75'
    document.getElementById('option6').style.color = '#ffffff'

    is_aVF = true;
}

function print_V1() {
    V1_start_x = Math.min(endX, startX);
    V1_end_x = Math.max(endX, startX);

    V1_start_y = Math.min(endY, startY);
    V1_end_y = Math.max(endY, startY);
    if (!isAreaChosen(V1_end_x, V1_start_x, V1_end_y, V1_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option7').style.backgroundColor = '#55ff75'
    document.getElementById('option7').style.color = '#ffffff'
    is_V1 = true;
}

function print_V2() {
    V2_start_x = Math.min(endX, startX);
    V2_end_x = Math.max(endX, startX);

    V2_start_y = Math.min(endY, startY);
    V2_end_y = Math.max(endY, startY);
    if (!isAreaChosen(V2_end_x, V2_start_x, V2_end_y, V2_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option8').style.backgroundColor = '#55ff75'
    document.getElementById('option8').style.color = '#ffffff'
    is_V2 = true;
}

function print_V3() {
    V3_start_x = Math.min(endX, startX);
    V3_end_x = Math.max(endX, startX);

    V3_start_y = Math.min(endY, startY);
    V3_end_y = Math.max(endY, startY);
    if (!isAreaChosen(V3_end_x, V3_start_x, V3_end_y, V3_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option9').style.backgroundColor = '#55ff75'
    document.getElementById('option9').style.color = '#ffffff'
    is_V3 = true;
}

function print_V4() {
    V4_start_x = Math.min(endX, startX);
    V4_end_x = Math.max(endX, startX);

    V4_start_y = Math.min(endY, startY);
    V4_end_y = Math.max(endY, startY);
    if (!isAreaChosen(V4_end_x, V4_start_x, V4_end_y, V4_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option10').style.backgroundColor = '#55ff75'
    document.getElementById('option10').style.color = '#ffffff'
    is_V4 = true;
}

function print_V5() {
    V5_start_x = Math.min(endX, startX);
    V5_end_x = Math.max(endX, startX);

    V5_start_y = Math.min(endY, startY);
    V5_end_y = Math.max(endY, startY);
    if (!isAreaChosen(V5_end_x, V5_start_x, V5_end_y, V5_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option11').style.backgroundColor = '#55ff75'
    document.getElementById('option11').style.color = '#ffffff'
    is_V5 = true;
}

function print_V6() {
    V6_start_x = Math.min(endX, startX);
    V6_end_x = Math.max(endX, startX);

    V6_start_y = Math.min(endY, startY);
    V6_end_y = Math.max(endY, startY);
    if (!isAreaChosen(V6_end_x, V6_start_x, V6_end_y, V6_start_y)) {
        alert("Сначала выделите область, в которую входит одно из отведений, пожалуйста");
        return;
    }
    document.getElementById('option12').style.backgroundColor = '#55ff75'
    document.getElementById('option12').style.color = '#ffffff'
    is_V6 = true;
}

function save_images() {
    if (is_I && is_II && is_III && is_aVF && is_aVL && is_aVR && is_V1 && is_V2 && is_V3 && is_V4 && is_V5 && is_V6) {
        let xhr = new XMLHttpRequest();
        xhr.open('POST', 'http://127.0.0.1:8000/ecg_editor/image/cut', false);
        //xhr.setRequestHeader('X-CSRFToken', "getCookie(\"csrftoken\")");
        //xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        const body = 'I_start_x=' + encodeURIComponent(I_start_x) + '&I_start_y=' + encodeURIComponent(I_start_y)
            + '&I_end_x=' + encodeURIComponent(I_end_x) + '&I_end_y=' + encodeURIComponent(I_end_y)
            + '&II_start_x=' + encodeURIComponent(II_start_x) + '&II_start_y=' + encodeURIComponent(II_start_y)
            + '&II_end_x=' + encodeURIComponent(II_end_x) + '&II_end_y=' + encodeURIComponent(II_end_y)
            + '&III_start_x=' + encodeURIComponent(III_start_x) + '&III_start_y=' + encodeURIComponent(III_start_y)
            + '&III_end_x=' + encodeURIComponent(III_end_x) + '&III_end_y=' + encodeURIComponent(III_end_y)
            + '&aVR_start_x=' + encodeURIComponent(aVR_start_x) + '&aVR_start_y=' + encodeURIComponent(aVR_start_y)
            + '&aVR_end_x=' + encodeURIComponent(aVR_end_x) + '&aVR_end_y=' + encodeURIComponent(aVR_end_y)
            + '&aVL_start_x=' + encodeURIComponent(aVL_start_x) + '&aVL_start_y=' + encodeURIComponent(aVL_start_y)
            + '&aVL_end_x=' + encodeURIComponent(aVL_end_x) + '&aVL_end_y=' + encodeURIComponent(aVL_end_y)
            + '&aVF_start_x=' + encodeURIComponent(aVF_start_x) + '&aVF_start_y=' + encodeURIComponent(aVF_start_y)
            + '&aVF_end_x=' + encodeURIComponent(aVF_end_x) + '&aVF_end_y=' + encodeURIComponent(aVF_end_y)
            + '&V1_start_x=' + encodeURIComponent(V1_start_x) + '&V1_start_y=' + encodeURIComponent(V1_start_y)
            + '&V1_end_x=' + encodeURIComponent(V1_end_x) + '&V1_end_y=' + encodeURIComponent(V1_end_y)
            + '&V2_start_x=' + encodeURIComponent(V2_start_x) + '&V2_start_y=' + encodeURIComponent(V2_start_y)
            + '&V2_end_x=' + encodeURIComponent(V2_end_x) + '&V2_end_y=' + encodeURIComponent(V2_end_y)
            + '&V3_start_x=' + encodeURIComponent(V3_start_x) + '&V3_start_y=' + encodeURIComponent(V3_start_y)
            + '&V3_end_x=' + encodeURIComponent(V3_end_x) + '&V3_end_y=' + encodeURIComponent(V3_end_y)
            + '&V4_start_x=' + encodeURIComponent(V4_start_x) + '&V4_start_y=' + encodeURIComponent(V4_start_y)
            + '&V4_end_x=' + encodeURIComponent(V4_end_x) + '&V4_end_y=' + encodeURIComponent(V4_end_y)
            + '&V5_start_x=' + encodeURIComponent(V5_start_x) + '&V5_start_y=' + encodeURIComponent(V5_start_y)
            + '&V5_end_x=' + encodeURIComponent(V5_end_x) + '&V5_end_y=' + encodeURIComponent(V5_end_y)
            + '&V6_start_x=' + encodeURIComponent(V6_start_x) + '&V6_start_y=' + encodeURIComponent(V6_start_y)
            + '&V6_end_x=' + encodeURIComponent(V6_end_x) + '&V6_end_y=' + encodeURIComponent(V6_end_y)
            //TODO
            + '&patient_id=';
        xhr.send(body);
        if (xhr.status !== 200) {
            alert(xhr.status + ': ' + xhr.statusText);
        } else {
            alert("ВСе океюшки");
        }
    } else {
        window.alert("Выделите все отведения");
    }
}

function isAreaChosen(end_x, start_x, end_y, start_y) {
    if (isNaN(end_x) || isNaN(start_y) || isNaN(start_y) || isNaN(start_y)) {
        return false;
    }
    if (end_x - start_x < 50 || end_y - start_y < 50) {
        return false;
    }
    return true;
}
