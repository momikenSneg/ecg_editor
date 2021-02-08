let canvas = document.getElementById("paint");
let ctx = canvas.getContext("2d");
const width = canvas.width, height = canvas.height;
let canvas_data = {"pencil": [], "line": [], "rectangle": [], "circle": [], "eraser": []};

let image = document.getElementById('source');

let button_I = document.getElementById('option1')
let button_II = document.getElementById('option2')
let button_III = document.getElementById('option3')
let button_aVR = document.getElementById('option4')
let button_aVL = document.getElementById('option5')
let button_aVF = document.getElementById('option6')
let button_V1 = document.getElementById('option7')
let button_V2 = document.getElementById('option8')
let button_V3 = document.getElementById('option9')
let button_V4 = document.getElementById('option10')
let button_V5 = document.getElementById('option11')
let button_V6 = document.getElementById('option12')

let I_start_x = document.getElementById('I_start_x')
let I_start_y = document.getElementById('I_start_y')
let I_end_x = document.getElementById('I_end_x')
let I_end_y = document.getElementById('I_end_y')
let II_start_x = document.getElementById('II_start_x')
let II_start_y = document.getElementById('II_start_y')
let II_end_x = document.getElementById('II_end_x')
let II_end_y = document.getElementById('II_end_y')

let III_start_x = document.getElementById('III_start_x')
let III_start_y = document.getElementById('III_start_y')
let III_end_x = document.getElementById('III_end_x')
let III_end_y = document.getElementById('III_end_y')
let aVR_start_x = document.getElementById('aVR_start_x')
let aVR_start_y = document.getElementById('aVR_start_y')
let aVR_end_x = document.getElementById('aVR_end_x')
let aVR_end_y = document.getElementById('aVR_end_y')
let aVL_start_x = document.getElementById('aVL_start_x')
let aVL_start_y = document.getElementById('aVL_start_y')
let aVL_end_x = document.getElementById('aVL_end_x')
let aVL_end_y = document.getElementById('aVL_end_y')
let aVF_start_x = document.getElementById('aVF_start_x')
let aVF_start_y = document.getElementById('aVF_start_y')
let aVF_end_x = document.getElementById('aVF_end_x')
let aVF_end_y = document.getElementById('aVF_end_y')
let V1_start_x = document.getElementById('V1_start_x')
let V1_start_y = document.getElementById('V1_start_y')
let V1_end_x = document.getElementById('V1_end_x')
let V1_end_y = document.getElementById('V1_end_y')
let V2_start_x = document.getElementById('V2_start_x')
let V2_start_y = document.getElementById('V2_start_y')
let V2_end_x = document.getElementById('V2_end_x')
let V2_end_y = document.getElementById('V2_end_y')
let V3_start_x = document.getElementById('V3_start_x')
let V3_start_y = document.getElementById('V3_start_y')
let V3_end_x = document.getElementById('V3_end_x')
let V3_end_y = document.getElementById('V3_end_y')
let V4_start_x = document.getElementById('V4_start_x')
let V4_start_y = document.getElementById('V4_start_y')
let V4_end_x = document.getElementById('V4_end_x')
let V4_end_y = document.getElementById('V4_end_y')
let V5_start_x = document.getElementById('V5_start_x')
let V5_start_y = document.getElementById('V5_start_y')
let V5_end_x = document.getElementById('V5_end_x')
let V5_end_y = document.getElementById('V5_end_y')
let V6_start_x = document.getElementById('V6_start_x')
let V6_start_y = document.getElementById('V6_start_y')
let V6_end_x = document.getElementById('V6_end_x')
let V6_end_y = document.getElementById('V6_end_y')


ctx.drawImage(image, 0, 0);

function rectangle (){

    canvas.onmousedown = function (e){
        ctx.drawImage(image, 0, 0);
        img = ctx.getImageData(0, 0, width, height);
        prevX = e.offsetX;
        prevY = e.offsetY;
        hold = true;
    };

    canvas.onmousemove = function (e){
        if (hold){
            ctx.putImageData(img, 0, 0);
            curX = e.offsetX - prevX;
            curY = e.offsetY - prevY;
            ctx.strokeRect(prevX, prevY, curX, curY);
            canvas_data.rectangle.push({ "starx": prevX, "stary": prevY, "width": curX, "height": curY,
                "thick": ctx.lineWidth, "stroke": stroke_value, "stroke_color": ctx.strokeStyle, "fill": fill_value,
                "fill_color": ctx.fillStyle });

        }
    };

    canvas.onmouseup = function (e){
        hold = false;
    };

    canvas.onmouseout = function (e){
        hold = false;
    };
}

function print_I() {
    button_I.onmousedown = function (e){
        if (curX > prevX){
            I_start_x.value = prevX
            I_end_x.value = curX
        } else {
            I_start_x.value = curX
            I_end_x.value = prevX
        }
        if (curY > prevY){
            I_start_y.value = prevY
            I_end_y.value = curY
        } else {
            I_start_y.value = curY
            I_end_y.value = prevY
        }
    }
}

