# ExpressGST || GSTR-1 Prepare and Filing Process (DIY)

**Section:** Express GST

**Category:** Express-GST

**Source:** https://support.kdksoftware.com/portal/en/kb/articles/expressgst-gstr1-prepare-and-filing-process-diy

**Tags:** gstr-1, gstr-1 filing, launchpad, gst, express gst, books vs e-way bill, gst portal, gstr1 preparation, gstr1 filing, gstr-1 prepare and filing process, e-way bill, diy, b2c data import, download ims data, json import, launchpad options, gstr1 prepare process, expressgst, gstr1, flipkart, books vs gst portal, gstr-1 preparation, reconciliation, e-invoice, amazon, ewb, gstr 1, books vs e-invoice, import books, gstr1 prepare and filing process

---

GSTR-1 Preparation and Filing Process

This guide explains the complete process of preparing, validating, and filing GSTR-1 using the revamped workflow. The updated module is designed to improve accuracy, simplify data handling, and ensure seamless integration with the GST portal.

Prerequisites

Before proceeding, ensure that:

The correct Return Period is selected 

Books data is accurate and complete 

Required data sources (E-Invoice / EWB / Portal data) are available, if applicable 

Navigation Path

Dashboard → GSTR-1 → Switch to New → Select Return Period → Prepare/Due

Workflow Summary

The GSTR-1 process is divided into the following stages:

Prepare Books – Data entry and import 

Reconciliation – Data comparison and validation 

Review – Final verification and error correction 

File – Upload and submit return 

Step 1: Prepare Books (Data Entry & Import)

1.1 Manual Data Entry

Navigate to the required GSTR-1 table 

Click on the “+” (Add) button

      
Enter the necessary details in the data entry screen 

1.2 Multiple Line Item Entry

Use the “+” button on the right panel to add multiple line items within a document

      
Use Action/Remarks to: 

Verify E-Way Bill (EWB) status 

Check E-Invoice status 

Review GSTN upload status 

Move records to B2CS (Summary) 

1.3 Import Books Data

Use the Import Books Data option from Launchpad:

      
Supported Import Types

JSON Import – Import GST return JSON files 

GSTIN Templates – 

KDK Template 

Government format 

Supported software: Tally, Busy, Marg 

Amazon Template – Import MTR reports 

Flipkart Template – Import sales data

      
1.4 B2C Data Import Configuration

Append to existing B2CS data → The B2CS records from the import file will be appended to the existing dataset. Previously available records will remain unchanged.
Overwrite existing B2CS data → The existing B2CS data will be completely replaced with the records from the import file.
Not applicable → The system will exclude B2CS data from the import process under this option.
      
1.5 Launchpad Options

The Launchpad provides quick access to:

E-Invoice Data 

E-Way Bill (EWB) Data 

GST Portal Data 

Action Tracker (records moved to Action Center) 

Download IMS Data 

Download Error/Review Reports 

Log File (Edit/Delete History) 

Export Options: Excel, PDF, JSON

      
1.6 Filters and View Customization

Apply filters based on: 

Error status 

Upload readiness

      
Customize table columns using the Customize View option

      
Step 2: Reconciliation
Purpose: To compare Books data with external data sources and identify discrepancies.

Available Comparisons

Books vs E-Way Bill (EWB) 

Books vs E-Invoice 

Books vs GST Portal Data

      

Key Features

Tolerance Setting: Define acceptable differences in taxable value and tax 

Bulk Actions: Accept data from Books, EWB, E-Invoice, or Portal 

Filters: Analyze mismatched or specific data

      

Step 3: Review

3.1 Reconciliation Report

View: 

Transaction-level data 

Summary-level data 

Overall totals

      
3.2 Status Classification

Upload Ready: Ready for upload 

Warning: Can be uploaded with caution 

Error: Must be corrected before upload 

Portal Data: Already available on GST portal 

3.3 Section-wise Summary

Displays a consolidated summary of all entries for validation

      
3.4 Month Comparison

Compare: 

Current period data 

Previous period data

      
3.5 Summary View

Final consolidated view before filing 

      
Step 4: Filing

4.1 Upload Return

Upload prepared data directly to the GST portal

      
4.2 Post Upload

System displays a summary of uploaded data for verification
4.3 Filing Options

EVC (Electronic Verification Code) 

DSC (Digital Signature Certificate) 

Important Notes

Data marked as Error must be corrected before upload 

Deleted records can be restored only before final submission 

Ensure correct return period selection before import or upload 

Validate all data in the Review stage before proceeding to filing 

Conclusion

The revamped GSTR-1 workflow simplifies return preparation through structured stages, enhanced validation, and seamless GST portal integration. Following the above steps ensures accurate filing, reduced errors, and improved compliance.