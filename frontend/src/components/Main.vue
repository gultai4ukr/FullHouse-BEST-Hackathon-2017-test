<template>
  <div class="main">
    <div class="item" v-for="item in newsData">
      <div class="title"> {{ item.title }} <icon name="external-link" scale="1" class="link"></icon> </div>
      <div class="content"> {{ item.text }} </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['newsData'],
  data () {
    return {
      
    }
  }
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
    flex-direction: column;
    justify-content: center;
  }
  .item {
    border: 1px solid #8CA0B7;
    margin: 1% auto;
    width: 70%;
    background-color: #F5F7F9;
    -webkit-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
    -moz-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
    box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
  }
  .content {
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
