<template>
  <div id="app">
    <div class="header">
      <icon name="circle-o-notch" scale="1.5" class="loader" spin/>
      <input class="filterString" type="text" @keyup="updateList" v-model="filterQuery" autofocus>
   </div>
    <MainComponent :newsData="newsToShow"> </MainComponent>
  </div>
</template>

<script>
//import HeaderComponent from './components/Header'
import MainComponent from './components/Main'

export default {
  data () {
    return {
      url: 'http://konchytsv.pythonanywhere.com/',
      news: '',
      newsToShow: '',
      filterQuery: ''
    }
  },
  components: {
    MainComponent
  },
  created: function () {
    this.$http.get(this.url + '/articles/').then(res => {
     // console.log(res.body);
      this.news = res.body;
      this.newsToShow = res.body;
    }).catch(e => console.log(e))
  },
  methods: {
    updateList: function() {
      this.newsToShow = this.filteredNews
    }
  },
  computed: {
    filteredNews() {
      return this.news.filter(item => {
         return item.title.toLowerCase().indexOf(this.filterQuery.toLowerCase()) > -1 ||
         item.text.toLowerCase().indexOf(this.filterQuery.toLowerCase()) > -1
      })
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
  .header {
    background: #A5B5C7;
    padding: 1%;
  }
  .filterString {
    outline: none;
    padding: 0.5%;
    font-size: 1.2em;
    border-radius: 3px;
    border: none;
  }
  .loader {
    color: #fff;
    vertical-align: middle;
    float: left;
  }
</style>