function print_II() {
    button_II.onmousedown = function (e){
        if (curX > prevX){
            II_start_x.value = prevX
            II_end_x.value = curX
        } else {
            II_start_x.value = curX
            II_end_x.value = prevX
        }
        if (curY > prevY){
            II_start_y.value = prevY
            II_end_y.value = curY
        } else {
            II_start_y.value = curY
            II_end_y.value = prevY
        }
    }
}

function print_III() {
    button_III.onmousedown = function (e){
        if (curX > prevX){
            III_start_x.value = prevX
            III_end_x.value = curX
        } else {
            III_start_x.value = curX
            III_end_x.value = prevX
        }
        if (curY > prevY){
            III_start_y.value = prevY
            III_end_y.value = curY
        } else {
            III_start_y.value = curY
            III_end_y.value = prevY
        }
    }
}

function print_aVR() {
    button_aVR.onmousedown = function (e){
        if (curX > prevX){
            aVR_start_x.value = prevX
            aVR_end_x.value = curX
        } else {
            aVR_start_x.value = curX
            aVR_end_x.value = prevX
        }
        if (curY > prevY){
            aVR_start_y.value = prevY
            aVR_end_y.value = curY
        } else {
            aVR_start_y.value = curY
            aVR_end_y.value = prevY
        }
    }
}

function print_aVL() {
    button_aVL.onmousedown = function (e){
        if (curX > prevX){
            aVL_start_x.value = prevX
            aVL_end_x.value = curX
        } else {
            aVL_start_x.value = curX
            aVL_end_x.value = prevX
        }
        if (curY > prevY){
            aVL_start_y.value = prevY
            aVL_end_y.value = curY
        } else {
            aVL_start_y.value = curY
            aVL_end_y.value = prevY
        }
    }
}

function print_aVF() {
    button_aVF.onmousedown = function (e){
        if (curX > prevX){
            aVF_start_x.value = prevX
            aVF_end_x.value = curX
        } else {
            aVF_start_x.value = curX
            aVF_end_x.value = prevX
        }
        if (curY > prevY){
            aVF_start_y.value = prevY
            aVF_end_y.value = curY
        } else {
            aVF_start_y.value = curY
            aVF_end_y.value = prevY
        }
    }
}

function print_V1() {
    button_V1.onmousedown = function (e){
        if (curX > prevX){
            V1_start_x.value = prevX
            V1_end_x.value = curX
        } else {
            V1_start_x.value = curX
            V1_end_x.value = prevX
        }
        if (curY > prevY){
            V1_start_y.value = prevY
            V1_end_y.value = curY
        } else {
            V1_start_y.value = curY
            V1_end_y.value = prevY
        }
    }
}

function print_V2() {
    button_V2.onmousedown = function (e){
        if (curX > prevX){
            V2_start_x.value = prevX
            V2_end_x.value = curX
        } else {
            V2_start_x.value = curX
            V2_end_x.value = prevX
        }
        if (curY > prevY){
            V2_start_y.value = prevY
            V2_end_y.value = curY
        } else {
            V2_start_y.value = curY
            V2_end_y.value = prevY
        }
    }
}

function print_V3() {
    button_V3.onmousedown = function (e){
        if (curX > prevX){
            V3_start_x.value = prevX
            V3_end_x.value = curX
        } else {
            V3_start_x.value = curX
            V3_end_x.value = prevX
        }
        if (curY > prevY){
            V3_start_y.value = prevY
            V3_end_y.value = curY
        } else {
            V3_start_y.value = curY
            V3_end_y.value = prevY
        }
    }
}

function print_V4() {
    button_V4.onmousedown = function (e){
        if (curX > prevX){
            V4_start_x.value = prevX.toString()
            V4_end_x.value = curX.toString()
        } else {
            V4_start_x.value = curX
            V4_end_x.value = prevX
        }
        if (curY > prevY){
            V4_start_y.value = prevY
            V4_end_y.value = curY
        } else {
            V4_start_y.value = curY
            V4_end_y.value = prevY
        }
    }
}

function print_V5() {
    button_V5.onmousedown = function (e){
        if (curX > prevX){
            V5_start_x.value = prevX.toString()
            V5_end_x.value = curX.toString()
        } else {
            V5_start_x.value = curX
            V5_end_x.value = prevX
        }
        if (curY > prevY){
            V5_start_y.value = prevY
            V5_end_y.value = curY
        } else {
            V5_start_y.value = curY
            V5_end_y.value = prevY
        }
    }
}

function print_V6() {
    button_V6.onmousedown = function (e){
        if (curX > prevX){
            V6_start_x.value = prevX.toString()
            V6_end_x.value = curX.toString()
        } else {
            V6_start_x.value = curX
            V6_end_x.value = prevX
        }
        if (curY > prevY){
            V6_start_y.value = prevY
            V6_end_y.value = curY
        } else {
            V6_start_y.value = curY
            V6_end_y.value = prevY
        }
    }
}