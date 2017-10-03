<template>
  <div id="app">
    <div class="sidebar">
      <div style="background-color:#8CA0B7" @click="changeParam('?language=de')"><icon name="globe"/> <font>DE</font></div>
      <div style="background-color:#8CA0B7" @click="changeParam('?language=en')"><icon name="globe"/> <font>EN</font></div>
      <div @click="changeParam('?category=music')"><icon name="music"/> <font>Music</font></div>
      <div @click="changeParam('?category=business')"><icon name="briefcase"/> <font>Business</font></div>
      <div @click="changeParam('?category=entertainmen')"><icon name="ravelry"/> <font>Entertainment</font></div>
      <div @click="changeParam('?category=gaming')"><icon name="gamepad"/> <font>Gaming</font></div>
      <div @click="changeParam('?category=general')"><icon name="newspaper-o"/> <font>General</font></div>
      <div @click="changeParam('?category=sport')"><icon name="heartbeat"/> <font>Sport</font></div>
      <div @click="changeParam('?category=politics')"><icon name="handshake-o"/> <font>Politics</font></div>
      <div @click="changeParam('?category=technology')"><icon name="cogs"/> <font>Technology</font></div>
      <div @click="changeParam('?category=science-and-nature')"><icon name="leaf"/> <font>Science and nature</font></div>
      <div style="background-color:#F45B69" @click="changeParam('?country=it')"><icon name="flag"/> <font>Italy</font></div>
      <div style="background-color:#F45B69" @click="changeParam('?country=us')"><icon name="flag"/> <font>USA</font></div>
      <div style="background-color:#F45B69" @click="changeParam('?country=gb')"><icon name="flag"/> <font>Great Britain</font></div>
    </div>
    <MainComponent :param="param"> </MainComponent>
  </div>
</template>

<script>
import MainComponent from './components/Main'

export default {
  components: {
    MainComponent
  },
  data() {
    return {
      param: ''
    }
  },
  methods: {
    changeParam: function(query) {
      this.param = query
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Open+Sans');
  body, html {
      font-family: 'Open Sans', sans-serif;
      margin: 0;
      padding: 0;
      background-color: rgb(250, 250, 252);
    }
  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  .sidebar {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    width: 10vw;
    visibility: visible;
    transition: 0.5s;
    z-index: 1000;
  }
  .sidebar div {
    text-align: center;
    color: #fff;
    background-color: #506E92;
    transition: 0.5s;
    transform: translate(0px, 0px);
    cursor: pointer;
    padding: 5px;
  }
  .sidebar div:hover {
    color: #506E92;
    background-color: #fff;
  }
  div icon div font {
    display: inline-block;
    vertical-align: middle;
  }
  .loader {
    position: fixed;
    left: 40px;
    bottom: 30px;
    margin-top: auto;
    margin-bottom: auto;
    color: #3F6083;
  }
</style>
