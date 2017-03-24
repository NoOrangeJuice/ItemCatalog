# itemcatalog
Item catalog project for Udacity. This application allows users create a catalog of restaurants, and food items for their restuarants. Users may login using Google's Oauth and may only edit/delete their own submissions. Application is currently being hosted on an Ubuntu Lightsail instance which can be found here: http://34.195.88.228/
<hr>
<h3>Requirements</h3>
  <ul>
    <li>VirtualBox</li>
    <li>Vagrant</li>
  </ul>
<hr>
<h3>Instructions</h3>
  <ul>
    <li>Install requirements</li>
    <li>Clone repository from https://github.com/NoOrangeJuice/itemcatalog.git or download the zip file</li>
    <li>$ cd ~/itemcatalog/</li>
    <li>$ vagrant up</li>
    <li>Once the vagrant machine has finished installing run: $ vagrant ssh</li>
    <li>Once inside the vagrant machine run: $ cd /vagrant/catalog</li>
    <li>$ python database_setup.py</li>
    <li>$ python populatemenus.py</li>
    <li>$ python project.py</li>
    <li>Go to http://localhost:5000 in your web browser.</li>
    <li>Items and restaurants can only be deleted by the user who made them, you will not be able to delete the starting restaurants or items.</li>
    <li>Login with gmail and play around with the functionality of the site. Once you are done be sure to logout.</li>
<hr>
This is part of the Full Stack Web Developer course at Udacity.

For more info on courses visit https://www.udacity.com

Calvin Ellington - calvinje@gmail.com
