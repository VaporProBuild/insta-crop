<template>
  <div class="boarder">
    Instagram Cropping Tool
  </div>
  <!-- Button to upload a file -->
  <div class="boarder">
    <input type="file" id="file" accept="image/*" />
  </div>
  <!-- Div to display the file that is an image -->
  <div class="boarder">
    <img id="image" />
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
export default {
  name: "App",
  setup() {
    const file = ref(null);
    const image = ref(null);
    const onFileChange = (e) => {
      file.value = e.target.files[0];
    };
    onMounted(() => {
      document.getElementById("file").addEventListener("change", onFileChange);
    });
    return {
      file,
      image,
    };
  },
};
</script>

<style scoped>
.boarder {
  border: 1px solid rgb(255, 255, 255);
  width: 100%;
  height: 100%;
}
</style>
