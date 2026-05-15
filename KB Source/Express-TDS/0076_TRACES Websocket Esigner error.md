# TRACES Websocket Esigner error

**Section:** Technical Help

**Category:** Express-TDS

**Source:** https://support.kdksoftware.com/portal/en/kb/articles/traces-websocket-esigner-error

**Tags:** validate dsc, tds, traces websocket esigner, em-signer, esigner, zen tds, websocket, em-signer utility, expresstds, websigner setup, dsc activities

---

Error in establishing connection with TRACES Websocket Esigner. Please ensure that WebSigner Setup is installed and services is running on your machine and there are no proxies enabled on the browser while doing DSC activities.

            

Root Cause of the error →

The ESigner Setup may not be installed properly or the service may not be running on your system.

There might be proxies enabled on your browser during DSC activities, which can interrupt the connection.

The FVU file (File Validation Utility), em-Signer Utility or the PDF converter utilities are basically Java-based utilities provided by the Traces (TDS) department. The utility of the department would respond only if there is required JAVA installed on the system.

The minimum required version of JAVA should be JAVA 8 or above (32-Bit Only). 

(Check the version from Control Panel → Program and Feature → to get help in knowing the installed JAVA on the system)

            

If there are multiple JAVA's installed on the system, then the command line "Java -Version" will help to know the java running on the system.

      

Steps to Resolve:

Step 1: Verify the Java Version

Ensure you have Java 8 or above (32-Bit Only) installed on your system as required by the TRACES department.

Step 2: Close the Browser and TRACES em-Signer

Before proceeding with any changes, close the browser and the em-Signer application.

Step 3: Download and Install Latest em-Signer

Log in to the TRACES website.

Go to the Downloads section and download the latest version of em-Signer.

Install the downloaded em-Signer.

Step 4: Add Sites to Java Security Exception List

To ensure the Java application can connect to the necessary sites, add the following URLs to the Java security exception list:
https://downloads.tdscpc.gov.in/applet/docwebsigner4.6.jar

https://tdscpc.gov.in/app/ded/kyc3formdsc.xhtml

https://www.tdscpc.gov.in/

To add these sites:

Open Control Panel > Java (32-Bit).

                  
In the Java Control Panel, go to the Security tab and click on Edit Site List.

                  
Click the Add button and add the above URLs one by one.

                  

                  
Click OK and then OK again.

Step 5: Run em-Signer as Administrator

Run the em-Signer application as Administrator and proceed with the DSC activities again.

By following these steps, you should be able to resolve the connection error and continue with your DSC activities.