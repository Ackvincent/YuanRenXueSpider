# YuanRenXueSpider
猿人学爬虫题[ing]

工具：
https://beautifier.io/
https://obfuscator.io/
https://www.bejson.com/

1、第一题 Js混淆源码乱码
var timestamp = Date.parse(new Date()) + 100000000;
var m = oo0O0(timestamp.toString()) + window.f;
var m = window.f;
var m = hex_md5(mwqqppz);
var m = hex_md5(timestamp);

2、第二题 JS混淆---动态Cookie
挂油猴脚本过掉debugger，用Fiddler抓包很容易发现第一次请求返回了一段Js，经典的ob混淆用AST处理后容易找到生成Cookie的位置。

3、第四题 雪碧图
var j_key = '.' + hex_md5(btoa(data.key + data.value).replace(/=/g, '')); 生成对应哪些图片不显示的key
left对应偏移量，在计算时要加上原本img的宽度11px。


后记：
有点后悔毕业后从前端被分配去做了爬虫，工作层面上讲，爬虫绝对不是一个很好的选择【岗位少，学的杂】。
刷完感兴趣的逆向题后彻底放弃爬虫专心做应用开发了，留下痕迹，选择大于努力，这句话永不过时。