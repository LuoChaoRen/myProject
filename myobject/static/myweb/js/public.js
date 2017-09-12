 // rem.js文件内容 
(function(){
    var calc = function(){
        //获取当前文档
        var docElement = document.documentElement;
        // 判断 当前文档宽度 大于 750 那么变量就是  750,否则就是当前文档实际宽度
        var clientWidthValue = docElement.clientWidth > 750 ? 750 : docElement.clientWidth;
        //设置当前文档的字体大小
        docElement.style.fontSize = 20*(clientWidthValue/375)+'px';
    }
    calc();
    //绑定事件,当浏览器的大小发生改变时
    window.addEventListener('resize',calc);
})();


// 表单事件

//声明全局变量
var NameOk = false;
var PassOk = false;
var EmailOk = false;

//获取焦点事件 focus
	$('.dengl .denglname input').focus(function(){
		//获取焦点时,给予提示信息
		console.log(1)
		var at = $(this).attr('readme');
		$(this).next('span').html(at).css('color','blue');
		$(this).css('border','1px solid blue');
	})

	//绑定丧失焦点事件 blur
	$('.dengl .denglname input[name=username]').blur(function(){
		//获取用户的输入信息
		var v = $(this).val();
		var reg = /^\w{6,18}$/;
		if(reg.test(v)){
			$(this).next('span').html('√').css('color','green');
			$(this).css('border','1px solid green');
			//修改全局变量
			NameOk = true;
		}else{
			$(this).next('span').html('用户名格式不正确').css('color','red');
			$(this).css('border','1px solid red');
			//修改全局变量
			NameOk = false;
		}
	})

	//绑定丧失焦点事件 blur
	$('.dengl .denglname input[name=password]').blur(function(){
		//获取用户的输入信息
		var v = $(this).val();
		var reg = /^\w{6,18}$/;
		if(reg.test(v)){
			$(this).next('span').html('√').css('color','green');
			$(this).css('border','1px solid green');
			//修改全局变量
			PassOk = true;
		}else{
			$(this).next('span').html('密码格式不正确').css('color','red');
			$(this).css('border','1px solid red');
				//修改全局变量
			PassOk = false;
		}
	})


	

	//表单提交事件 submit
	$('.dengl .denglname form').submit(function(){
		//触发input 丧失焦点事件
		$('.dengl .denglname input').trigger('blur');

		//判断如果都正确
		if(NameOk && PassOk ){
			return true;
		}
		//阻止默认行为
		return false;
	})


//导航栏
$('.pdd2 li').mouseover(function(){
	var a = $(this).val()
	if (a==1) {
		$('#dss').attr('src', 'static/myweb/img/fdb_hover.png' )
	}if (a==2) {
		$('#dgwc').attr('src', 'static/myweb/img/shopb.png' )
	}if (a==3) {
		$('#dp').attr('src', 'static/myweb/img/icon_person_hover.png' )
	}
})
$('.pdd2 li').mouseout(function(){
	var a = $(this).val()
	if (a==1) {
		$('#dss').attr('src', 'static/myweb/img/fdb.png' )
	}if (a==2) {
		$('#dgwc').attr('src', 'static/myweb/img/shopw.png' )
	}if (a==3) {
		$('#dp').attr('src', 'static/myweb/img/icon_person.png' )
	}
})

$(window).scroll(function(){
	var a = $(window).scrollTop();
	if (a>110) {
		$('.daohang2 .navbar').addClass('navbar-fixed-top')
		$('.dh2mobile, .listaa').addClass('navbar-fixed-top')
		$('.daohang2 .navbar').css('background','rgba(255,255,255,0.8)')
	}
	if (a<110) {
		$('.daohang2 .navbar').removeClass('navbar-fixed-top')
		$('.dh2mobile, .listaa').removeClass('navbar-fixed-top')
	}
});
$(window).scroll(function(){
	var b = $(window).scrollTop();
	if (b>110) {
		$('.lista li').css('background','rgba(255,255,255,0.0)')
		$('.listaa').css('background','rgba(255,255,255,0.8)')
		$('.lista').css('background','rgba(255,255,255,0)')
		$('.lista li').css('height','60px')
		$('.yangshi').css('display','none');

	}
	if (b<110) {
		$('.lista li').css('height','120px')
		$('.yangshi').css('display','block');

	}
});

$('.lista li').mouseover(function(){
	var a = $(this).val()
	$(this).css('color','#ED0A2B')
	if (a == 1) {
		$('#a1').attr('src', 'static/myweb/img/shoujic.png' )
	}
	if (a == 2) {
		$('#a2').attr('src', 'static/myweb/img/erjic.png' )
	}
	if (a == 3) {
		$('#a3').attr('src', 'static/myweb/img/kec.png' )
	}
	if (a == 4) {
		$('#a4').attr('src', 'static/myweb/img/xianc.png' )
	}
	if (a == 5) {
		$('#a5').attr('src', 'static/myweb/img/taozhuangc.png' )
	}
	if (a == 6) {
		$('#a6').attr('src', 'static/myweb/img/baoc.png' )
	}
})
$('.lista li').mouseout(function(){
	var a = $(this).val()
	$(this).css('color','#808080')
	if (a == 1) {
		$('#a1').attr('src', 'static/myweb/img/shoujib.png' )
	}
	if (a == 2) {
		$('#a2').attr('src', 'static/myweb/img/erjib.png' )
	}
	if (a == 3) {
		$('#a3').attr('src', 'static/myweb/img/keb.png' )
	}
	if (a == 4) {
		$('#a4').attr('src','static/myweb/img/xianb.png')
	}
	if (a == 5) {
		$('#a5').attr('src', 'static/myweb/img/taozhuangb.png' )
	}
	if (a == 6) {
		$('#a6').attr('src', 'static/myweb/img/baob.png' )
	}
})




















