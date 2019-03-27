# Analog-access

## 简介
针对本学期网络营销作业，制作了一个可以自动化访问网站的脚本，功能可以拓展(有兴趣的同学可以自行研究)，后期会加上自动化访问微信与微博网店的部分。  

使用python selenium库来模拟测试浏览访问我们需要访问的内容。 

使用了前人写好的[代理池](https://github.com/Python3WebSpider/ProxyPool)。
我如今将其部署在了我的服务器上，需要使用的小伙伴可以直接使用[我的代理池](http://www.weekbin.xyz:5555/random)    

因为代理池是免费的，所以速度可能是非常慢的，成功率可能也不高，如果自己有代理，可以直接使用自己的。  

本脚本的初衷是可以模拟点击等各种事件，提高百度统计的各种转化率，但是在实际运用过程中，因为每个人的需求不尽相同，所以没有做出统一的接口。我后期会贴出方法，有需求的同学可以自行研究更改。    

本脚本适用于windows系统。linux以及mac系统虽也可以使用，但是坑比较多，不推荐。因本人能力等原因，脚本存在一些问题，所以也不推荐吧脚本部署在服务器上。


## 预装环境
* [Git](https://git-scm.com/)
* [Python 3.0 +](https://www.python.org/downloads/)
* [Chrome](https://www.google.cn/intl/zh-CN/chrome/?brand=CHBD&gclid=CjwKCAjwvuzkBRAhEiwA9E3FUs1mtJwoJcyMftX4NdDr-ZBEPMNPr49XG3V7--HkwVW5cDQVAs1rDxoC7kcQAvD_BwE&gclsrc=aw.ds)
* [ChromeDriver](http://chromedriver.storage.googleapis.com/index.html)
* [ChromeDriver 与 Chrome 版本映射表](https://blog.csdn.net/huilan_same/article/details/51896672)

**注：您下载安装的 `Chrome` 版本需要与 `ChromeDriver`相一致。如果 `ChromeDriver` 链接点不开也可以使用这里的 [`taobao源`](http://npm.taobao.org/mirrors/chromedriver/)。**

## 使用方式
在使用之前，需要安装chromedriver和chrome浏览器，因为涉及到chromedriver和Chrome每个小伙伴的版本不同，所以这里请大家自行安装。

#### 如果你的电脑上已经安装了git，可以使用如下命令,如果没有git你可以直接下载压缩包到本地    
```bash
mkdir analog-access
cd analog-access/
git clone https://github.com/weekbin/Analog-access.git
```
#### 请确保你的电脑安装了python环境以及pip    
```bash
pip install -r requirements.txt
```
#### 在正式运行之前，请在url.py中调整url去访问你想访问的地址。    
```bash
尚未写好的代码块
```
#### 最后运行即可    
```bash
python main.py
``` 
#### 如需退出，直接CTRL + C退出即可    

  
 
 
 