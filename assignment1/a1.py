"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Tianli Xia (tx58)
Date:   Sep 11th, 2018
"""

import introcs
import a1

def exchange(currency_from, currency_to, amount_from):
    """
    Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in currency
    currency_from to the currency currency_to. The value returned represents the
    amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    if (a1.iscurrency(currency_from) and a1.iscurrency(currency_to)):
        response=a1.passcurrency_response(currency_from, currency_to, amount_from)
        if (has_error(response)):
            print("Has an error: not valid url.")
            return
        else:
            src=(a1.get_src(response) )
            dst=(a1.get_dst(response) )
            src_num= a1.before_space(src)
            src_currency= a1.after_space(src)
            dst_num= a1.before_space(dst)
            dst_currency= a1.after_space(dst)
            return float(dst_num)
    else:
        print("Has an error: not valid currency.")
        return


def before_space(s):
    """
    Returns: Substring of s; up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    return s[:s.find(' ')]


def after_space(s):
    """
    Returns: Substring of s after the first after_space

    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    return s[s.find(' ')+1:]


def first_inside_quotes(s):
    """
    Returns: The first substring of s between two (double) quote characters

    A quote character is one that is inside a string, not one that delimits it. We typically use single quotes (') to delimit a string if want to use a double quote character (") inside of it.

    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C' because it only picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside.
    """
    return s[s.find('"')+1, s.find('"',s.find('"'))]


def get_src(json):
    """
    Returns: The SRC value in the response to a currency query.

    Given a json response to a currency query, this returns the string inside double quotes (") immediately following the keyword "src". For example, if the json is

      '{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'
    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). It returns the empty string if the json is the result of on invalid query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    a= json.find(":")
    b= json.find('"',a)
    return json[b+1: json.find('"',b+1)]


def get_dst(json):
    """
    Returns: The DST value in the response to a currency query.

    Given a json response to a currency query, this returns the string inside double quotes (") immediately following the keyword "dst". For example, if the json is

      '{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'
    Parameter json: a json string to parse
    then this function returns '1.825936 Euros' (not '"1.727138 Euros"'). It returns the empty string if the json is the result of on invalid query.
    Precondition: json is the response to a currency query
    """
    a= json.find('dst')
    b= json.find(':',a)
    c= json.find('"',b)
    return json[c+1: json.find('"',c+1)]


def has_error(json):
    """
    Returns: True if the query has an error; False otherwise.

    Given a json response to a currency query, this returns the opposite of the value following the keyword "success". For example, if the json is

      '{ "src" : "", "dst" : "", "valid" : false, "error" : "Source currency code is invalid." }'
    then the query is not valid, so this function returns True (It does NOT return the message 'Source currency code is invalid').
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    a= json.find('valid')
    b= json.find(':',a)
    c= json.find(' ',b)
    valid= json[c+1: json.find(',',c+1)]
    if (valid=="false"):
        return True
    else:
        return False


def passcurrency_response(currency_from, currency_to, amount_from):
    """
    Returns: a json string that is a response to a currency query.

    A currency query converts amount_from money in currency currency_from to the currency currency_to. The response should be a string of the form

     '{ "src" : "<old-amt>", "dst" : "<new-amt>", "valid" : "", "error" : "" }'
    where the values old-amount and new-amount contain the value and name for the original and new currencies. If the query is invalid, both old-amount and new-amount will be empty, while "success" will be followed by the value false.
    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string

    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    LHS=currency_from.upper()
    RHS=currency_to.upper()
    query= 'http://cs1110.cs.cornell.edu/2018fa/a1server.php?from='+ LHS + '&to=' + RHS + '&amt=' + str(amount_from)
    return introcs.urlread(query)


def iscurrency(currency):
    """
    Returns: True if currency is a valid (3 letter code for a) currency. It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string.
    """
    if (len(currency)==3):
        return True
    else:
        return False
