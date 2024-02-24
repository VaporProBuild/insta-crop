# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

## Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).


# insta-crop
Crop photos for instagram to fit as a swipe pano or for your feed!

# Description
Download executable file for Mac or Windows to use a discoverable app. It uses Tkinter for the GUI and a custom python backend. Very lightweight and easy to use!

## Testing
Start a virtual environment and install the requirements.
```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

Use the `instacrop.py` script to crop your photos. It will create a new folder called `cropped` with the cropped photos. Run with command below.
```
python3 instacrop.py
```

To make this into a executable to share simply use the 

```pyinstaller --noconsole --name "Insta-Crop" app.py```

To redeploy app
```npm run deploy```
https://mkay11.medium.com/how-to-deploy-your-vite-vue-3-application-in-github-pages-2023-2b842f50576a
