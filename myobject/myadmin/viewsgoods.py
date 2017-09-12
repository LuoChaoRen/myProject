from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from myadmin.models import Types,Users,Goods
from PIL import Image
import time,json,os

# ==============后台商品类别信息管理======================
# 浏览商品类别信息
def typeindex(request):
    # 执行数据查询，并放置到模板中
    list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    # 遍历查询结果，为每个结果对象追加一个pname属性，目的用于缩进标题
    for ob in list:
        ob.pname ='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'*(ob.path.count(',')-1)
        # print(list[0].__dict__)
    context = {"typeslist":list}
    return render(request,'myadmin/type/index.html',context)

# 商品类别信息添加表单
def typeadd(request,tid):
    # 获取父类别信息，若没有则默认为根类别信息
    if tid == '0':
        context = {'pid':0,'path':'0,','name':'根类别'}
    else:
        ob = Types.objects.get(id=tid)
        context = {'pid':ob.id,'path':ob.path+str(ob.id)+',','name':ob.name}
    return render(request,'myadmin/type/add.html',context)

#执行商品类别信息添加	
def typeinsert(request):
    try:
        ob = Types()
        ob.name = request.POST['name']
        ob.pid = request.POST['pid']
        ob.path = request.POST['path']
        ob.save()
        context = {'info':'添加成功！'}
    except:
        
        context = {'info':'添加失败！'}

    return render(request,"myadmin/type/info.html",context)

# 执行商品类别信息删除
def typedel(request,tid):
    try:
        # 获取被删除商品的子类别信息量，若有数据，就禁止删除当前类别
        row = Types.objects.filter(pid=tid).count()
        if row > 0:
            context = {'info':'删除失败：此类别下还有子类别！'}
            return render(request,"myadmin/type/info.html",context)
        ob = Types.objects.get(id=tid)
        ob.delete()
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/type/info.html",context)

# 打开商品类别信息编辑表单
def typeedit(request,tid):
    try:
        ob = Types.objects.get(id=tid)
        context = {'type':ob}
        return render(request,"myadmin/type/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
    return render(request,"myadmin/type/info.html",context)

# 执行商品类别信息编辑
def typeupdate(request,tid):
    try:
        ob = Types.objects.get(id=tid)
        ob.name = request.POST['name']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myadmin/type/info.html",context)


    

#====================商品管理=========================================
# 浏览商品

def goodsindex(request,ids):
    # 执行数据查询，并放置到模板中
    list =Goods.objects.all()
    context = {"goodslist":list}
    #return HttpResponse(list)
    return render(request,'myadmin/goods/index.html',context)

# 商品信息添加表单
def goodsadd(request):
    list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    context = {"typelist":list}
    return render(request,"myadmin/goods/add.html",context)
    
def goodsinsert(request):
    try:

        myfile = request.FILES.get('pic',None)
        if not myfile:
            return HttpResponse('没有上传文件信息')
        filename = str(time.time())+'.'+myfile.name.split('.').pop()
        destination = open(os.path.join('./static/goods/',filename),'wb+')
        for chunk in myfile.chunks():
            destination.write(chunk)
        destination.close()
         # 执行图片缩放
        im = Image.open("./static/goods/"+filename)
        # 缩放到375*375:
        im.thumbnail((375, 375))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/goods/"+filename, 'jpeg')
        # 缩放到220*220:
        im.thumbnail((220, 220))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/goods/m_"+filename, 'jpeg')
        # 缩放到220*220:
        im.thumbnail((100, 100))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/goods/s_"+filename, 'jpeg')




        ob = Goods()
        ob.typeid =request.POST['typeid']
        ob.goods =request.POST['goods']
        ob.company =request.POST['company']
        ob.descr =request.POST['descr']
        ob.price =request.POST['price']
        ob.picname =filename
        ob.state =request.POST['state']
        ob.store =request.POST['store']
        ob.num =request.POST['num']
        ob.clicknum =request.POST['clicknum']
        ob.addtime = time.time()

        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}
    return render(request,"myadmin/goods/info.html",context)

def goodsdel(request,uid):
    try:
        ob = Goods.objects.get(id = uid)
        ob.delete()
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/goods/info.html",context)
def goodsedit(request,uid):
    try:
        ob = Goods.objects.get(id = uid)
        context = {'goods':ob}
        return render(request,"myadmin/goods/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
        return render(request,"myadmin/goods/info.html",context)
def goodsupdate(request,uid):
    try:
        ob = Goods.objects.get(id = uid)
        ob.typeid =request.POST['typeid ']
        ob.goods =request.POST['goods ']
        ob.company =request.POST['company ']
        ob.descr =request.POST['descr ']
        ob.price =request.POST['price ']
        ob.picname =request.POST['picname ']
        ob.state =request.POST['state ']
        ob.store =request.POST['store ']
        ob.num =request.POST['num ']
        ob.clicknum =request.POST['clicknum ']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}

    return render(request,"myadmin/goods/info.html",context)

