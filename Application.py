#!/usr/bin/env python

import os,xlrd
from Seller import Account,User

class Application:
    
    def __init__(self):
      self.current_session=None
      
    
    
    
    def Create_User(self,name,directory=None):
        # Creates a User
        
        user_name=name
        path_name=os.path.join('C:\Users\Tristan Angeles\Desktop',user_name)
        #print(path_name)
        if not os.path.exists(path_name):
            os.mkdir(path_name)
            
            
            #create accounts folder
            accounts_path=os.path.join(path_name,'accounts')
            if not os.path.exists(accounts_path):
                os.mkdir(accounts_path)
            
        else:
            print("User already exists")
            
            
        self.Start_Session(user_name,path_name)
        
            
        
    
    
    def Create_Account(self,name):
        print(self.current_session)
        if not self.current_session:
            print("Create Session first")
            return
        
       
        path_name=os.path.join(self.current_session.accounts_directory,name)
        print(path_name)
        if not os.path.exists(path_name):
            os.mkdir(path_name)
          
            
        else:
            print("Account already exists.Choose another account name")
       
     
    
    
    def Load_User(self,user_id):
        #Opens user for a Session
        pass
    
    
    def Load_Account(self,account_id):
        #Loads Account
        pass
    
    
    def Start_Session(self,user_id,directory=None):
        self.current_session=Session(user_id,directory)
    
    
    

class Session:
    
    def __init__(self,user_id,directory=None):
        self.user=user_id
        self.directory=directory
        self.accounts_directory=os.path.join(self.directory,'accounts')
    
    
    
