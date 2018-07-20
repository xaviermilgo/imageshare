# Image Share
> Checkout my cool gallery

#### This is my personal gallery website where you can see photos that i have uploaded.
![Live preview](http://i.imgur.com/bchrE9h.png)

## As users you can :
* View different photos that interest me.
* Click on a single photo to expand it and view the details of the photo.
* View different categories of photos.
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

## Development setup

To access the Code behind this site, you will need to:

1. Clone this repo:
  ```bash
  git clone https://github.com/reivhax/imageshare
  ```
2. Move to the folder and install requirements
  ```bash
  cd imageshare
  pip install -r requirements.txt
  ```
3. Create database on psql shell
  ```SQL
  psql
  CREATE DATABASE imageshare;
  ```
4. Run the application
  ```bash
  python manage.py server
  ```

  ## Licensing
  ###### This Project is under the MIT License 2018
  ###### See more about this in the [License.md](https://github.com/reivhax/imageshare/blob/master/LICENSE.md) File
