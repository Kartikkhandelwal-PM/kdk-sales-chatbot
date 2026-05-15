# ExpressITR || Client Master Migration from ClearTax to ExpressITR

**Section:** Data Feeding

**Category:** Express-ITR

**Source:** https://support.kdksoftware.com/portal/en/kb/articles/expressitr-client-master-migration-from-cleartax-to-expressitr

**Tags:** express itr, spectrum-cloud, cleartax, client master migration, expressitr, 2fa, 2fa authentication error, create new client, clear tax, 2fa authentication errors, migrate from cleartax, client master migrate, spectrum cloud itr, client master migration from cleartax to expressitr, two-factor auth, spectrumcloud, two-factor authentication, cleartax to expressitr, client master

---

Client Master Migration from ClearTax to ExpressITR
This article explains the complete process to migrate Client Master data from ClearTax software to the ExpressITR application.

The migration utility helps users quickly transfer existing client records from ClearTax into ExpressITR, eliminating the need for manual data entry and ensuring a smooth transition to the new system.

Initiating Client Master Migration

Step 1: Open the Client Master Screen

Launch the ExpressITR application.

Navigate to the Client Master section and click on the Add (+) icon to create or import client records.

This will open the Client Master creation screen where different client addition options are available.

Step 2: Select the ClearTax Migration Option

Click on Migrate from ClearTax.

Enter your ClearTax Login Credentials (Username and Password).

Click the Proceed button.

The system will begin fetching the client details available in your ClearTax account.

Note: During the migration process, only the Client Master details (PAN Number) will be imported from the ClearTax application. The password must be entered manually by the user, as password information is not available from the ClearTax application.

Verifying Migrated Client Data

Once the migration process is completed:

Return to the Client Master screen in ExpressITR.

The migrated client records will now appear in the client list.

Users are required to enter the password manually, after which they can review and manage the migrated client records within the ExpressITR application.
This confirms that the client data has been successfully transferred from ClearTax.

2FA Authentication Error
If an error related to Two-Factor Authentication (2FA) occurs during the migration process, follow the steps below.

      

Step 1: Log in to the ClearTax Portal

Visit the ClearTax ITR website (https://taxcloudindia.com/entity#/) and log in using your credentials.

After successfully logging in, open the following link in the same browser session to access the account security settings: https://accounts.cleartax.in/user-settings/
Step 2: Access Security Settings

Navigate to the Security tab.

Locate the Two-factor authentication (2FA) Status option.

Step 3: Disable Two-Factor Authentication

Turn OFF the 2FA toggle.

Enter your ClearTax password when prompted for confirmation.

Click Save to apply the changes.
After disabling 2FA, retry the migration process in the ExpressITR application.

This should allow the system to successfully connect to ClearTax and complete the client data migration.