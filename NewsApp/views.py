from django.shortcuts import render, redirect
from .models import NewsType, NewsInfo


def Index(request):
    NewsType.objects.filter().delete()
    NewsInfo.objects.filter().delete()

    NewsType.objects.create(tName='体育')
    NewsType.objects.create(tName='娱乐')
    NewsType.objects.create(tName='科技')
    NewsType.objects.create(tName='财经')
    NewsType.objects.create(tName='军事')
    NewsType.objects.create(tName='国际')

    nty = NewsType.objects.filter(tName='体育').first()
    NewsInfo.objects.create(nTitle='CBA：北控VS苏州', nAuthor='搜狐新闻', nContent='两队上赛季交锋记录', nStatus=0, tid=nty)
    NewsInfo.objects.create(nTitle='德甲：拜仁VS沃尔夫斯堡', nAuthor='搜狐新闻', nContent='如今沃尔夫斯堡排名积分榜', nStatus=0, tid=nty)
    NewsInfo.objects.create(nTitle='足球', nAuthor='搜狐新闻', nContent='C罗再遭KO！',  nStatus=0, tid=nty)
    NewsInfo.objects.create(nTitle='林书豪', nAuthor='搜狐新闻', nContent='五棵松看台喊林书豪', nPubDateTime='2019-12-21', nStatus=0, tid=nty)

    nyl = NewsType.objects.filter(tName='娱乐').first()
    NewsInfo.objects.create(nTitle='杨幂恋情曝光？', nAuthor='搜狐娱乐', nContent='疯狂点赞微博承认与杨幂恋情？',  nStatus=0, tid=nyl)

    nkj = NewsType.objects.filter(tName='科技').first()
    NewsInfo.objects.create(nTitle='5G时代', nAuthor='科技蜀黍', nContent='5G时代来临',  nStatus=0, tid=nkj)

    ncj = NewsType.objects.filter(tName='财经').first()
    NewsInfo.objects.create(nTitle='谷歌罚款', nAuthor='央视网', nContent='开出个罚单？',  nStatus=0, tid=ncj)

    njs = NewsType.objects.filter(tName='军事').first()
    NewsInfo.objects.create(nTitle='中美', nAuthor='环球网', nContent='杨毅：中美关系的真正拐点',  nStatus=0, tid=njs)

    ngj = NewsType.objects.filter(tName='国际').first()
    NewsInfo.objects.create(nTitle='特朗普', nAuthor='人民网', nContent='美国特朗普正式宣布成立坦克军',  nStatus=0, tid=ngj)

    return render(request, 'Index.html')


def Show(request):
    ni = NewsInfo.objects.all()
    if request.method == 'GET':
        return render(request, 'Show.html', {'ni': ni})
    else:
        val = request.POST.get('select')
        fir = NewsType.objects.filter(tName=val).first()
        all = NewsInfo.objects.filter(tid=fir).all()
        return render(request, 'Show.html', {'all': all, 'val': val})


def Delete(request, id):
    NewsInfo.objects.filter(id=id).delete()
    return redirect(Show)


def Add(request):
    if request.method == 'GET':
        return render(request, 'Add.html')
    else:
        tName = request.POST.get('tName')
        
        nTitle = request.POST.get('nTitle')
        nAuthor = request.POST.get('nAuthor')
        nStatus = request.POST.get('nStatus')
        if nStatus == '未审核':
            nStatus = 0
        else:
            nStatus = 1
        nContent = request.POST.get('nContent')
        
        nt = NewsType.objects.filter(tName=tName).first()
        if nt:
            NewsInfo.objects.create(nTitle=nTitle, nAuthor=nAuthor, nStatus=nStatus, nContent=nContent, tid=nt)
        else:
            new_nt = NewsType.objects.create(tName=tName)
            NewsInfo.objects.create(nTitle=nTitle, nAuthor=nAuthor, nStatus=nStatus, nContent=nContent, tid=new_nt)

        return redirect(Show)
