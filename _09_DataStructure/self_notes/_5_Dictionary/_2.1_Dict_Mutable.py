"""
Dictionary is a mutable data. That means we can change only the values.
we cant change the key,because key is immutable.

ex.
data = { "s_rno" : 01,
         "s_fname" : 'Rinky',
         "s_lname" : 'Kumari",
         "s_class" : "IV",
         "s_add"   : [ 201, "Gumla", "Ranchi", 835294]
        }

  print("----------------- UPDATE --------------")
  data = { "s_rno" : 01,
         "s_fname" : 'Rinky',
         "s_lname" : 'Kumari",
         "s_class" : "IV",
         "s_add"   : [ 265, "ACE LAYOUT", "Marathahlli, 560025]
        }


 print("----------------- UPDATE --------------")
  data = { "s_rno" : 01,
         "s_fname" : 'Rinky',
         "s_lname" : 'Kumari",
         "s_std" : "IV",        # ERROR
         "s_add"   : [ 265, "ACE LAYOUT", "Marathahlli, 560025]
        }


"""