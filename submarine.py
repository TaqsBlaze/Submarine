import requests
import json
import sys
import os

class ImportModule:

    def __init__(self,module):
        self.module = module
        self.module_dir = 'modules'

    def module_import(self):

        try:
            
            from self.module_dir import self.module

        except ImportError:

            print(f"[+] Failed to import module: {self.module}")
            exit()



class Submarine:

    def __init__(self, target):
        self.target = target
        self.sub_domain_db = None


    def clean_string(self):

        # Remove protocol
        if self.target.startswith("https://") or self.target.startswith("http://"):
            disect = self.target.split("//")
            no_protocol = disect[1]
            self.target = no_protocol

        return self.target


    def load_sub_db(self):
        try:
            with open("sublist/sublist.txt","r") as sublistdb:
                subdomains = sublistdb.readlines().strip()
                self.sub_domain_db = subdomains
        except Exception as error:
            print("[+] Failed to load subdomain database")


    def sector_search(self):
        pass
