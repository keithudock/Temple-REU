import cmd
from ravel.app import AppConsole

class LinksConsole(AppConsole):
	def do_addlink(self, line):
		"""Adds a link between two nodes, must use id number rather than node name 
Format: addlink [id1] [id2]"""
		args = line.split()
		if len(args) != 2:
			print "Invalid Syntax"
			return

		node1 = str(args[0])
		node2 = str(args[1])
		try:
			sid = []
			sid.append(str(self.db.cursor.execute("SELECT sid"
					       " FROM tp;")))
			nid = str(self.db.cursor.execute("SELECT nid"
					       " FROM tp;"))
			hostid = str(self.db.cursor.execute("SELECT hid"
							  " FROM hosts;"))
						       
			if node1 in sid and node2 in nid:
				print "Already Linked"
				return
			elif node1 in hostid or node2 in hostid:
				self.db.cursor.execute("INSERT INTO tp (sid, nid, ishost, isactive)"
						       "VALUES ({0},{1},1,1);".format(node1, node2));
				self.db.cursor.execute("INSERT INTO tp (sid, nid, ishost, isactive)"
						       "VALUES ({0},{1},1,1);".format(node2, node1));
			else:
				self.db.cursor.execute("INSERT INTO tp (sid, nid, ishost, isactive)"
						       "VALUES ({0},{1},0,1);".format(node1, node2));
				self.db.cursor.execute("INSERT INTO tp (sid, nid, ishost, isactive)"
						       "VALUES ({0},{1},0,1);".format(node2, node1));

		except Exception, e:
			print "Link not Added", e
			return

		print "Success link added"


	def do_dellink(self, line):
		"""Deletes a link between two nodes, must use id number rather than node name 
Format: addlink [id1] [id2]"""
		args = line.split()
		if len(args) != 2:
			print "Invalid Syntax"
			return

		node1 = args[0]
		node2 = args[1]
		try:
			self.db.cursor.execute("DELETE FROM tp WHERE "
					       "sid={0} AND nid={1};".format(node1, node2));
			self.db.cursor.execute("DELETE FROM tp WHERE "
					       "sid={0} AND nid={1};".format(node2, node1));

			self.db.cursor.execute("DELETE FROM cf WHERE "
					       "pid={0} OR pid={1};".format(node2, node1));
			self.db.cursor.execute("DELETE FROM cf WHERE "
					       "sid={0} OR sid={1};".format(node2, node1));
			self.db.cursor.execute("DELETE FROM cf WHERE "
					       "nid={0} OR nid={1};".format(node2, node1));

		except Exception, e:
			print "Link not Deleted", e
			return

		print "Success link deleted"
						


shortcut = "link"
description = "changes links between nodes"
console = LinksConsole
