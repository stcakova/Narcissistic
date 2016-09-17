#Signing and distributing your Firefox add-on

# 1.Signing your add-on
Add-ons are signed by [submitting them to AMO](https://addons.mozilla.org/en-US/developers/addon/submit/1) or using the API and passing either an automated or manual code review. 
Note that you are not required to list or distribute your add-on through AMO. If you are distributing the add-on on your own, 
you can choose the Unlisted option and AMO will only serve as the way to get your package signed.

# 2.Signing API
If your add-on is an SDK add-on then use the [jpm](https://developer.mozilla.org/en-US/Add-ons/SDK/Tools/jpm) tool, the [jpm sign](https://developer.mozilla.org/en-US/Add-ons/SDK/Tools/jpm#jpm_sign) command will work with the API to sign your add-on.

# 3.Submitting to AMO
New add-ons are uploaded to AMO through [this](https://accounts.firefox.com/oauth/signin?scope=profile&state=277b095cdc2f3ac5942e54350bb0fbac5a9aef30f9802efa70ee4b22f87ea997%3AL2VuLVVTL2RldmVsb3BlcnMvYWRkb24vc3VibWl0LzE&redirect_url=https%3A%2F%2Faddons.mozilla.org%2Fapi%2Fv3%2Faccounts%2Fauthorize%2F&client_id=a4907de5fa9d78fc) submission form. The first step is to read through and accept the [Developer Agreement](https://developer.mozilla.org/en-US/Add-ons/AMO/Policy/Agreement).
Next, you'll need to decide if you want to distribute and list your add-on through AMO or not. 

# 4.Listed add-ons
After accepting the Developer Agreement, you'll be asked if you want to list your add-on on AMO. Listing it should be the default option.
Choose the platforms your add-on supports and upload your XPI. The file will be scanned by an automatic code validator which will show a number of warnings or errors
depending on what it detects. Errors only show up for listed add-ons if there's something wrong in the package that needs to be fixed before it
can be accepted. Warnings can vary in importance and severity; you should read through all of them carefully and see if there's anything
you can fix in your add-on in order to avoid them showing up. This doesn't mean that you should obfuscate your code to bypass validation
warnings. That practice can lead to your add-on being rejected and potentially blocklisted.
Once you finish your listed add-on submission, it will be placed in a review queue, where it will be given a look. This can take between a couple
of hours to a number of weeks, depending on add-on complexity and other factors. It also takes longer for the first submission, since all of the code 
needs to be reviewed. Updates are reviewed based on a diff, so they are quicker. Once your add-on passes review, the file is signed and published on AMO.
Listed add-ons can be submitted for Preliminary Review or Full Review.  Preliminary Review consists of security and content
checks, focused on the add-on's code. Full Review is a higher standard, and reviews include feature testing and performance checks. 
Add-ons with Full Review have more prominence on the site and can be nominated to be [featured](https://developer.mozilla.org/en-US/Add-ons/AMO/Policy/Featured). Add-ons that are nominated for Full Review and don't meet that standard may receive
Preliminary Review approval instead.

# 5.Ownership
Add-ons can have multiple users with permission to update and manage the listing. Existing authors of an add-on can transfer ownership and add additional developers to an add-on's listing through the Developer Tools provided. No interaction with Mozilla representatives is necessary for a transfer of ownership.
