<template>
  <nav class="navbar">
    <!-- NAVIGATION MENU -->
    <ul class="nav-links">
      <!-- USING CHECKBOX HACK -->
      <input class="menu_checkbox" type="checkbox" id="checkbox_toggle" />
      <label for="checkbox_toggle" class="hamburger">&#9776;</label>
      <!-- NAVIGATION MENUS -->
      <div class="menu">
        <li><router-link to='/'>Home</router-link></li>
        <li><router-link to='/calculate'>Calculate</router-link></li>
<!--         
        <li class="services">
          <a href="/">Services</a>
          <ul class="dropdown">
            <li><a href="/">Dropdown 1 </a></li>
            <li><a href="/">Dropdown 2</a></li>
            <li><a href="/">Dropdown 2</a></li>
            <li><a href="/">Dropdown 3</a></li>
            <li><a href="/">Dropdown 4</a></li>
          </ul>
        </li>
-->
      </div>
    </ul>
    <!-- LOGO -->
    <div class="logo">Profile radio planner</div>
  </nav>
</template>

<style scoped>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 5px;
  background-color: darkslategray;
  color: #fff;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
  width: 100%;
  height: 35px;
}

.nav-links a {
  color: #fff;
  text-decoration: none;
}

/* LOGO */
.logo {
  font-size: 24px;
}

/* NAVBAR MENU */
.menu {
  display: flex;
  gap: 1em;
  font-size: 14px;
}

.menu li:hover {
  background-color: #4c9e9e;
  border-radius: 2px;
  transition: 0.3s ease;
}

.menu li {
  padding: 5px 5px;
  list-style: none;
}

/* DROPDOWN MENU */
.services {
  position: relative;
}

.dropdown {
  background-color: darkslategray;
  position: absolute; /*WITH RESPECT TO PARENT*/
  display: none;
  border-radius: 2px;
  top: 30px;
}

.dropdown li + li {
  margin-top: 5px;
}

.dropdown li {
  padding: 0.5em 1em;
  width: 9em;
  text-align: center;
}

.dropdown li:hover {
  background-color: #4c9e9e;
}

.services:hover .dropdown {
  display: block;
}

/* CHECKBOX HACK */
input[type=checkbox]{
  display: none;
}

/*HAMBURGER MENU*/
.hamburger {
  display: none;
  font-size: 24px;
  user-select: none;
}

/* APPLYING MEDIA QUERIES */
@media (max-width: 768px) {
  .menu {
    display:none;
    position: absolute;
    background-color:teal;
    right: 0;
    left: 0;
    text-align: center;
    padding: 16px 0;
  }
  .menu li:hover {
    display: inline-block;
    background-color:#4c9e9e;
    transition: 0.3s ease;
  }
  .menu li + li {
    margin-top: 12px;
  }
  input[type=checkbox]:checked ~ .menu{
    display: block;
  }
  .hamburger {
    display: block;
  }
  .dropdown {
    left: 50%;
    top: 30px;
    transform: translateX(35%);
  }
  .dropdown li:hover {
    background-color: #4c9e9e;
  }
}

</style>
