<template>
  <div class="title">
    Instagram Cropping Tool
  </div>
  <!-- Button to upload a file -->
  <div class="boarder">
    <input type="file" id="file" accept="image/*" />
  </div>
  <!-- Div to display the file that is an image -->
	<cropper
		:src="img"
		@change="onChange"
		:debounce="false"
		:stencil-props="{
			aspectRatio: 9 / 16
		}"
	/>
	<preview
		:width="90"
		:height="160"
		:image="result.image"
		:coordinates="result.coordinates"
	/>
  <button 
    @click="crop">
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
      img: 'https://images.unsplash.com/photo-1682687219640-b3f11f4b7234?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      result: {
				coordinates: null,
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
    onChange({ coordinates, image }) {
			this.result = {
				coordinates,
				image
			};
		},
    // crop() {
		// 	const { coordinates, canvas, } = this.$refs.cropper.getResult();
		// 	this.coordinates = coordinates;
		// 	// You able to do different manipulations at a canvas
		// 	// but there we just get a cropped image, that can be used 
		// 	// as src for <img/> to preview result
		// 	this.image = canvas.toDataURL();
		// },
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
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  display: grid;
}

.grid-item {
  background-color: transparent;
  border: 1px dashed;
  font-size: 30px;
  text-align: center;
  color: rgb(255, 0, 0);
}
</style>
