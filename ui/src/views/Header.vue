<template>
  <div class="row">
    <div class="col-md-12">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <!--<a class="navbar-brand" href="/">BCE</a>-->
        <router-link class="navbar-brand" to="/">BCE</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <!--<a class="nav-link" href="/risks">Create Risk <span class="sr-only">(current)</span></a>-->
              <router-link class="nav-link" to="/risks"
                >Create Risk</router-link
              >
            </li>
            <li class="nav-item">
              <!--<a class="nav-link" href="/risk-types">Manage Risk Types</a>-->
              <router-link class="nav-link" to="/risk-types"
                >Manage Risk Types</router-link
              >
            </li>
          </ul>
          <ul class="navbar-nav navbar-right">
            <li class="nav-item">
              <!--<a class="nav-link" (click)="logout()" >Log Out</a>-->
              <router-link to="/login">Logout</router-link>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header"
};
</script>

<style scoped></style>
