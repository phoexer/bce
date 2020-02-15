# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:58:42 2018

@author: michael
"""

from cryptography.fernet import Fernet

key = "TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM="

# Oh no! The code is going over the edge! What are you going to do?
message = b"gAAAAABb6-OvdToVBFcNpOUSnOKrTJcjA40W06Eipcz_jl6GBDBAtklQ5vUXKk2Jn-yD433ifgoq_\
m05GRkukJp_1GgxirQsY7macr8URJtw9zUTcEZgE1kUA723FUbxqPRhCp00l2XtWaItVnhK_pALCF5WCuyWZEFkKIcogNeQ1a9UoQsIhiE="


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
