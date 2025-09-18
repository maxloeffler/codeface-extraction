# This file is part of codeface-extraction, which is free software: you
# can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Copyright 2010, 2011 by Wolfgang Mauerer <wm@linux-kernel.net>
# Copyright 2012, 2013, Siemens AG, Wolfgang Mauerer <wolfgang.mauerer@siemens.com>
# All Rights Reserved.
#
# The code in this file originates from:
# https://github.com/siemens/codeface/blob/master/codeface/cluster/PersonInfo.py

from __future__ import absolute_import


class PersonInfo:
    """ Information about a commiter, and his relation to other commiters"""

    def __init__(self, ID=None, name="", email=""):
        self.ID = ID
        self.name = name
        self.email = email

    def __str__(self):
        return self.name + " <" + self.email + ">"

    def setID(self, ID):
        self.ID = ID
    def getID(self):
        return self.ID

    def setName(self, name):
        self.name = name
    def getName(self):
        if self.name == "":
            return self.email
        return self.name

    def setEmail(self, email):
        self.email = email
    def getEmail(self):
        return self.email


############################ Test cases #########################
if __name__ == "__main__":
    personInfo = PersonInfo("sepp")

# TODO: Implement a couple of test cases
