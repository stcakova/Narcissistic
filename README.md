#Publish your app to the Chrome Web Store

# 1. Create your app’s zip file
  To upload your app, you need to create a ZIP file that contains at least one file: your app's     manifest.json. Set the initial version number in the manifest to a low value, such as 1.0.0 or lower if you intend to test the plugin before the actual release

# 2. Create a developer account
 If you want to publish a hosted app, you'll need to prove that your developer account owns the URLs that comprise the app. Visit the Google Webmaster Tools Help Center for information on [proving site ownership](https://support.google.com/webmasters/answer/34592?hl=en).

# 3. Upload your app
Go to the Chrome [Developer Dashboard](https://chrome.google.com/webstore/developer/dashboard).
Sign into the developer account.
Click the Add new item button.

If you've never uploaded an item before, you need to accept the developer agreement before going to the next step.

Click Choose file > your zip file > Upload. If your app's manifest and ZIP file are valid, you can edit your app on the next page.

# 4. Pick a payments system

If you aren't going to use Chrome Web Store Payments, you can delay or (for free apps) omit this step.

# 5. Get the app ID

The app ID appears in the URL of any dashboard or store page for your app. You’ll need the app ID if you want to use the Licensing API.

For example, the URL "https://chrome.google.com/extensions/detail/aaaaaaaaaabbbbbbbbbbcccccccccc?hl=en" has the app ID “aaaaaaaaaabbbbbbbbbbcccccccccc.”


#6. Get the OAuth token
Go to the Chrome [Developer Dashboard](https://chrome.google.com/webstore/developer/dashboard). Each hosted app that you've uploaded and that uses Chrome Web Store Payments has an OAuth setup link that lets you get OAuth information for that app.

Note: The OAuth setup link is only shown for hosted apps. If you don't see the OAuth setup link for your hosted app, click the Edit link and use the Change pricing button to specify that your app uses Chrome Web Store Payments.
Click the OAuth setup link. You get a page with OAuth information for the Licensing API. At the bottom of that page is the information you need to make Licensing API requests with your app, including the app ID but not the access token and token secret.
Click the Generate new token button at the bottom of the page to generate the OAuth access token and token secret for your app.
Record the token and token secret in a safe place. The dashboard will not show them to you again.

# 7. Finish the app
Now you can add any code that refers to the app ID or OAuth access token to complete your app. You can update your app as many times as you want, just remember to increase the version number each time.

# 8. Pay the developer signup fee
Before you publish your first app, you must pay a one-time $5 developer signup fee. A reminder in the dashboard will appear until you pay the fee.For more information, including troubleshooting tips, see the [Registration article](https://developer.chrome.com/webstore?visit_id=1-636097005655114165-1457965878&rd=2).

# 9. Publish your app





