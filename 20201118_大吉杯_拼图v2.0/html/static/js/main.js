var popGrid = function ($grid, html, quantity) {
  var computed = html;
  for (var i = 0; i < quantity; i++) {
    if (typeof (html) == 'function') {
      computed = html(i);
    }
    $($grid).append(computed);
  }
};
var down_time = new Date().getTime();
var ImgClick = function(which) {
    down_time = new Date().getTime();
};
var ImgRotate = function(which){
    var up_time = new Date().getTime();
    if(up_time - down_time < 300){
        var rota = which.style.transform;
        if(!rota){
            rota = 90;
        }else{
            rota = parseInt(rota.split("rotate(")[1].split("deg)")[0]);
            rota = (rota+90)%360;
        }
        $(which).css('transform', 'rotate('+rota+'deg)');
    }
};
$(function(){
	popGrid('#grid', function (i) {
        return '<a class="cell" style="background-image: url(/static/img/blocks/'+block_data[i]+'.png);" onmousedown="ImgClick(this)" onmouseup="ImgRotate(this)"></a>';
    }, block_data.length);
    $('#grid').gridstrap({
        swapMode: true,
        rearrangeOnDrag: false,
        autoPadNonContiguousCells: false
    });
});