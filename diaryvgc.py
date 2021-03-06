#!/usr/bin/python

# Version 1.4
# A script for posting diaries created by VIM Calender to Google Calendar
# Author: Ryan Qian <ryan.qian@gmail.com>

try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar
import atom
import getopt
import os
import sys
import string
import datetime
import re
import codecs
import md5

reload(sys)
sys.setdefaultencoding('utf8')

class CalendarVIM:

    def __init__(self, email, password):
        self.cal_client = gdata.calendar.service.CalendarService()
        self.cal_client.email = email
        self.cal_client.password = password
        self.cal_client.source = 'Google-Calendar_Python_Sample-1.0'
        self.cal_client.ProgrammaticLogin()

    def _PrintUserCalendars(self): 
        feed = self.cal_client.GetAllCalendarsFeed()
        print 'Printing allcalendars: %s' % feed.title.text
        for i, a_calendar in zip(xrange(len(feed.entry)), feed.entry):
            print '\t%s. %s' % (i, a_calendar.title.text,)

    def _PrintOwnCalendars(self):
        feed = self.cal_client.GetOwnCalendarsFeed()
        print 'Printing owncalendars: %s' % feed.title.text
        for i, a_calendar in zip(xrange(len(feed.entry)), feed.entry):
            print '\t%s. %s' % (i, a_calendar.title.text,)

    def _IfVIMCalendar(self):
        feed = self.cal_client.GetOwnCalendarsFeed()
        vim_num = []
        #print 'Check If I have the VIM Calendar in: %s' % feed.title.text
        for i, a_calendar in zip(xrange(len(feed.entry)), feed.entry):
            if a_calendar.title.text=='VIM':
                vim_num.append(a_calendar.id.text[len("http://www.google.com/calendar/feeds/default/owncalendars/full")+1:])
        if len(vim_num) == 1:
            return vim_num[0]
        elif len(vim_num) == 0:
            return None

    def _PrintAllEventsOnDefaultCalendar(self):
        feed = self.cal_client.GetCalendarEventFeed()
        print 'Events on Primary Calendar: %s' % (feed.title.text,)
        for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
            print '\t%s. %s' % (i, an_event.title.text,)

    def _PrintAllEventsOnVIMCalendar(self,muri=''):
        feed = self.cal_client.GetCalendarEventFeed(uri=muri)
        print 'Events on Primary Calendar: %s' % (feed.title.text,)
        for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
            print '\t%s. %s' % (i, an_event.title.text,)

    def _InsertVIMCalendar(self, title='VIM',
        description='This calendar contains VIM Diary items',
        time_zone='Asia/Shanghai', hidden=False, location='China',
        color='#2952A3'): 
        """Creates a new calendar using the specified data."""
        print 'Creating new calendar with title "%s"' % title
        calendar = gdata.calendar.CalendarListEntry()
        calendar.title = atom.Title(text=title)
        calendar.summary = atom.Summary(text=description)
        calendar.where = gdata.calendar.Where(value_string=location)
        calendar.color = gdata.calendar.Color(value=color)
        calendar.timezone = gdata.calendar.Timezone(value=time_zone)  
        if hidden:
            calendar.hidden = gdata.calendar.Hidden(value='true')
        else:
            calendar.hidden = gdata.calendar.Hidden(value='false')

        new_calendar = self.cal_client.InsertCalendar(new_calendar=calendar)
        return new_calendar

    def _InsertEvent(self, title='Insert Event', 
        content='from vim diary', where='China',
        start_time=None, end_time=None, recurrence_data=None,which_calendar='/calendar/feeds/default/private/full'):

        event = gdata.calendar.CalendarEventEntry()
        event.title = atom.Title(text=title)
        event.content = atom.Content(text=content)
        event.where.append(gdata.calendar.Where(value_string=where))
        start_time = start_time
        end_time = start_time
        event.when.append(gdata.calendar.When(start_time=start_time, end_time=end_time))
        new_event = self.cal_client.InsertEvent(event,insert_uri=which_calendar)
        return new_event

    def _InsertSingleEvent(self, title='New VIM Event-single',
        content='from vim diary description', where='China',
        start_time=None, end_time=None,which_calendar='/calendar/feeds/default/private/full'):
        """Uses the _InsertEvent helper method to insert a single event which
        does not have any recurrence syntax specified."""

        new_event = self._InsertEvent(title, content, where, start_time, end_time, 
            recurrence_data=None,which_calendar=which_calendar)
        print "Insert \t"+ start_time +"\t Diary"

    def _DeleteAllVIMEvent(self, dvim_id=''):
        if dvim_id == '':
            print "Sorry, Can not delete this NULL id Calendar's Event"
        else:
            print "Delete All Event at this Goole Calendar ID:\n" + dvim_id
            feed = self.cal_client.GetCalendarEventFeed(uri=dvim_id)
            for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
                print 'Deleting... \t%s. ' % i
                #print 'Deleting... \t%s. %s\n' % (i, an_event.title.text,)
                self.cal_client.DeleteEvent(an_event.GetEditLink().href)

    def Run(self, info="Hi, I am VIM Event",desc='From vim diary description',datetime='',delete='false'):
