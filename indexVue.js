function updateName(e) {
  console.log(" e", e);
  console.log("update name called", this.name);
}
var app = new Vue({
  el: "#app",
  data: {
    name: "",
    message: "Good Morning",
    display: false,
    names:['anisha','somya','sanyam']
  },
  methods: {
    updateName,
    mouseover() {
      this.display = !this.display
    },
  },
});
