# ExpressITR || Income Credited to P&L A/c Under Business Head: can not be greater than Income shown under PART-A PL

**Section:** e-filing

**Category:** Express-ITR

**Source:** https://support.kdksoftware.com/portal/en/kb/articles/income-credited-to-pl-ac-under-business-head

**Tags:** efiling, income, income credited, can not be greater than income shown under part-a pl, income credited to profit and loss account under business head, e-filing error, json generation error, p and l, part-a, business head, efiling error, json generation issue, profit and loss account, e-filing, profit and loss, json generation

---

Income Credited to P&L A/c Under Business Head: can not be greater than Income shown under PART-A PL

If you face this error during JSON generation, follow these steps to resolve it:

Steps to Fix the Issue

Step 1: Locate the Error

Click on the error message link.

This will redirect you to the Consolidated Sch. BP.

      

Step 2: Open Adjusted P&L Annexure

In the Adjusted P&L Annexure, verify the details of income credited to the P&L under the Business/Profession head.

      

Scenario 1: Incorrect Reduction of Income

Check if you have mistakenly reduced income from Business/Profession in the adjusted P&L.

If yes, remove the incorrect reduction and generate the JSON file again.

Scenario 2: Income Reduction from Business Head

If you intend to reduce income from the Business/Profession head, ensure the following:

Cross-Check Point No. 14 – Other Income: Confirm that the income you reduced is included in Point No. 14 – Other Income of the Profit & Loss Account.

Adjustments: If this income is not reflected in Point No. 14 – Other Income, add it under the appropriate column in the Financial Statement's Profit and Loss Account.

Step 3: Mandatory Adjustments

After adjustments, ensure that:

The income reduced under the Business/Profession head is equal to or less than the income reported under Point No. 14 – Other Income of the P&L.

The income reduced is correctly categorized under the appropriate income head.

Instructions for Feeding P&L (Point No. 14 - Other Income)

Go to Financial Statement: Open the Profit and Loss Account.
Locate Point No. 14: Find Other Income in the P&L section.
Enter Income Details: Add the income amount under the applicable column.
Save Changes: Click Save or Done to confirm.

      
      

Ensure this matches your adjustments in the Adjusted P&L.

Step 4: Generate JSON Again

After completing these adjustments, generate the JSON file again.

The error should now be resolved.

Additional Notes :

The total income shown under a separate income head must be equal to or greater than the income reduced from Business/Profession.

Accurate categorization and reconciliation are mandatory to avoid discrepancies.

Hope this resolves your issue!