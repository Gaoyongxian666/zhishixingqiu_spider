# zhishixingqiu_sprider
爬虫，爬取知识星球网页版
 
requests实现


他是js请求数据，url中的参数end_time就是上次请求最后一个主题的创造时间。

要加上头信息：当你登陆完成之后，复制头信息，主要就是这个authorization参数，加到get请求中，就可以获取相应的数据——json形式。
 
我最后保存的是一个json文件，解析即可。
