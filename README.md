# Book Donation App
---

## Fundamental Project 

Contents
- Brief
  - Requirements 
  - My Approach
- Architecture
  - Database Structure
  - CI Pipeline
- Project Tracking
- Risk Assessment
- Testing
- Front-End Design
- Future Improvements

## Resources

Trello Board - add links
Risk Assessment - add links

## Brief
---
### Requirements

The minimum viable product was to create an application that utilises create, read, update, and delete (CRUD) functionalities using technologies, tools and methods covered so far during training. In addition, the secondary requirements for this piece of work must also pass the following criteria: 

- A Trello board
- A relational database, consisting of at least two tables that model a relationship
- Clear documentation of the design phase, app architecture and risk assessment
- A python-based functional application that follows best practices and design principles
- Test suites for the application, which will include automated tests for validation of the application
- A front-end website, created using Flask
- Code integrated into a Version Control System which will be built through a CI server and deployed to a cloud-based virtual machine

### My Approach

To satisfy the requirements above, I have decided to create a simple book donation app which allows the user to: 

- Create a shop (satisfies 'Create') with the following information:
  - *Shop name*
  - *Shop Location*

- Add books to newly created shop with the following information:
  - *Book title*
  - *Date and Time* the book was added

- View the shop that has been created (satisfies 'Read')
- Update the shop details (satisfies 'Update')
- Delete the shop (satisfies 'Delete')

## Architecture 
---
Database Structure
Below is an entity relationship diagram (ERD) which illustrates the architectural structure of the database and the types of relationships which occur between the tables. 

As shown, the app models a many-to-many relationship between Users and Shops using an intermediate table for Books. This allows a user to create shop requests to donate a book to the shop in question. A user can donate books to many shops while a shop can have many users donating books. 





