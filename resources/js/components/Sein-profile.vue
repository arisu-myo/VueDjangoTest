<template></template>

<script>
export default {
  data() {
    return {
      msg: null,
    };
  },
  mounted() {
    this.$router.push("/profile");
  },
  //   methods: {
  //     redirect: function () {
  //       this.$$router.push("/profile");
  //     },
  //   },
};
</script>