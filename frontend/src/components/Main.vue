<template>
  <div class="main">

    <div class="item" v-for="item in newsToShow">
      <a :href="item.url" style="text-decoration:none; color:#3F6083">
      <div>
        <img v-bind:src="item.urlToImage" />
      
      <div class="news-content">
        <div>{{ item.title }}</div>
        <div>{{ item.text }}</div>
      </div>
    </div>
    </a>
    </div>

  </div>
</template>

<script>
export default {
  data () {
    return {
      url: 'https://konchytsv.pythonanywhere.com',
      news: [],
      newsToShow: [],
      filterQuery: '',
      loader: false
    }
  },
  created: async function () {
    this.loader = true
    for (let i = 0; i < 8; i++) {
      this.news.push(await this.callAPI())
    }
    console.log(this.news)
    this.newsToShow = this.news
    this.loader = false

    for (let i = 0; i < 8; i++) {
      setInterval(async () => {
        this.news.splice(i, 1, (await this.callAPI()))
      }, getRandomDelay(1000, 4000))
    }
  },
  methods: {
    updateList: function() {
      this.newsToShow = this.filteredNews
    },
    callAPI: function() {
      return new Promise((resolve, reject) => {
        this.$http.get(this.url + '/article/').then(res => {
        resolve(res.body)
        }).catch(e => console.log(e))
      })
    }
  }
}
function getRandomDelay (min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .title {
    background-color: #8CA0B7;
    color: #fff;
    padding: 2px;
  }
  .main {
    column-count: 4;
    column-gap: 1;
    width: 100vw;
  }
  .item {
    margin-top: 2%;
    border: 1px solid #8CA0B7;
    background-color: #F5F7F9;
    -webkit-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
    -moz-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
    box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
    display: inline-block;
    width: 90%;
    vertical-align: top;
  }
  .item img {
    position: relative;
    width: 100%;
  }
  .news-content {
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    padding: 5px;
  }
  .link {
    vertical-align: middle;
    position: relative;
    float: left;
    cursor: pointer;
  }
  .link:hover {
    color: #F5F7F9;
  }

</style>
