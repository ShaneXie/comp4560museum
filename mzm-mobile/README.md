# NativeScript Museum Project
## Development environment setup
This project is using TypeScript, Angular2 and NativeScript. This section will introduce how to setup the development environment for this project.
### Node.js
Node.js is an open-source, cross-platform JavaScript runtime environment. We need Node.js as run time environment and package management software for our project.

Node.js could be download from their official website:[NodeJs Download](https://nodejs.org/en/)

### TypeScript
TypeScript as a supersite of JavaScript. We will need TS for Angular2 and NativeScript.

To install TypeScript, we shall use npm package management tool by cmd in terminal:

    npm install -g typescript

### Angular2
Angular2 is a web framework that provides the ability to convert typescript code with into JavaScript. We will use npm to install the necessary packages.

We need to install packages for following project:

    mzm-front
    mzm-mobile

For each of the folder above, change the path to its root folder. For example, for mzm-front project:

    cd ~/comp4560museum/mzm-front/

then run the cmd:

    npm install

### NativeScript
NativeScript is an open-source framework for building native mobile apps that convert Angular/TypeScript or JavaScript code to ObjC or Java.

#### NativeScript installation
By npm:

    npm install -g nativescript

verify installation by enter tns terminal:

    tns

and you would see the following

    ┌─────────┬─────────────────────────────────────────────────────────────────────┐
    │ Usage   │ Synopsis                                                            │
    │ General │ $ tns <Command> [Command Parameters] [--command <Options>]          │
    │ Alias   │ $ nativescript <Command> [Command Parameters] [--command <Options>] │
    └─────────┴─────────────────────────────────────────────────────────────────────┘

Check NativeScript environment

    tns doctor

Note:
1.  To run android emulators, tns doctor will ask to install Android SDK.
2.  To run iOS emulator, you need to install xCode on the environment for the official emulator. Which means you need a OSX system.

#### Platform setting
we need to setup the mobile platform for project by following cmd:

iOS:

    tns platform add ios

Android:

    tns platform add android

## How to run
### mzm-mobile

Change the path to mzm-mobile folder to start the operation.

To run on emulator:

    tns run ios --emulator
    tns run android --emulator

To run on an android device(you need to open the usb debug mode from your device)

    tns run android

### WorkFlow
We may need to see the changes we make during the coding.

iOS emulator:

    tns livesync ios --emulator --watch

Android emulator:

    tns livesync android --emulator --watch

Android Device:

    tns livesync android --watch

## Publish
### Android
To publish an android apk, we need a keystore file.
For details check the [link](https://developer.android.com/studio/publish/app-signing.html#signing-manually)

then use the cmd as follow:

    tns build android --release --key-store-path <path-to-your-keystore> --key-store-password <your-key-store-password> --key-store-alias <your-alias-name> --key-store-alias-password <your-alias-password>

### iOS
Fisrt we need a apple developer account and xCode to sign the program.

More details: [iOS publish](http://docs.nativescript.org/angular/publishing/publishing-ios-apps#creating-ios-nativescript-app)
