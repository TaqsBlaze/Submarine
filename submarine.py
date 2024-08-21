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
        self.found = []


    def clean_string(self):

        # Remove protocol
        if self.target.startswith("https://") or self.target.startswith("http://"):
            protocol_disect = self.target.split("//")
            no_protocol = disect[1]
            self.target = no_protocol
        # Removing www subdomain
        if self.target.startswith("www."):
            subdomain_disect = self.target.split("www.")[1]
            self.target = subdomain_disect

        return self.target


    def load_sub_db(self):
        try:
            with open("sublist/sublist.txt","r") as sublistdb:
                subdomains = sublistdb.readlines()
                self.sub_domain_db = subdomains
        except Exception as error:
            print("[+] Failed to load subdomain database")
            exit()


    def sector_search(self):
        
        for subdomain in self.sub_domain_db:

            target = f"{self.sub_domain_db}{self.target}"

            response = requests.get(target)

            if response.status_code == 200:
                self.found.append(target)
            else:
                continue

