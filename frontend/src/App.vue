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
    <cropper :src="img" ref="cropper" @change="onChange" :debounce="false" :stencil-props="{
      aspectRatio: this.getLocalAspectRatio()
    }" />
  </div>
  <!-- Slider between 1-5 -->
  <div class="slider">
    <input type="range" min="2" max="6" value="1" v-model="sliderValue" id="myRange">
    {{ sliderValue }} {{ this.getLocalAspectRatio() }}
  </div>
  <div class="display-container">
    <div v-for="index in parseInt(this.sliderValue)" :key="index" class="display-preview">
      <preview class="preview-image" :width="90" :height="160" :image="result.image" :coordinates="{
        width: result.coordinates.width / parseInt(this.sliderValue),
        height: result.coordinates.height,
        top: result.coordinates.top,
        left: result.coordinates.left + ((result.coordinates.width / parseInt(this.sliderValue)) * (index - 1))
      }" />
    </div>
  </div>
  <button @click="crop">
    Crop
  </button>
</template>

<script>
import { Cropper, Preview } from 'vue-advanced-cropper';
import 'vue-advanced-cropper/dist/style.css';

export default {
  name: 'APP',
  components: {
    Cropper,
    Preview
  },
  props: {
  },
  data() {
    return {
      file: null,
      sliderValue: 2,
      img: 'https://images.unsplash.com/photo-1682687219640-b3f11f4b7234?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      result: {
        coordinates: {
          width: 0,
          height: 0,
          top: 0,
          left: 0
        },
        image: null
      }
    }
  },
  watch: {
  },
  mounted() {
    document.getElementById("file").addEventListener("change", this.onFileChange);
  },
  methods: {
    // onFileChange(e) {
    //   this.file = e.target.files[0];
    //   if (this.file) {
    //     const reader = new FileReader();
    //     reader.onload = (e) => {
    //       this.img = e.target.result;
    //     };
    //     reader.readAsDataURL(this.file);
    //   }
    // },
    getLocalAspectRatio() {
      return (this.sliderValue * 9) / 16;
    },
    onChange({ coordinates, image }) {
      this.result = {
        coordinates,
        image
      };
    },
    crop() {
      //Do logic here to save n amount of photos based on the selected amount to get proper cropping
      const { coordinates, canvas, } = this.$refs.cropper.getResult();
      this.image = canvas.toDataURL();
      const newWidth = coordinates.width / parseInt(this.sliderValue);
      const link = document.createElement('a');
      link.download = 'image.png';
      link.href = this.image;
      link.click();
    },
  }
}
</script>

<style scoped>
.title {
  font-size: 2em;
  text-align: center;
}

.image-container {
  display: inline-block;
  max-height: 40%;
  max-width: 70%;
}

.display-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.display-preview {
  max-height: 40%;
  max-width: 70%;
  padding: 10px;
}

.preview-image {
  background-color: aliceblue;

}
</style>
