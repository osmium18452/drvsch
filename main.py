# coding=utf-8
import pymysql
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from mainwindow import Ui_Form


class Window(QMainWindow, Ui_Form):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent=parent)
		
		# connect the database
		try:
			self.conn = pymysql.connect(host="10.70.157.47",
										user="admin",
										passwd="fushuai",
										charset="utf8")
			self.cur = self.conn.cursor()
			self.conn.select_db("drive_school")
		except:
			print("Database connecting failed. Pleases check your database configuration!")
			exit(0)
		
		self.setupUi(self)
		self.addCoachButton.clicked.connect(self.addCoach)
		self.addStdButton.clicked.connect(self.addStudent)
		self.addFieldButton.clicked.connect(self.addField)
		self.addExamButton.clicked.connect(self.addExam)
		self.addLessButton.clicked.connect(self.addLesson)
		
		self.presExamButton.clicked.connect(self.presExam)
		self.presClassButton.clicked.connect(self.presLess)
		self.presFieldButton.clicked.connect(self.presField)
		
		self.dispCoach.clicked.connect(self.displayCoach)
		self.dispStd.clicked.connect(self.displayStudent)
		self.dispLess.clicked.connect(self.displayLessons)
		self.dispExam.clicked.connect(self.displayExam)
		self.dispField.clicked.connect(self.displayField)
		
		self.dispBatchExam.clicked.connect(self.displayBatchExam)
		self.dispBatchLess.clicked.connect(self.displayBatchLesson)
		
		self.consult.clicked.connect(self.cons)
		self.cancel.clicked.connect(self.canc)
	
	def __del__(self):
		self.close()
		self.conn.close()
	
	# setup the window's logic
	
	@pyqtSlot()
	def addCoach(self):
		cno = self.coachNum.text()
		cname = self.coachName.text()
		if cno == "" or cname == "":
			self.displayBox.append("请输入教练的姓名和编号！")
			return
		try:
			self.cur.execute("""
			INSERT INTO coach(cno, cname)
			VALUES ('%s','%s')""" % (cno, cname))
			self.conn.commit()
			self.displayBox.append("添加成功！")
		except:
			self.displayBox.append("教练编号已被注册！")
	
	@pyqtSlot()
	def addStudent(self):
		sno = self.stdNum.text()
		sname = self.stdName.text()
		if sno == "" or sname == "":
			self.displayBox.append("请输入学生的姓名和编号！")
			return
		try:
			self.cur.execute("""
			INSERT INTO student(sno, sname)
			VALUES ('%s','%s')""" % (sno, sname))
			self.conn.commit()
			self.displayBox.append("添加成功！")
		except:
			self.displayBox.append("学生学号已经被注册！")
	
	@pyqtSlot()
	def addField(self):
		fno = self.fieldNum.text()
		floc = self.fieldLocation.text()
		fcap = self.fieldCapacity.text()
		if fno == "" or floc == "" or fcap == "":
			self.displayBox.append("请输入完整的场地信息！")
			return
		try:
			self.cur.execute("""
			INSERT INTO field(fno, floc, fcap)
			VALUES ('%s','%s','%s')""" % (fno, floc, fcap))
			self.conn.commit()
			self.displayBox.append("添加成功！")
		except pymysql.Error as err:
			print(err.args)
			self.displayBox.append("场地编号已经被注册！")
	
	@pyqtSlot()
	def addExam(self):
		eno = self.examNum.text()
		efield = self.examField.text()
		etime = self.examDate.text()
		if eno == "" or efield == "" or etime == "":
			self.displayBox.append("请输入完整的考试信息！")
			return
		try:
			self.cur.execute("""
			INSERT INTO exam(eno, etime, fno)
			VALUES ('%s','%s','%s')""" % (eno, etime, efield))
			self.conn.commit()
			self.displayBox.append("添加成功！")
		except pymysql.Error as err:
			print(err.args)
			self.displayBox.append("考试编号已被注册！")
	
	@pyqtSlot()
	def addLesson(self):
		lno = self.lessNum.text()
		fno = self.lessField.text()
		cno = self.lessCoach.text()
		if lno == "" or fno == "" or cno == "":
			self.displayBox.append("请输入完整的课程信息！")
			return
		try:
			self.cur.execute("""
			INSERT INTO lesson(lno, fno, cno)
			VALUES('%s','%s','%s')""" % (lno, fno, cno))
			self.conn.commit()
			self.displayBox.append("添加成功！")
		except :
			# print(e.args)
			self.displayBox.append("课程编号已被注册！")
	
	@pyqtSlot()
	def presExam(self):
		sno = self.examStdNum.text()
		eno = self.examExamNum.text()
		if sno == "" or eno == "":
			self.displayBox.append("请输入完整的考试预约信息！")
			return
		try:
			self.cur.execute("""
			INSERT INTO SE(sno,eno)
			VALUES('%s','%s')""" % (sno, eno))
			self.conn.commit()
			self.displayBox.append("预约成功！")
		except:
			self.displayBox.append("预约失败，请检查填入信息是否有误！")
	
	@pyqtSlot()
	def presLess(self):
		sno = self.lessStdNum.text()
		lno = self.lessLessNum.text()
		if sno == "" or lno == "":
			self.displayBox.append("请输入完整的课程预约信息！")
			return
		try:
			self.cur.execute("""
			INSERT INTO SL(sno,lno)
			VALUES ('%s','%s')""" % (sno, lno))
			self.conn.commit()
			self.displayBox.append("预约成功！")
		except pymysql.Error as err:
			print(err.args)
			self.displayBox.append("预约失败，请检查输入的信息是否有误！")
	
	@pyqtSlot()
	def presField(self):
		sno = self.fieldStdNum.text()
		fno = self.fieldFieldNum.text()
		date = self.fieldTime.text()
		if sno == "" or fno == "" or date == "":
			self.displayBox.append("请输入完整的场地预约信息！")
			return
		try:
			self.cur.execute("""
			INSERT INTO SF(sno, fno, sftime)
			VALUES('%s','%s','%s')""" % (sno, fno, date))
			self.conn.commit()
			self.displayBox.append("预约成功！")
		except:
			self.displayBox.append("预约失败，请检查输入的信息是否有误！")
	
	@pyqtSlot()
	def displayCoach(self):
		self.cur.execute("""
		SELECT * FROM coach""")
		result = self.cur.fetchall()
		if len(result)==0:
			self.displayBox.append("没有注册的教练")
			return
		for items in result:
			cno, cname = items
			self.displayBox.append("教练编号：%s" % cno)
			self.displayBox.append("教练姓名：%s" % cname)
			self.displayBox.append("")
	
	@pyqtSlot()
	def displayStudent(self):
		self.cur.execute("""
		SELECT * FROM student""")
		result = self.cur.fetchall()
		if len(result)==0:
			self.displayBox.append("没有注册的学生")
			return
		for items in result:
			sno, sname = items
			self.displayBox.append("学生编号：%s" % sno)
			self.displayBox.append("学生姓名：%s" % sname)
			self.displayBox.append("")
	
	@pyqtSlot()
	def displayLessons(self):
		self.cur.execute("""
		SELECT * FROM lesson""")
		result = self.cur.fetchall()
		if len(result)==0:
			self.displayBox.append("没有添加的课程")
			return
		for items in result:
			lno, fno, cno = items
			self.displayBox.append("课程编号：%s" % lno)
			self.displayBox.append("场地编号：%s" % fno)
			self.displayBox.append("教练编号：%s" % cno)
			self.displayBox.append("")
	
	@pyqtSlot()
	def displayExam(self):
		self.cur.execute("""
		SELECT * FROM exam""")
		result = self.cur.fetchall()
		if len(result)==0:
			self.displayBox.append("没有添加的考试")
			return
		for items in result:
			eno, fno, date = items
			self.displayBox.append("考试编号：%s" % eno)
			self.displayBox.append("考场编号：%s" % fno)
			self.displayBox.append("考试时间：%s" % date)
			self.displayBox.append("")
	
	@pyqtSlot()
	def displayField(self):
		self.cur.execute("""
			SELECT * FROM field""")
		result = self.cur.fetchall()
		if len(result)==0:
			self.displayBox.append("没有添加的场地")
			return
		for items in result:
			fno, floc, fcap = items
			self.displayBox.append("场地编号：%s" % fno)
			self.displayBox.append("场地位置：%s" % floc)
			self.displayBox.append("场地容量：%s" % fcap)
			self.displayBox.append("")
	
	@pyqtSlot()
	def displayBatchLesson(self):
		self.cur.execute("""SELECT fno, COUNT(DISTINCT sno)
		                            FROM SL, lesson
		                            WHERE SL.lno = lesson.lno
		                            GROUP BY fno
		                            """)
		result = self.cur.fetchall()
		if len(result)==0:
			self.displayBox.append("没有添加课程")
			return
		for items in result:
			time, count = items
			self.displayBox.append("上课场地：%s" % time)
			self.displayBox.append("上课人数：%s" % count)
			self.displayBox.append("")
	
	@pyqtSlot()
	def displayBatchExam(self):
		self.cur.execute("""SELECT etime, COUNT(DISTINCT sno)
			                            FROM SE, exam
			                            WHERE SE.eno = exam.eno
			                            GROUP BY etime
			                            """)
		result = self.cur.fetchall()
		if len(result)==0:
			self.displayBox.append("没有添加考试")
			return
		for items in result:
			time, count = items
			self.displayBox.append("考试时间：%s" % time)
			self.displayBox.append("考试人数：%s" % count)
			self.displayBox.append("")
	
	@pyqtSlot()
	def cons(self):
		sno = self.hahaha.text()
		if sno == "":
			self.displayBox.append("请输入学号！")
		else:
			self.displayBox.append('场地预约：')
			self.cur.execute("""SELECT DISTINCT SF.fno, sftime, floc
			                                FROM SF, field
			                                WHERE SF.sno = '%s' AND
			                                      SF.fno = field.fno
			                                """ % sno)
			results = self.cur.fetchall()
			if results is None or len(results) == 0:
				self.displayBox.append('没有预约场地！')
			else:
				for item in results:
					fno, sftime, floc = item
					self.displayBox.append('场地编号：%s' % fno)
					self.displayBox.append('预约时间：%s' % sftime)
					self.displayBox.append('场地位置：%s' % floc)
					self.displayBox.append('')
			self.displayBox.append('课程预约：')
			self.cur.execute("""SELECT DISTINCT SL.lno, floc, cname
											FROM SL, lesson, field, coach
			                                WHERE SL.sno = '%s' AND
			                                      SL.lno = lesson.lno AND
			                                      lesson.fno = field.fno AND
			                                      lesson.cno = coach.cno
			                                """ % sno)
			results = self.cur.fetchall()
			if results is None or len(results) == 0:
				self.displayBox.append('没有预约课程！')
			else:
				for item in results:
					lno, floc, cname = item
					self.displayBox.append('课程编号：%s' % lno)
					self.displayBox.append('上课场地：%s' % floc)
					self.displayBox.append('上课教练：%s' % cname)
					self.displayBox.append('')
			self.displayBox.append('考试预约：')
			self.cur.execute("""SELECT DISTINCT SE.eno, etime, floc
			                                FROM SE, exam, field
			                                WHERE SE.sno = '%s' AND
			                                      SE.eno = exam.eno AND
			                                      exam.fno = field.fno
			                                """ % sno)
			results = self.cur.fetchall()
			if results is None or len(results) == 0:
				self.displayBox.append('没有预约考试！')
			else:
				for item in results:
					eno, etime, floc = item
					self.displayBox.append('考试编号：%s' % eno)
					self.displayBox.append('考试时间：%s' % etime)
					self.displayBox.append('考试场地：%s' % floc)
					self.displayBox.append('')
	
	@pyqtSlot()
	def canc(self):
		sno = self.hahaha.text()
		time = self.lalala.text()
		if (sno == '' or time == ''):
			self.displayBox.append('输入内容为空！')
		else:
			self.cur.execute("""DELETE
	                                FROM SF
	                                WHERE sno = '%s' AND sftime = '%s'
	                                """ % (sno, time))
			self.cur.execute("""DELETE
	                                FROM SE
	                                WHERE sno = '%s' AND eno IN
	                                    (
	                                    SELECT eno
	                                    FROM exam
	                                    WHERE etime = '%s'
	                                    )
	                                """ % (sno, time))
			self.conn.commit()
			self.displayBox.append("预约删除成功！")


if __name__ == '__main__':
	app = QApplication([])
	window = QMainWindow()
	w = Window()
	w.show()
	sys.exit(app.exec_())