#   Show what have already in there
#    print "Print All Event at Default Calendar"
#    self._PrintAllEventsOnDefaultCalendar()
#        print "Print All Event at VIM Calendar"
#        self._PrintAllEventsOnVIMCalendar(muri=vim_id)
        if delete == 'true':
            vim_there =  self._IfVIMCalendar()
            if vim_there is None:
                print "NO VIM calendar in your Google Calendar"
                sys.exit(2)
            else:
                vim_id = '/calendar/feeds/'+vim_there+'/private/full'
                self._DeleteAllVIMEvent(dvim_id=vim_id)
    
        if delete == 'false':
            vim_there =  self._IfVIMCalendar()
            if vim_there is None:
                self._InsertVIMCalendar() 
                new_vim_there =  self._IfVIMCalendar()
                new_vim_id = '/calendar/feeds/'+new_vim_there+'/private/full'
                self._InsertSingleEvent(title=info,content=desc,start_time=datetime,which_calendar=new_vim_id)
            else:
                vim_id = '/calendar/feeds/'+vim_there+'/private/full'
                self._InsertSingleEvent(title=info,content=desc,start_time=datetime,which_calendar=vim_id)

    def DateRangeQuery(self, start_date='2007-01-01', end_date='2007-07-01'):
        vim_there =  self._IfVIMCalendar()
        calendar_service = self.cal_client
        query = gdata.calendar.service.CalendarEventQuery(vim_there, 'private', 'full')
        query.start_min = start_date
        query.start_max = end_date 
        feed = calendar_service.CalendarQuery(query)
    #    print 'Date range query for events on Primary Calendar: %s to %s' % (start_date, end_date,)
        for i, an_event in enumerate(feed.entry):
            #print '\t%s. %s' % (i, an_event.title.text,)
            return an_event

    def Update_single(self, event, info='New Updated title',desc='New Updated information'):
        for a_event in event.when:
            print '\n\tDiary at date: %s' % (a_event.start_time,) + ' CHANGED, will be updated right now'
        calendar_service = self.cal_client
        event.title.text = info
        event.content.text = desc
        vim_there =  self._IfVIMCalendar()
        return calendar_service.UpdateEvent(event.GetEditLink().href, event)


    def Code_info(self,t=''):
        info_done = ""
        if sys.platform[:3] == 'win':
            try:
                diaryinfo = open(t).read()
                info_done = unicode(diaryinfo,'cp936')
                #print "=============win===UTF8=============="+tfile
            except Exception,ex:
                diaryinfo = codecs.open(t,'r','gb2312').read()
                info_done = diaryinfo.encode("utf-8")
                #print "============win====GB2312=============="+tfile
        else:
            try:
                diaryinfo = codecs.open(t,'r','gb2312').read()
                info_done = diaryinfo.encode("utf-8")
                #print "=============notwin===GB2312=============="+tfile
            except Exception,ex:
                diaryinfo = open(t).read()
                info_done = diaryinfo
                #print "============notwin====UTF8=============="+tfile
        return info_done


    def md5sum(self,t=''):
        m = md5.new()
        m.update(open(t).read())
        return m.hexdigest()


