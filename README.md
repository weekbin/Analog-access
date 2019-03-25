# Analog-access

## 简介
* 针对本学期网络营销作业，制作了一个可以自动化访问网站的脚本，功能可以拓展(有兴趣的同学可以自行研究)，后期会加上自动化访问微信与微博网店的部分。
* 使用python selenium库来模拟测试浏览访问我们需要访问的内容。
* 使用了前人写好的代理池,[ProxyPool](https://github.com/Python3WebSpider/ProxyPool)；使用了前人的分享，我如今将其部署在了我的服务器上，需要使用的小伙伴可以直接使用[my-ProxyPool](http://www.weekbin.xyz:5555/random);如果使用遇到了问题可以参考下前人经验，或者也可以直接联系我。
* 因为代理池是免费的，所以速度可能是非常慢的，成功率可能也不高，如果自己有代理，可以直接使用自己的。
* 本脚本的初衷是可以模拟点击等各种事件，提高百度统计的各种转化率，但是在实际运用过程中，因为每个人的需求不尽相同，所以没有做出统一的接口。我后期会贴出方法，有需求的同学可以自行研究更改。
* 本脚本适用于windows系统，linux以及mac系统虽也可以使用，但是坑比较多，不推荐。因本人能力等原因，脚本存在一些问题，所以也不推荐吧脚本部署在服务器上。

## 使用方式
在使用之前，需要安装chromedriver和chrome浏览器，因为涉及到chromedriver和Chrome每个小伙伴的版本不同，所以这里请大家自行安装。（这一点很重要，没有这个环境，脚本无法运行；如果觉得麻烦，可以自行用request库来写请求）    
如果你的电脑上已经安装了git，可以使用如下命令,如果没有git你可以直接下载压缩包到本地    
`mkdir analog-access`    
`cd analog-access/`    
`git clone https://github.com/weekbin/Analog-access.git`    
请确保你的电脑安装了python环境以及pip    
`pip install -r requirements.txt`    
在正式运行之前，请在url.py中调整url去访问你想访问的地址。    
最后运行即可    
`python package.py`    
如需退出，直接CTRL + C退出即可    