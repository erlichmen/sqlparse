<<<<<<< HEAD
"""
CoolaData tests for SQLparse:
"""

import unittest
import sqlparse

@unittest.skip("Who cares about SqlParse?")
class test_sqlparse(unittest.TestCase):
    """ 
    Tests for Sqlparse:
    
    Tests will have there own SQL input statement, which will be parsed using SQLparse, and then some sort of assertion will take place.
    
    """

    def test_keyword_in_identifierlist(self):
        " Making sure *user* in identifier list was treated as a normal identifier, and not as a Keyword "
        " known keywords : *user*, *type*, *level*"

        stmt = "Select a,b,user,c" 
        parsed = sqlparse.parse(stmt)
        self.assertEqual(parsed[0].tokens[2].tokens[4].value, 'user', "Identifier List keyword was not handled correctly.")

    def test_keyword_in_where(self):
        " making sure that *type* in the Where clause passed OK "
        " --- **type** should be treated like **zype** "
        
        stmt = "Select a Where type=42"
        parsed = sqlparse.parse(stmt)

        self.assertEqual(parsed[0].tokens[-1].tokens[-1].tokens[0], 'type', "Where clause keyword was not handled correctly.")

    def test_minus_in_where(self):
        " A test for handling minus sign correctly."
        "  ---- **a-b** should be treated like **a+b** ----  "
        
        stmt = "Select a Where beauty-16=levels"   
        parsed = sqlparse.parse(stmt)
    
        self.assertEqual(parsed[0].tokens[-1].tokens[2].__class__, sqlparse.sql.Comparison, "Where clause minus sign was not handled correctly.")    
        self.assertEqual(parsed[0].tokens[-1].tokens[2].tokens[0].value, 'beauty-16', "Where clause minus sign was not handled correctly.")     

    def test_func_in_compare(self):
        " A test for the correct handling of a function inside a comparison."
        """ Parser currently takes function out of the comparison. we want it inside, just like a normal identifier.
          ---- **func(money)** should be treated like **money** ---- 
        """

        stmt = "Select a Where func(money)>16"
        parsed = sqlparse.parse(stmt)

        self.assertEqual(parsed[0].tokens[-1].tokens[-1].__class__, sqlparse.sql.Comparison, "Was expacting a comparison.")
        self.assertEqual(parsed[0].tokens[-1].tokens[-1].tokens[0].__class__, sqlparse.sql.function, "The function was not treated correctly." )

    def test_floats_in_compare(self):
        " A test for the handeling of floats inside a comparison. "
        "   ---- **4.2** should be treated like **42** ----  "

        stmt = "Select a Where exp/4.2=cash"
        parsed = sqlparse.parse(stmt)

        self.assertEqual(parsed[0].tokens[-1].tokens[2].__class__, sqlparse.sql.Comparison, "Was expacting a comparison.")
        self.assertEqual(parsed[0].tokens[-1].tokens[-1].tokens[0].value, 'exp/4.2', "The float was not treated correctly." )