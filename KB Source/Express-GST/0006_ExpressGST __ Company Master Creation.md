# ExpressGST || Company Master Creation

**Section:** Express GST

**Category:** Express-GST

**Source:** https://support.kdksoftware.com/portal/en/kb/articles/company-master-creation

**Tags:** bulk import, expressgst, add client, excel import, gst, gstin, login details, excel download, add company, client master

---

Company Master Creation Guide

In ExpressGST, a Client represents a business entity or individual registered under the Goods and Services Tax (GST) who utilizes the platform for GST compliance and return filing. Each client is configured with unique credentials mapped to their respective GSTIN (Goods and Services Tax Identification Number).
This document provides a comprehensive guide to creating a Company (Client) Master using various available methods.

Methods for Company Master Creation

The application supports the following methods for adding clients:

GSTIN Credentials (Single Client Creation)

Excel Upload (Bulk Import)

JSON Import (From Local System)

Migration from ClearTax

1. Client Creation Using GSTIN Credentials

This method is recommended for adding a single client using GST portal login credentials.

Steps to Create Client

Step 1: Log in to the application and click on “Add New Company”.

      
Step 2: Enter the required details:
GSTN Username: GST portal username of the client

GSTN Password: Corresponding password

Captcha: Enter the captcha as displayed

      
Step 3: Click on Save to proceed.

Result: The client will be successfully created and listed in the Client Master.

2. Client Creation via Excel Upload (Bulk Import)

This method is suitable for creating multiple clients simultaneously.

Steps for Bulk Import

Step 1: Log in to the application and click on “Add Company Name”.
Step 2: Click on Browse Excel.

      

Step 3: Download the predefined template by clicking on “Click here to download”.

      

Step 4: Open the template and enter client details, including:
GSTIN

Username

Password

      

Step 5: Save the completed Excel file on your system.

Step 6: Click on Select File, choose the prepared file, and click Open.

      

Step 7: Click on Import to initiate the upload.
Step 8: Review the import summary:
Successfully imported records

Rejected records with reasons (e.g., invalid GSTIN, incorrect credentials)

      

Step 9: Click OK to confirm.

Step 10: Click on Get Captcha, enter the captcha, and select “Create Company” to complete the process.

      

Result: All valid records will be added to the Client Master.

3. Client Creation via JSON Import (Local System)

This method allows users to create multiple clients using JSON files.

Available Options

Browse JSON File/Folder: Select a specific JSON file or an entire folder from your local system for import.
Auto Scan: Automatically detects and imports JSON data available from the portal.
      
4. Migration from ClearTax

This option enables seamless migration of client data from ClearTax.

Steps

Enter ClearTax Username and Password

Click on Proceed to initiate migration

      

Result: Client data will be imported into ExpressGST.
Reference Link:  For detailed migration steps, refer to: https://support.kdksoftware.com/portal/en/kb/articles/client-master-migration-from-cleartax-to-expressgst

Important Notes

Ensure that GSTIN credentials are valid to avoid import failures.

Verify Excel template format before uploading to prevent rejection of records.

JSON import should be performed only with valid and properly structured files.

During bulk import, only valid records will be processed; invalid entries will be highlighted in the summary.

ExpressGST provides flexible and efficient methods for creating and managing Client Masters. Users can choose the appropriate method based on their requirements—whether adding a single client, performing bulk imports, or migrating existing data.