---
layout: page
title: Privacy
---

We value personal privacy very highly.
This system has been designed to minimize information disclosure.
Please review the source code to verify we have stuck to this commitement.

# Tapsafe.github.io Website

The sites functionality relies on storing a Web Push subscription from your paired Mobile.
This is stored in LocalStorage and can be inspected with your Browser's built in tools.
No Cookies or other deliberate tracking methods are employed.

This page is built using [Jekyll](https://jekyllrb.com/) and makes significant use of Javascript libraries.
As much as fesable we have verified these libraries are well behaved inline with the spirit of this policy.
(Please raise Issues if you feel we have missed anything.)

This website is served over SSL, curtesy of Github Pages and thier CDN.
View thier [privacy policy](https://github.com/site/privacy).
This does raise the posibility of Github replacing or altering these pages; however this seemed more transparent then asking you to trust a server fully under my control.
You are encouraged to host these pages yourself.

Web Push is provided by your Browser which controls its privacy.
All messages sent are encripted with private keys which never leave your Browser and Mobile.
Browser vendors relay the messages centrally, tracking timing and addressing for the service to work.

# Tapsafe Browser Extension

The extension itself does not collect or transmit tracking information.
By default it uses your Browser's auto-update mechinisium.
Browser vendors do track some usage information from these update checks.

Clicking the extensions button transmits the hostname of the page in the currently active tab to the local javascript loaded from tapsafe.github.io.
The details of the websites are stored in the URL #fragment so they are not sent with HTTP requests.

# Tapsafe Mobile App

The App is developed using many libraries and the funcionality of the mobile OS.
As much as fesable we have verified these libraries are well behaved inline with the spirit of this policy.
(Please raise Issues if you feel we have missed anything.)

The App stores your Browser's Web Push subscription to taspsafe.github.io, and your TOTP secrets on your device.
No advertising or deliberate tracking systems are included.

The App is distributed via most popular appstores, with auto-updates enabled.
Please refer to the privacy policies of the store you used.

You are encouraged to build the application for yourself.
The appstore versions are built in cairfully audited environments and signed with our private keys.
