# Book Catalog

Third project for Full-Stack Web Devloper Nanodegree course; Book Catalog is a web application that catagorizes books into different genres.

Feature list:
* View all books in catalog
* Add, edit, and delete your own books
* Third party Login using OAuth 2 with Google+ Sign-in
* RESTful JSON and XML endpoints
* CSRF protection with Flask-WTF

## Table of Contents

* [Dependancies](#dependancies)
* [Installation and Run](#installation-and-run)
* [Helpful Commands](#helpful-commands)
* [Notes](#notes)
* [JSON and XML RESTful API Examples](#json-and-xml-restful-api-examples)
* [Creator](#creator)
* [Copyright and license](#copyright-and-license)

## Dependancies

Book Catalog is built using Python, and depends on Virtual Box and Vagrant to run; be sure to have them installed.
* [Python 2.7](https://www.python.org/downloads/)
* [Vagrant](https://www.vagrantup.com)
* [Virtual Box](https://www.virtualbox.org)

## Installation and Run

In order to install and run Book Catalog follow these instructions:
* Get source code by either downloading the zip [here](https://github.com/brianquach/udacity-nano-fullstack-catalog) or using git clone: 
```sh
git clone https://github.com/brianquach/udacity-nano-fullstack-catalog.git
```
* Navigate to the directory where the code was unzipped or cloned to
* Add your client_secrets.json file into `/vagrant/catalog` directory. See [generating client_secrets.json](#generating-client_secretsjson) for more details.

* Launch Vagrant VM and SSH into it
* Navigate to the Book Catalog directory
```sh 
cd /vagrant/catalog
```
* Initialize database and data
```sh
python create_db.py
````
* Run the Book Catalog server
```sh
python runserver.py
```
* Use web browser to navigate to http://localhost:8000/

#### Helpful Commands
* Launch Vagrant `vagrant up`
* Terminate Vagrant `vagrant halt`
* SSH into Vagrant `vagrant ssh`
* Exit out of Vagrant SSH `exit`

#### Generating client_secrets.json
At the time of this writing, to create a Google Developers Console project and client ID, follow these steps:

* Go to the [Google Developers Console](https://console.developers.google.com/).
* Create a new project by selecting **Create a Project** from your projects list:
  - In the **Project name** field, type in a name for your project.
  - Your **Project ID** is created by the console for you.
  - Click the **Create** button and wait for the project to be created.
* Once created, click on the **Enable and manage APIs** link within the **Use Google APIs** [card](https://www.google.com/design/spec/components/cards.html).
* In the sidebar under "API Manager", select **Credentials**, and click the **OAuth consent screen** tab.
  - Choose an **Email Address**, specify a **Product Name**, and click **Save**.
* In the sidebar under "API Manager", select **Credentials**.
* Click **Create a new Client ID** — a dialog box appears.
  - Select **OAuth client ID** 
  - In the **Application type** section of the dialog, select Web application.
  - In the **Authorized JavaScript origins field**, enter `http://localhost:8000`
  - In the **Authorized redirect URI field**, enter `http://localhost:8000/server-connect`
* Click the **Create Client ID** button.
* Select the newly created OAuth 2.0 client ID and click on **Download JSON**
* Rename file to **client_secrets.json**

## Notes
In order to be authenticated and authorized to use site function such as adding a book to the catalog, you must have a google+ account to login with.

You can add or edit the test data by editing the test_data.json file, which will be loaded and used by `create_db.py`; just follow the given format.


## JSON and XML RESTful API Examples

Book Catalog implements a RESTful API returning data in both JSON and XML formats. Calls can be made to view user profile, list of catagories, and list of items within a specified catagory; see examples below.

**To get data in the XML format instead of JSON from the examples below replace `.json` with `.xml`*

#### Examples
`http://localhost:8000/me.json`

**Must be logged in to get profile information*

Yields:
```json
{
  "user": {
    "address": "13rianquach@gmail.com",
    "id": 1,
    "name": "Brian Quach",
    "picture": "https://lh6.googleusercontent.com/-3MBWgjlPOEA/AAAAAAAAAAI/AAAAAAAAANQ/J1Lg994nBZQ/photo.jpg"
  }
}
```

`http://localhost:8000/catagories.json`

Yields:
```json
{
  "catagories": [
    {
      "id": 1,
      "items": [
        {
          "author": "Steve Jenkins",
          "description": "Our world is filled with extraordinary diversity, from\namoebas to zebras, from tiny toadstools to giant oaks. The wonders of the\nnatural world are on display in The Animal Book. This guide to life on our\nplanet is packed full of information about creatures big and small. This tome\nis structured according to scientific classification, with straightforward\nexplanations of more than 1,500 specimens, each stunningly photographed. A\n\"tree of life\" greets readers at the beginning of the book, charting the\ncomplex and interconnected relationships between species. Every plant and\nanimal is presented in proportion, with in-depth spreads giving a sense of\nscale to each organism. Feature spreads that focus on a single specimen let\nchildren get up close and personal with the world's most fascinating animals,\nmaking The Animal Book perfect not only for homework help but to satisfy kids'\ncuriosity about the wealth of living creatures that inhabit our planet.\n",
          "id": 1,
          "name": "The Animal Book",
          "picture": "https://donalynmiller.files.wordpress.com/2013/12/animal-book.jpg"
        }
      ],
      "name": "Animal"
    }
  ]
}
```

`http://localhost:8000/catagory/<catagory_id>/items.json`

**Replace `<catagory_id>` with the Id of the catagory you want to the API to pull from*

`http://localhost:8000/catagory/1/items.json`

Yields:
```json
{
  "catagory": "Animal",
  "catagory_items": [
    {
      "author": "Steve Jenkins",
      "description": "Our world is filled with extraordinary diversity, from\namoebas to zebras, from tiny toadstools to giant oaks. The wonders of the\nnatural world are on display in The Animal Book. This guide to life on our\nplanet is packed full of information about creatures big and small. This tome\nis structured according to scientific classification, with straightforward\nexplanations of more than 1,500 specimens, each stunningly photographed. A\n\"tree of life\" greets readers at the beginning of the book, charting the\ncomplex and interconnected relationships between species. Every plant and\nanimal is presented in proportion, with in-depth spreads giving a sense of\nscale to each organism. Feature spreads that focus on a single specimen let\nchildren get up close and personal with the world's most fascinating animals,\nmaking The Animal Book perfect not only for homework help but to satisfy kids'\ncuriosity about the wealth of living creatures that inhabit our planet.\n",
      "id": 1,
      "name": "The Animal Book",
      "picture": "https://donalynmiller.files.wordpress.com/2013/12/animal-book.jpg"
    }
  ]
}
```

`http://localhost:8000/catagory/1/items.xml`

**Example retrieving data in XML instead of JSON*

Yields:
```xml
<catagory>
  <items>
    <item>
      <picture>
      https://donalynmiller.files.wordpress.com/2013/12/animal-book.jpg
      </picture>
      <description>
      Our world is filled with extraordinary diversity, from amoebas to zebras, from tiny toadstools to giant oaks. The wonders of the natural world are on display in The Animal Book. This guide to life on our planet is packed full of information about creatures big and small. This tome is structured according to scientific classification, with straightforward explanations of more than 1,500 specimens, each stunningly photographed. A "tree of life" greets readers at the beginning of the book, charting the complex and interconnected relationships between species. Every plant and animal is presented in proportion, with in-depth spreads giving a sense of scale to each organism. Feature spreads that focus on a single specimen let children get up close and personal with the world's most fascinating animals, making The Animal Book perfect not only for homework help but to satisfy kids' curiosity about the wealth of living creatures that inhabit our planet.
      </description>
      <author>Steve Jenkins</author>
      <id>1</id>
      <name>The Animal Book</name>
    </item>
    </items>
  <name>Animal</name>
</catagory>
```

## Creator

Brian Quach
* <https://github.com/brianquach>

## Copyright and license

Code copyright 2016 Brian Quach. Code released under [the MIT license](https://github.com/brianquach/udacity-nano-fullstack-catalog/blob/master/LICENSE).