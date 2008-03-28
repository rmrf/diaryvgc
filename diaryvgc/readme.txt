作者: ryan.qian@gmail.com 美金

脚本用途：将VIM Calendar 插件生成的Diary同步到Google Calendar 。

编写动机：一直以来我都用Google Calendar记录每日流水帐，记录每一天都做了什么。以前工作的时候，这个习惯非常好，尤其是在定期给客户写维护报告的时候。一些细节的琐碎事情都能借助Google Calendar的搜索功能准确定位时间。缺点就是要联网的时候才能写，否则就要临时编辑个文件，时间久了，想要从这些乱七八糟的本地文件里面找到有用的信息真是痛苦。最近使用了VIM Calendar插件，发现可以写diary，记录流水帐再好不过。缺点就是检索和查看都比较困难，于是就萌生了同步diary到Google Calendar的想法。

运行平台： Unix/Linux/windows

脚本原理：
VIM Calendar插件会在用户目录下的diary目录中按照日期的目录结构生成日记文本，如: /home/money/diary/2008/3/21.cal,每一个文件代表一天的日记。脚本会扫描/home/money/diary目录下的文件，并生成/home/money/diary/vimlog.txt文件作为记录，随后依次上传每个文件的内容到Google Calendar。当然事先要有一个Google Calendar的帐号提供给脚本。为了不与Google Calendar默认的日历冲突(Primary)，脚本会在自动创建一个Title为”VIM”的子日历，随后所有的操作都是在此子日历上起作用。如上传diary和删除diary。
上传diary的过程中使用的Google Gdata的python API。

脚本运行：
./diaryvgc.py --user=username --pw=password --dir=/home/money/diary [-d] -h --help
--user 指定Google Calendar Account的用户名，不必加后面的@gmail.com后缀
--password 指定Google Calendar Account用户的密码，没必要加引号
--dir 指定diary存放的目录，因为就这一个参数，脚本就没有使用配置文件了。并且配置文件存放Google Account的密码也并不安全。
-d 这个是可选参数，如果不使用，则同步diary到Google Calendar。如果指定了-d 则将 Google Calendar的VIM子日历中条目全部删除。
-h 或--help 打印usage

上传diary:
./diaryvgc.py --user=username --pw=password --dir=/home/money/diary
删除Google Calendar中 VIM子Calendar中的所有条目:
./diaryvgc.py --user=username --pw=password --dir=C:\diary -d

说明：
1.支持增量同步。第一次运行时将所有diary同步到Google Calendar，随后只检查新增的diary。这个功能依靠文件vimlog.txt中的记录实现。
2.需要Google Gdata Pytho API支持。现已经把脚本所需的package一起放到程序里面了。只要在Linux下有python(应该都有吧)，就没问题了。
3.diary以’All Day’的形式加入到Google Calendar中。避免了Google Calendar自动分析diary，造成上传日记内容不完整的情况。
4.因未加入同步控制，所以启动后会将diary全部upload到Google Calendar。如果你的diary很多的话，要耐心，因为它的速度依赖于网络。

后期计划：
1, 增加windows平台支持(已经支持)
2, 增加Diary修改的检测,修改后的diary可以同步到Google Calendar。
3, 增加同步控制

脚本下载：

http://code.google.com/p/diaryvgc/downloads/list

相关资源：
VIM Calendar 插件下载: http://www.vim.org/scripts/script.php?script_id=52
Google Gdata API : http://code.google.com/apis/gdata/