def main():
    """Runs the CalendarVIM application with the provided username and
    and password values.  Authentication credentials are required.  """
    
    def usage():
        usage_mesg = """ 
python diaryvgc.py [-D] -u=[username] -p=[password] -d=[diarydir] \n 
-D:      If used, Can Delete ALL The Event in Google VIM title Calendar 
-h:      Print This
--help:  Print This
-u=[username]: Google Account,without @gmail.com is fine 
-p=[password]: Google Account Password 
-d=[diarydir]: VIM Calendar Directory,such as /home/username/diary
"""
        print usage_mesg
       
  # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hDd:u:p:", ["help"])
    except getopt.error, msg:
        usage()
        sys.exit(2)
    user = ''
    pw = ''
    delete = 'false'
    diarydir = ''
    # Process options
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o == "-D":
            delete='true'
        elif o == "-u":
            user = a
        elif o == "-p":
            pw = a
        elif o == "-d":
            diarydir = a

    diarylog = diarydir+os.path.sep+'vimlog.txt'

    if user == '' or pw == '' or diarydir == '':
        usage()
        sys.exit(2)
    # Create vim google calendar Instence
    diaryvgc = CalendarVIM(user, pw)
    # For the Big Check if we wanna delete all the event in VIM calendar
    if delete == 'true':
          print "delete all event in vim calendar"
          try:
              if os.path.isfile(diarylog):
                  os.remove(diarylog)
                  print diarylog+" has been deleted"
              else:
                  pass
          except:
              print "Can not delete "+diarylog
          diaryvgc.Run(delete='true')
    
    elif delete == 'false' :
        # I will scan the vim diary directory and insert diary content as event into Google VIM calendar 
        log_dic = {}
        exist_line = []
        exist_md5 = []
        if os.path.isfile(diarylog):
            t = open(diarylog,'r')
            alllines = t.readlines()
            try:
                log_dic = dict([(line.split()) for line in alllines])
                exist_line = log_dic.keys()
                logfile = open(diarylog,'w')
            except ValueError:
                print "Detect you are using OLD version diaryvgc logfile, Upgrading the logfile to LATEST"
                print "Create vim calendar log file at "+ diarydir
                logfile = open(diarylog,'w')
        else:
            print "Create vim calendar log file at "+ diarydir
            logfile = open(diarylog,'w')

        #Check if the diary file scanned is good one
        pattern_lin = r'(\d{4})/(\d{1,2})/(\d{1,2}).cal$'
        pattern_win = r'(\d{4})\\(\d{1,2})\\(\d{1,2}).cal$'
        if sys.platform[:3]=='win':
            pattern = pattern_win
        else:
            pattern = pattern_lin
        #print pattern
        ptime = re.compile(pattern)
        # Walk the Diary Directory for diary files and upload them to Google Calendar
        for (top,dirname,filenames) in os.walk(diarydir):
            for file in filenames:
                tfile = os.path.join(top,file)
                if ptime.search(tfile):
                    (year,month,day) = ptime.search(tfile).groups()
                    dddd = datetime.date(int(year),int(month),int(day))
                    dtime = dddd.isoformat()
                    dtime_plus = (dddd + datetime.timedelta(1)).isoformat()
                    #print tfile+'\t'+dtime
                    #check if the diary nothing in it
                    if os.path.getsize(tfile) == 0:
                        os.remove(tfile)
                    else:
                        exist_it = diaryvgc.DateRangeQuery(start_date=dtime,end_date=dtime_plus)
                        if tfile not in exist_line:  #if I found NEW diary,so....
                            if exist_it:
                                    des_md5 = diaryvgc.md5sum(t=tfile)
                                    log_dic[tfile] = des_md5
                            else:
                                try:
                                    #Generate MD5 sum for every file
                                    des_md5 = diaryvgc.md5sum(t=tfile)
                                    log_dic[tfile] = des_md5
                                    #logfile.write(tfile+'\t'+des_md5+'\n') 
                                    #Try to Guess file encode
                                    info_done = diaryvgc.Code_info(t=tfile)
                                    
                                    dotdot = ''
                                    if info_done[80:] != '':
                                        dotdot='...'
                                    shortdesc = info_done[0:80]+dotdot
                                    longdesc = info_done
                                    diaryvgc.Run(info=shortdesc,desc=longdesc,datetime=dtime)
                                except Exception,ex:
                                    print Exception,':',ex
                                    print "Sorry, something inside your diary I can not upload to Google Calendar"
                        #
                        elif tfile in exist_line:  #if I found OLD diary tfile,so....
                            src_md5 = diaryvgc.md5sum(t=tfile)
                            if src_md5 !=  log_dic.get(tfile):
                                print tfile,"Found md5 diff"
                                u_desc = diaryvgc.Code_info(t=tfile)
                                dotdot = ''
                                if u_desc[80:] != '':
                                    dotdot='...'
                                shortdesc = u_desc[0:80]+dotdot
                                #Get which diary has been changed 
                                u_event = diaryvgc.DateRangeQuery(start_date=dtime,end_date=dtime_plus)
                                                                  
                                #Update diary content to GOOGLE
                                diaryvgc.Update_single(u_event,info=shortdesc,desc=u_desc)
                                log_dic[tfile] = src_md5 # update MD5 sum to vimlog.txt

        for k in log_dic.keys():
            logline = k+"\t"+log_dic[k]+"\n"
            logfile.write(logline)
        logfile.close()

    else:
        usage()

if __name__ == '__main__':
  main()
