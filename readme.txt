1.4�汾���£�

1, ����update���ܣ��޸Ĺ���diary������ִ��diaryvgc.py��ʱ�򣬻��Զ���������ͬ�����������ϡ��˹���ʹ�����µ�vimlog.txt��ʽ�����ļ��м�����md5У���롣
2, �����˳�ͻ��⣬��ֹ�ظ���Google Calendar�ϴ�diary��
3, �����˳����ļ���ʽ������������һ���ˡ� 
4, �޸��˳���ִ�еĲ�����-u �û��� -p ���� -d ·�� [-D] (�Ƿ�ɾ��) 



�ű���;����VIM Calendar ������ɵ�Diaryͬ����Google Calendar ��

��д������һֱ�����Ҷ���Google Calendar��¼ÿ����ˮ�ʣ���¼ÿһ�춼����ʲô��������ʱ�����ϰ�߷ǳ��ã��������ڶ��ڸ��ͻ�дά�������ʱ��һЩϸ�ڵ��������鶼�ܽ���Google Calendar����������׼ȷ��λʱ�䡣ȱ�����Ҫ������ʱ�����д�������Ҫ��ʱ�༭���ļ���ʱ����ˣ���Ҫ����Щ���߰���ı����ļ������ҵ����õ���Ϣ����ʹ�ࡣ���ʹ����VIM Calendar��������ֿ���дdiary����¼��ˮ���ٺò�����ȱ����Ǽ����Ͳ鿴���Ƚ����ѣ����Ǿ�������ͬ��diary��Google Calendar���뷨��

����ƽ̨�� Unix/Linux/windows

�ű�ԭ��
VIM Calendar��������û�Ŀ¼�µ�diaryĿ¼�а������ڵ�Ŀ¼�ṹ�����ռ��ı�����: /home/money/diary/2008/3/21.cal,ÿһ���ļ�����һ����ռǡ��ű���ɨ��/home/money/diaryĿ¼�µ��ļ���������/home/money/diary/vimlog.txt�ļ���Ϊ��¼����������ϴ�ÿ���ļ������ݵ�Google Calendar����Ȼ����Ҫ��һ��Google Calendar���ʺ��ṩ���ű���Ϊ�˲���Google CalendarĬ�ϵ�������ͻ(Primary)���ű������Զ�����һ��TitleΪ��VIM������������������еĲ��������ڴ��������������á����ϴ�diary��ɾ��diary��
�ϴ�diary�Ĺ�����ʹ�õ�Google Gdata��python API��

�ű����У�
./diaryvgc.py -u username -p password -d /home/money/diary [-D] -h --help
-u ָ��Google Calendar Account���û��������ؼӺ����@gmail.com��׺
-p ָ��Google Calendar Account�û������룬û��Ҫ������
-d ָ��diary��ŵ�Ŀ¼ �� -d /home/money/diary
-D ����ǿ�ѡ�����������ʹ�ã���ͬ��diary��Google Calendar�����ָ����-D �� Google Calendar��VIM����������Ŀȫ��ɾ����
-h ��--help ��ӡusage
��Ϊ�������٣��ű���û��ʹ�������ļ��ˡ����������ļ����Google Account������Ҳ������ȫ��

�ϴ�diary:
    ./diaryvgc.py -u username -p password -d /home/money/diary
ɾ��Google Calendar�� VIM��Calendar�е�������Ŀ:
    ./diaryvgc.py -u username -p password -d C:\diary -D

˵����
1.֧������ͬ������һ������ʱ������diaryͬ����Google Calendar�����ֻ���������diary��������������ļ�vimlog.txt�еļ�¼ʵ�֡�
  ���Google Calendar���Ѿ����ڣ������������ظ������ݡ�
2.��ҪGoogle Gdata Python API֧�֡����Ѿ��ѽű������packageһ��ŵ����������ˡ�ֻҪ��Linux����python(Ӧ�ö��а�)����û�����ˡ�
3.diary�ԡ�All Day������ʽ���뵽Google Calendar�С�������Google Calendar�Զ�����diary������ϴ��ռ����ݲ������������
4.�����һ�����н����δ�ϴ��������ռ�һ�����ϴ���������diary�ܶ�Ļ���Ҫ���ģ���Ϊ�����ٶ����������硣
5.��Diary�����ϴ���Google Calendar��Ŀ��Description(����)�У���������Ŀ��title,title�н������ժҪ����,�����˲鿴����������󡣾�����Google Calendar���������ܺ�����Ŀ��Description������Ľ��󣬶Խϴ��Diary����ʮ��������

���ڼƻ���
1, ����Diary�޸ĵļ��,�޸ĺ��diary����ͬ����Google Calendar��(�Ѿ�֧��)

�ű����أ�

http://code.google.com/p/diaryvgc/downloads/list

�����Դ��
VIM Calendar �������: http://www.vim.org/scripts/script.php?script_id=52
Google Gdata API : http://code.google.com/apis/gdata/
