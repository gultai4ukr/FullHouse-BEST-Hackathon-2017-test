<template>
  <div class="main">
    <icon name="circle-o-notch" scale="2" class="loader" v-if="loader" spin/>
    <div class="item" v-for="item in news">
      <a :href="item.url" style="text-decoration:none; color:#3F6083">
      <div>
        {{ !item.urlToImage ? item.urlToImage = 'https://www.jordans.com/~/media/jordans%20redesign/no-image-found.ashx?h=275&la=en&w=275&hash=F87BC23F17E37D57E2A0B1CC6E2E3EEE312AAD5B' : null }}
        <img v-bind:src="item.urlToImage" />

      <div class="news-content">
        <div>{{ item.title }}</div>
        <div>{{ item.text }}</div>
        <div class="date">{{ articleTime }}</div>
      </div>
    </div>
    </a>
    </div>

  </div>
</template>

<script>
export default {
  props: ['param'],
  data () {
    return {
      url: 'https://konchytsv.pythonanywhere.com',
      news: [],
      loader: false,
      articleTime: ''
    }
  },
  created: async function () {
    this.loader = true;
    for (let i = 0; i < 18; i++) {
      this.news.push(await this.callAPI())
      let date = new Date(this.news[i].publishedAt)
      this.articleTime = date.toLocaleString()

      setInterval(async () => {
        this.news.splice(i, 1, (await this.callAPI()))
      }, getRandomDelay(14000, 17000))
    }

    this.loader = false;
  },
  watch: {
    news: function() {
      this.loader = true
      setTimeout(() => this.loader = false, 2500)
    }
  },
  methods: {
    /**
     * @returns {Promise}
     */
    callAPI: function() {
      return new Promise((resolve, reject) => {
        if (this.param) {
          this.$http.get(this.url + '/article/' + this.param).then(res => {
            resolve(res.body)
          }).catch(e => console.log(e))
        } else {
          this.$http.get(this.url + '/article/').then(res => {
            resolve(res.body)
          }).catch(e => console.log(e))
        }
      })
    },
    changeURL: function (param) {
      this.param = param
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
    column-gap: 0;
    width: 90vw;
    float: right;
    overflow: hidden;
  }
  .item {
    margin: 3%;
    margin-top: 2%;
    border: 1px solid #8CA0B7;
    background-color: #F5F7F9;
    -webkit-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
    -moz-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
    box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
    display: inline-block;
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
  .date {
    background-color: #ccc;
  }
</style>
