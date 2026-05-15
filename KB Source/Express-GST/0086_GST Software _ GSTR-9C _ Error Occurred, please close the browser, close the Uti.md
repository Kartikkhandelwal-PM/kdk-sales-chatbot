# GST Software > GSTR-9C > Error Occurred, please close the browser, close the Utility and try again.

**Section:** Technical Help

**Category:** Express-GST

**Source:** https://support.kdksoftware.com/portal/en/kb/articles/gst-software-gstr-9c-error-occurred-please-close-the-browser-close-the-utility-and-try-again

**Tags:** please close the browser, gst software, close the utility, expressgst, sign issue, gstr-9c, error occurred

---

Solution: 
  
 
 
 
  
  
 
 
 
 
   All of us know that we need to first download GSTR 9C utility from GST portal’s Download section and Import our JSON file in this through " 
  Open GSTR-9C JSON File Downloaded from GST Portal" option, still after this our job is not over. 
  
 
 
 
  
  
 
 
 
  
   
  
 
 
 
  
  
 
 
 
  
  
 
 
 
 
   Real trouble will start when we try to create Json file and thereafter from "To generate a JSON(.json) file to upload GSTR-9C details added in offline tool on GST Portal" option. 
  
 
 
 
  
  
 
 
 
  
   
  
 
 
 
  
  
 
 
 
 
   Following are the important steps before generating Json file and for filing GSTR 9C. 
  
 
 
 
  
  
 
 
 
  
   
   
     Make sure that all the 15 sheets are validated individually on the GSTR 9C Excel Utility. 
    
 
   
 
 
 
  
  
 
 
 
  
   
    
    
      Make sure that “wsweb” file is in the same folder in PC in which GSTR 9C utility is saved. 
     
 
    
 
  
 
   
   
 
  
 
 
 
  
  
 
 
 
 
   If you get any kind of error then you have to compulsorily follow these steps: 
  
 
 
 
  
   
   
 
  
 
   
    
     
     
       Step 1 : 
      
 
     
 
   
 
   
     Please close all the application on your system. 
    
 
   
 
  
 
 
 
  
   
    
    
      Step 2 :  
    
 
  
 
   
   Open your Internet Explorer 
  
 
 
 
  
   
    
     
     
       Step 3 : 
     
 
   
 
   
     Go to Tool–>Internet Option–>Security–>Custom level, 
    
 
   
 
 
 
  
   
    
     
     
       Step 4 : 
     
 
   
 
   
     You will find two options – 
    
 
   
 
 
 
  
  
 
 
 
 
               i) “Automatic prompting for ActiveX control”. Please click on Enable 
 
 
 
               ii) “Download unsigned ActiveX Control”. Click on Prompt then click OK 
  
 
 
 
  
  
 
 
 
  
   
    
    
      Step 5 : 
    
 
  
 
  
    Now download the Notepad++ from google and follow the following process. 
   
 
  
 
 
 
  
  
 
 
 
 
               i) Install the Notepad++, 
 
 
 
               ii) Go to the utility folder, right click on “wsweb.html”—> click on “Edit with Notepad++” 
 
 
 
               iii) Click after “<html>” tag, give a space after “<html>” tag and then press the backspace. 
  
 
 
 
  
  
 
 
 
  
   
    
    
      Step 6 : 
    
 
  
 
  
    Save the file using “Ctrl+S” key, close the file and stop the Emsigner Service, if started. 
   
 
  
 
 
 
  
  
 
 
 
  
   
    
    
      Step 7 : 
    
 
  
 
  
    Now start Emsigner again 
   
 
  
 
 
 
  
  
 
 
 
  
   
    
    
      Step 8 : 
    
 
  
 
  
    Open the utility and try to generate the JSON file again 
   
 
  
 
 
 
  
  
 
 
 
 
   Internet explorer pop-up will come, inside that you’ll get one more pop-up asking for “Allow Blocked content”, click on it then click on “Initiate signing”, then “Open Emsigner”. 
  
 
 
 
  
  
 
 
 
  
   
    
    
      Even after all these things it doesn’t works then delete emsigner from your PC and download the latest Emsigner and follow all the above steps again! 
    
 
  
 
   
   
 
  
 
 
 
 
   This will helps.