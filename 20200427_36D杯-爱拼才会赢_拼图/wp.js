// 点击图片进行交换
let page_one = null;
let page_two = null;

function change_div(){
	var tmp_bg = page_one.css("background-image");
	page_one.css("background-image",page_two.css("background-image"));
	page_two.css("background-image",tmp_bg);
	check_now();
}

$(".hang div").click(function(){
	if(!page_one){
		page_one = $(this);
		$("h1").text("page_one");
	}else if(!page_two){
		page_two = $(this);
		$("h1").text("page_two");
		change_div();
		page_one = null;
		page_two = null;
	}
});

// 字符串回显拼图
var origin_str = '5c2b316b52956639ece7fegac857dabcf8g0fff582b4b724d8cha4ag3341094d03760108290e04f1f38a70e1e25edcc50d96e6e53837g81a9f7ca1f77f835380614a435d7915403646ddf4ae5h1d026922458e994c0c1gehb875g2g926f997e41cfc1471c2ahc9fdd60f3234c08f8c922f3afaea72cbb23060g3fbf23cdh2ee0f6dgc613b0749d1h1e19db182cc1a89b8h5g6f472g2d4ef0d28g3b7b786g5554affgeg49b66a4b3gb99a7a77bhb3cc51874he9100bed94ac67dece86a0c4aabbfh7hg59e0a0h3hd45a4f123e642365a7cd11a97gbg2abd275f215025eeg67d9ca62881cgd9598990b19h8842bfef633fg11febc36c586h16b50gg784627e3556a3c7856dd5cae39g8d6edf173d1b068b44d3g420abd0a25ba59398d791cf2h734gba4868d10507e8adbe';
$(".hang div").each(function(i,e){
	if(i*2 < origin_str.length){
		$(e).css("background-image","url('./data/"+origin_str.substr(i*2,2)+".jpg')");
	}
});
check_now();

// 拼图导出字符串
var origin_str = '';
$(".hang div").each(function(i,e){
  var base = bg2base($(e).css("background-image"));
  if(base == 'empty'){ base = '';}
  origin_str += base;
});
console.log(origin_str);
