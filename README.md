# Agnostic
Agnostic is a Class Scaffolding Framework I am currently working on as a side project. Essentially the idea is if you provide a json file in a particular structure with information about classes, structs, enums, and interfaces, then Agnostic can use that information to generate stub (or scaffolded) code in whatever language it supports, thus allowing you to generate a basic structure for different languages quickly.

Because it takes in a Json file, you can use whatever tools you want to create the structure, including writing a parser for your existing code, or making GUI front-ends to quickly put together class models and have it convert that to JSON. In fact, one of the long-term goals is to have a cross-platform mobile app that allows you to input this basic information about your app from anywhere and it will create the structure file for you.

This project is NOT about trying to take in the entire structure of a program in a JSON structure and allowing a one stop shop for converting entire projects from language to language. Someone may want to eventually fork this project for attempting that, but I want to keep this easy to understand and create/modify both the structures and the templates and I do not want to overcomplicate it in order to achieve full compatibility. The intention is for the overall basic structure of the program.

This means that eventually this might be useful for people to study to get a better understanding of the similarities and differences between the basic syntax of other languages and can therefore pick up new languages faster, but that's more of a likely side-effect and not the main goal. 

### Road Map ###

Working on features for Major Iteration 2

####Major Iteration 1####

 1. This is where I was at when I made the first commits to Git.
 2. Basically a proof of concept, took in a json structure and a json template and processed the structure through the template in order to convert it to basic scaffolding code that resembles actual programming code, and doesn't require too much extra work in order to compile. Only had basic templates for C#, Objective-C, and Python

####Major Iteration 2####

 1. Write templates for top 10 languages on Tiobe (perhaps more if motivated to)
 2. Add support for header files to allow for C++ and Obj-C templates
 3. Output to files, with separate files for each class or structure
 4. Get type mapping working, so you can show the proper type text for primitives and objects, and allow for variable initialization
 5. Add constructor key to templates, and build constructor function
 6. Add support for passing in arguments to pass in the language file and the location of the structure json file to use

####Long-Term####

 1. Make a cross-platform mobile app (using Xamarin?) to allow users to quickly generate the json structure files using a GUI interface while they're on the go.
 