<template>
  <div id="app">
    <div class="header"></div>
    <icon name="circle-o-notch" scale="2" class="loader" v-if="loader" spin/>
    <MainComponent :items="newsToShow"> </MainComponent>
  </div>
</template>

<script>
//import HeaderComponent from './components/Header'
import MainComponent from './components/Main'

export default {
  components: {
    MainComponent
  },

  data () {
    return {
      url: 'https://konchytsv.pythonanywhere.com',
      news: '',
      newsToShow: '',
      filterQuery: '',
      loader: false
    }
  },
  created: async function () {
    // this.loader = true
    // this.news = await this.callAPI()
    // console.log(this.news)
    // this.newsToShow = this.news
    // this.loader = false
    },
  methods: {
    callAPI: function() {
      return new Promise((resolve, reject) => {
        this.$http.get(this.url + '/article/').then(res => {
        resolve(res.body)
        }).catch(e => console.log(e))
      })
    },
  },
  computed: {
    // filteredNews() {
    //   return this.news.filter(item => {
    //      return item.title.toLowerCase().indexOf(this.filterQuery.toLowerCase()) > -1 ||
    //      item.text.toLowerCase().indexOf(this.filterQuery.toLowerCase()) > -1
    //   })
    // }
  },
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
    position: relative;
    display: block;
    margin: 1% auto;
    color: #999;
  }
</style>
