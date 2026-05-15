# ExpressTDS || Valid Count of Challan/Transfer voucher Records Related Error

**Section:** Express TDS

**Category:** Express-TDS

**Source:** https://support.kdksoftware.com/portal/en/kb/articles/valid-count-of-challan-transfer-voucher-records-related-error

**Tags:** challan, fvu, valid count of challan, transfer voucher records, valid count of challan transfer voucher records must be provided, records, voucher, transfer voucher, count, fvu generation error, valid, transfer, valid count of challan transfer voucher records, fvu utility error, fvu utility

---

Valid Count of Challan/Transfer Voucher Records Related Error

      

Root Cause of the Error → This issue arises when challans are not mapped with the deductee transaction entries.

Resolving the Error → To address the "Valid Count of Challan/Transfer Voucher Records" error and map challans with deductee transactions in the File Validation Utility (FVU), follow the steps below:

Steps for Bulk Mapping

Step 1: Navigate to the Mapping Section

Open the FVU tool and go to the Mapping section.

Step 2: Select All Records

Select all the relevant records that need to be mapped.

Step 3: Drag and Drop

Drag and drop the selected records onto the corresponding challan records.

This will automatically map the challans with the deductee transactions.

      

Steps for Manual Mapping

Step 1: Open Deductee Transactions

Navigate to the section listing deductee transactions.

Step 2: Manually Map Each Deductee

For each deductee transaction, manually select and map the relevant challan.

Ensure accuracy when linking deductees to their respective challan records.

      

For further instructions, refer to the Challan Mapping Guide.

Key Points to Remember

Accurate Mapping: Ensure every challan is correctly linked to the relevant deductee records to prevent errors.

Error Prevention: Unmapped records will result in FVU errors related to the "Valid Count of Challan/Transfer Voucher Records."

Bulk Operations: Utilize the drag-and-drop functionality for bulk mapping to streamline the process.

By following these steps, you can efficiently resolve the error and successfully generate the FVU file.