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
    <input type="range" min="1" max="8" value="1" v-model="sliderValue" id="myRange">
    {{ sliderValue }} {{ this.getLocalAspectRatio() }}
  </div>
  <div class="display-container">
    <div v-for="index in parseInt(this.sliderValue)" :key="index" class="display-preview">
      <preview :id="'previewimage' + index" :width="90" :height="160" :image="result.image" :coordinates="{
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
      sliderValue: 1,
      img: null,
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
    onFileChange(e) {
      this.file = e.target.files[0];
      if (this.file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.img = e.target.result;
        };
        reader.readAsDataURL(this.file);
      }
    },
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
      const { coordinates, canvas } = this.$refs.cropper.getResult();
      const newWidth = coordinates.width / parseInt(this.sliderValue);

      for (let i = 0; i < parseInt(this.sliderValue); i++) {
        const x = 0 + (newWidth * i);
        const y = coordinates.top;
        const croppedImage = document.createElement('canvas');
        const ctx = croppedImage.getContext('2d');

        // //https://www.w3schools.com/jsref/canvas_drawimage.asp
        // Set the dimensions of the cropped image canvas
        croppedImage.width = newWidth;
        croppedImage.height = coordinates.height;

        // Draw the first half of the image onto the cropped image canvas
        ctx.drawImage(
          canvas,
          x, // Start X position in the original image
          y, // Start Y position in the original image
          newWidth, // Width of the portion to draw (half of the original width)
          coordinates.height, // Height of the portion to draw (full height of the original image)
          0, // Destination X position in the cropped image canvas
          0, // Destination Y position in the cropped image canvas
          newWidth, // Width of the drawn portion in the cropped image canvas
          coordinates.height // Height of the drawn portion in the cropped image canvas
        );

        // Convert the canvas to a blob with specified format and quality
        croppedImage.toBlob((blob) => {
          // Create a download link
          const link = document.createElement('a');
          link.download = 'image.png';

          // Create a URL for the blob and set it as the href of the link
          link.href = URL.createObjectURL(blob);

          // Append the link to the document
          document.body.appendChild(link);

          // Trigger a click on the link to initiate the download
          link.click();

          // Remove the link from the document
          document.body.removeChild(link);
        }, 'image/png', 1.0); // You can adjust the format and quality parameters as needed
      }
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
