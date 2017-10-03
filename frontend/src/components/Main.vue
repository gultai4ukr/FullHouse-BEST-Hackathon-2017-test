<template>
  <div class="main">
    <!--ость так я думаю будуть йти параметри в метод при кліку,
     якщо будуть інші пропозиції переробим, просто що в голову прийшло те і зробив-->
    <button @click="updateNews(category[0], filterQuery[0])">CLICK ME</button>
    <div class="item" v-for="item in newsToShow">
      <a :href="item.url" style="text-decoration:none; color:#3F6083">
      <div>
        <img v-bind:src="item.urlToImage" />

      <div class="news-content">
        <div>{{ item.title }}</div>
        <div>{{ item.text }}</div>
        <div>{{ articleTime }}</div>
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
      filterQuery: ['category', 'country', 'language'],
      category: [
        'business', 'entertainment', 'gaming', 'general', 'music',
        'politics', 'science-and-nature', 'sport', 'technology'
      ],
      country:  ['au', 'de', 'gb', 'in', 'it', 'us'],
      language: ['de, en'],
      loader: false,
      articleTime: ''
    }
  },
  created: async function () {
    this.loader = true;
    for (let i = 0; i < 8; i++) {
      this.news.push(await this.callAPI())
    }

    for(let i = 0; i < this.news.length; i++){
      let date = new Date(this.news[i].publishedAt);
      this.articleTime = date.toLocaleString();
    }
    this.newsToShow = this.news;
    this.loader = false;

   for (let i = 0; i < 8; i++) {
      setInterval(async () => {
        this.news.splice(i, 1, (await this.callAPI()))
      }, getRandomDelay(1000, 4000))
    }
  },
  methods: {
    /**
     * @returns {Promise}
     * @param param {string} depends of button -> category || country
     */
    callAPI: function(param) {
      return new Promise((resolve, reject) => {
        if (param) {
          this.$http.get(this.url + '/article/' + param).then(res => {
            resolve(res.body)
          }).catch(e => console.log(e))
        } else {
          this.$http.get(this.url + '/article/').then(res => {
            resolve(res.body)
          }).catch(e => console.log(e))
        }
      })
    },
    /**
     * @param param {string} type of category || country
     * @param type {string} type of filter
     */
    updateNews : function(param, type) {
      this.news.splice(0, this.news.length);
      let getParam = "?" + type + "=" + param;
      let self = this;
      setTimeout(async function () {
        for(let i = 0; i < 8; i++) {
          self.news.push(await self.callAPI(getParam));
        }
      }, 4000);
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
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-wrap: wrap;
    align-items:stretch
  }
  .item {
    border: 1px solid #8CA0B7;
    background-color: #F5F7F9;
    margin: 0.5%;
    width:20%;
    position: relative;
    max-width: 20%;
    height: auto;
    -webkit-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
    -moz-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
    box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
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
