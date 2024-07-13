// 定义模板template
function template(info){
	return `
	<div class="btn" id="${info['id']}">
		${info['title']}
	</div>
	`
}
var $btnList=$('.btn_list')
var $data=data
for(var i=0;i<$data.length;i++){
	$btn=template($data[i])
	$btnList.append($btn)
}
// 初始化页面信息
$cur_url_id=parseInt(location.pathname.split('/')[1])
$cur_data=data[$cur_url_id]
// console.log($cur_data)
$('title').text($cur_data['title'])
$('.header').text($cur_data['title'])
$('.panel').append(`<p>${$cur_data['des']}</p>`)
$('.panel').append(`<p>${$cur_data['question']}</p>`)
$('.btn').on('click',function(){
	var $id=$(this).attr('id')
	console.log($id)
	window.location.pathname=$id
})