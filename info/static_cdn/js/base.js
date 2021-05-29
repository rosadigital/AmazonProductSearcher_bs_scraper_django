      function mudarCor(novaCor) {
        var elemento = document.getElementById("para1");
        elemento.style.color = novaCor;
      }

//      function tableCreate() {
//      var body = document.getElementsByTagName('body')[0];
//      var tbl = document.createElement('table');
//      tbl.style.width = '100%';
//      tbl.setAttribute('border', '1');
//      var tbdy = document.createElement('tbody');
//      for (var i = 0; i < 3; i++) {
//        var tr = document.createElement('tr');
//        for (var j = 0; j < 2; j++) {
//          if (i == 2 && j == 1) {
//            break
//          } else {
//            var td = document.createElement('td');
//            td.appendChild(document.createTextNode('\u0020'))
//            i == 1 && j == 1 ? td.setAttribute('rowSpan', '2') : null;
//            tr.appendChild(td)
//          }
//        }
//        tbdy.appendChild(tr);
//      }
//      tbl.appendChild(tbdy);
//      body.appendChild(tbl)
//    }
//    tableCreate();
//|escapejs
function data(){
    var obj = document.getElementById("div1");
    var r = Math.floor(Math.random()*255);
    var g = Math.floor(Math.random()*255);
    var b = Math.floor(Math.random()*255);
    obj.style.color = "rgb("+r+","+g+","+b+")";

    var companies = '{{ data }}';
}
function refresh(){
    setInterval(data(),100)
}
window.addEventListener("load", refresh);


// setInterval(function(){//setInterval() method execute on every interval until called clearInterval()
//  $('#load_posts').load("display.php").fadeIn("slow");
//  //load() method fetch data from fetch.php page
// }, 1000);