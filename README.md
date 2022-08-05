<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.This is the first step towards building my first full web application: the AirBnB clone. This first step is very important because it will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… 

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/Okemwag/AirBnB_clone/blob/main/AUTHORS) | Project authors |



| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/Okemwag/AirBnB_clone/tree/main/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/engine/__init__.py) [/models/base_model.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/Okemwag/AirBnB_clone/blob/main/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/Okemwag/AirBnB_clone/blob/main/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/Okemwag/AirBnB_clone/blob/main/console.py) [/models/engine/file_storage.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/engine/file_storage.py) [/models/user.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/user.py) [/models/place.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/place.py) [/models/city.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/city.py) [/models/amenity.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/amenity.py) [/models/state.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/place.py) [/models/review.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/Okemwag/AirBnB_clone/blob/main/console.py) [/models/engine/file_storage.py](https://github.com/Okemwag/AirBnB_clone/blob/main/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
----
<center> <h1>General Use</h1> </center>

----
1. First clone this repository.
2. Once the repository is cloned locate the "console.py" file and run it as follows
```
/AirBnB_clone$ ./console.py
```
3. When this command is run the following prompt should appear:
```
(hbnb)
```
4. This prompt designates you are in the "HBnB" console, there are a variety of commands available once the console program is run.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)

    - It is possible to call <class_name>.<command>(arguments) as well
----
<center> <h2>Examples</h2> </center>

----
###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <class_id>
```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
```
```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <class_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
```
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <class_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
```
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2022, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
