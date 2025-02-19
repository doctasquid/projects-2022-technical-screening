"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json
import re
import string

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()


# sorry didnt have time to finish because of supps :(

def req_check(courses_list, req_string):

    #print(req_string)

    if (req_string == "") :
        return True

    if(req_string[0] == '(' and req_string[-1] == ")"):
        return req_check(courses_list, req_string[1:-2])

    course = re.compile(r"^(((COMP)|(DPST)|(ELEC)|(MTRN)|(MATH))\d{4})$")

    if (course.search(req_string) != None):
        return (req_string in courses_list)

    coursecode = re.compile(r"^\d{4}$")
    if (course.search(req_string) != None):
        return (("COMP" + req_string) in courses_list)

    atom = re.compile(r"(((COMP)|(DPST)|(MATH)|(ELEC)|(MTRN))\d{4})|\(.*\)")
    oratom = re.compile(r"((((COMP)|(DPST)|(MATH)|(ELEC)|(MTRN))\d{4})|\(.*\).*(or|OR))")
    andatom = re.compile(r"((((COMP)|(DPST)|(MATH)|(ELEC)|(MTRN))\d{4})|\(.*\).*(and|AND))")

    atomhold = atom.search(req_string)
    orhold = oratom.search(req_string)
    andhold = andatom.search(req_string)

    #if(orhold != None and (andhold == None or (len(orhold.group()) > len(andhold.group())))):
    if(orhold != None):
        return req_check(courses_list,orhold.group().strip()) or req_check(courses_list,req_string[len(orhold.group()) + 1:].strip()) 

    #if(andhold != None and (orhold == None or (len(andhold.group()) > len(orhold.group())))):
    if(andhold != None):
        return req_check(courses_list,andhold.group().strip()) and req_check(courses_list,req_string[len(orhold.group()) + 1:].strip()) 

    return False


def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
   

    return req_check(courses_list,(re.sub(r"Pre.*:","",CONDITIONS[target_course])).strip())
    # TODO: COMPLETE THIS FUNCTION!!!

#print(re.sub(r"Pre.*:","",CONDITIONS["COMP1511"]).strip())

#if (is_unlocked(["COMP1917", "DPST1092"],"COMP3151") == True):
#    print("success")
#else:
#    print("fail")





    
