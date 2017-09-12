from django.shortcuts import render
#商城前端界面布局
def index(request):

    return  render(request,"myweb/index.html")

# 商品信息列表页展示
def list(request):

    return  render(request,"myweb/list.html")
    
# 商品信息详情页展示
def xiangq(request):

    return  render(request,"myweb/xiangq.html")
    
def dengl(request):

    return  render(request,"myweb/dengl.html")
    
    
def gouw(request):

    return  render(request,"myweb/gouw.html")
  