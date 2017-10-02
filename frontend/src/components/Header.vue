<template>
  <div class="header">
    <input class="filterString" type="text" @change="updateList" v-model="query" autofocus>
  </div>
</template>

<script>
export default {
  data () {
    return {
      query: ''
    }
  },
  methods: {
    updateList: function() {
      console.log(this.query)
    }
  },
  computed: {
    filteredItems() {
      return this.items.filter(item => {
         return item.type.toLowerCase().indexOf(this.search.toLowerCase()) > -1
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
</style>
