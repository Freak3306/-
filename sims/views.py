import MySQLdb
from django.shortcuts import render, redirect


# Create your views here.
# 图书信息列表处理函数
def index(request):
    book_no = request.GET.get('book_no', '')
    book_name = request.GET.get('book_name', '')

    sql = "SELECT id,book_no,book_name FROM sims_book WHERE 1=1 "
    if book_no.strip() != '':
        sql = sql + " and book_no = '" + book_no+"'"
    if book_name.strip() != '':
        sql = sql + " and book_name = '" + book_name+"'"

    print(sql)
    conn = MySQLdb.connect(host="localhost", user="hzk", passwd="123", db="sms", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        books = cursor.fetchall()
    return render(request, 'book/index.html', {'books': books,
                                                  'book_name':book_name,'book_no':book_no})


# 图书信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'book/add.html')
    else:
        book_no = request.POST.get('book_no', '')
        book_name = request.POST.get('book_name', '')
        conn = MySQLdb.connect(host="localhost", user="hzk", passwd="123", db="sms", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO sims_book (book_no,book_name) "
                           "values (%s,%s)", [book_no, book_name])
            conn.commit()
        return redirect('../')


# 图书信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="hzk", passwd="123", db="sms", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,book_no,book_name FROM sims_book where id =%s", [id])
            book = cursor.fetchone()
        return render(request, 'book/edit.html', {'book': book})
    else:
        id = request.POST.get("id")
        book_no = request.POST.get('book_no', '')
        book_name = request.POST.get('book_name', '')
        conn = MySQLdb.connect(host="localhost", user="hzk", passwd="123", db="sms", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE sims_book set book_no=%s,book_name=%s where id =%s",
                           [book_no, book_name, id])
            conn.commit()
        return redirect('../')


# 图书信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="hzk", passwd="123", db="sms", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM sims_book WHERE id =%s", [id])
        conn.commit()
    return redirect('../')
