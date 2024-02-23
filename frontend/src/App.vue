<template>
  <div class="title">
    Instagram Cropping Tool
  </div>
  <!-- Button to upload a file -->
  <div class="boarder">
    <input type="file" id="file" accept="image/*" />
  </div>
  <!-- Div to display the file that is an image -->
  <div class="image-container">
    <img id="image" :src="image" alt="Uploaded Image" />
    <div class="grid-container">
      <div class="grid-item"></div>
      <div class="grid-item"></div>
      <div class="grid-item"></div>
      <div class="grid-item"></div>
      <div class="grid-item"></div>
      <div class="grid-item"></div>
      <div class="grid-item"></div>
      <div class="grid-item"></div>
      <div class="grid-item"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'APP',
  props: {
  },
  data() {
    return {
      file: null,
      image: null,
    }
  },
  watch: {
  },
  mounted() {
    document.getElementById("file").addEventListener("change", this.onFileChange);
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0];
      if (this.file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.image = e.target.result;
        };
        reader.readAsDataURL(this.file);
      }
    }
  }
}
</script>

<style scoped>
.title {
  font-size: 2em;
  text-align: center;
}

.image-container {
  position: relative;
  display: inline-block;
  width: 95%;
  height: 95%;
}

#image {
  width: 100%;
}

.grid-container {
  position:absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  display: grid;
  grid-template-columns: auto auto auto;
}
.grid-item {
  background-color:transparent;
  border: 1px dashed;
  font-size: 30px;
  text-align: center;
  color: rgb(255, 0, 0);
}
</style>
