#encoding:utf-8
import os

#用以统计的直方图
ct={'剧情':0,'制作':0,'主题':0,'视听':0,'角色':0}

#遍历目录中的文件并存入列表
def eachFile(flist,filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child=os.path.join('%s%s' % (filepath,allDir))
        flist.append(child)

#将目录中的文本写到一个文本文件中
def writeFile(flist,ofile):
    for fr in flist:
        for txt in open(fr,'r'):
            ofile.writelines(txt)

#统计关注点
def focus(filepath, filmpath,count):
    ls = list()
    eachFile(ls,filepath)
    a=open(filepath[:-1]+'txt','w')#词库
    b=open(filmpath,'r')#电影评论
    writeFile(ls,a)
    for key in count:
        if key in filepath:
            tmp=key
    a = open(filepath[:-1] + 'txt', 'r')
    comment= b.readlines()#电影评论字符串
    connet={tmp:a.readlines()}
    for w in connet[tmp]:
        for s in comment:
            if w in s:
                count[tmp] = count[tmp] + 1
    a.close()
    b.close()

focus('/home/lbw/Downloads/词典/主题/','/home/lbw/Downloads/太空旅客.txt',ct)
focus('/home/lbw/Downloads/词典/制作/','/home/lbw/Downloads/太空旅客.txt',ct)
focus('/home/lbw/Downloads/词典/视听/','/home/lbw/Downloads/太空旅客.txt',ct)
focus('/home/lbw/Downloads/词典/角色/','/home/lbw/Downloads/太空旅客.txt',ct)
focus('/home/lbw/Downloads/词典/剧情/','/home/lbw/Downloads/太空旅客.txt',ct)



for key in ct:
    print key, ct[key]
